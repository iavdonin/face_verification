from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel
from faceverification.verification import get_default_face_verificator
from faceverification.exceptions import (
    FaceNotFoundError,
    MultipleFacesError,
    PresentationAttackError,
)


class VerificationRequest(BaseModel):
    first_image: bytes
    second_image: bytes


class ExitCode(Enum):
    SUCCESS = 0
    ERROR = 1


verificator = get_default_face_verificator()
app = FastAPI()


@app.post("/")
async def verificate(request: VerificationRequest):
    request_dict = request.dict()
    first_image = request_dict["first_image"]
    second_image = request_dict["second_image"]

    try:
        is_verified, _ = verificator.verify(first_image, second_image)
    except FaceNotFoundError:
        is_verified = False
        exit_code = ExitCode.SUCCESS
        err_msg = (
            "Верификация не пройдена, т.к. не найдено лицо на изображении. "
            "Проверьте изображения или попробуйте переснять фотографию."
        )
    except MultipleFacesError:
        is_verified = False
        exit_code = ExitCode.SUCCESS
        err_msg = (
            "Верификация не пройдена, т.к. найдено несколько лиц на изображении. "
            "Проверьте изображения или попробуйте переснять фотографию."
        )
    except PresentationAttackError:
        is_verified = False
        exit_code = ExitCode.SUCCESS
        err_msg = "Верификация не пройдена (обнаружена атака)"
    except Exception as e:
        is_verified = False
        exit_code = ExitCode.ERROR
        err_msg = "Error on the server side"
    else:
        exit_code = ExitCode.SUCCESS
        err_msg = ""
    return {"exit_code": exit_code, "err_msg": err_msg, "is_verified": is_verified}
