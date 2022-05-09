""" Face verification system specific errors and exception """

from .exceptions import (
    FaceVerificationError,
    FaceNotFoundError,
    MultipleFacesError,
    BoundingBoxSizeError,
    ImageSizeError,
    PresentationAttackError
)

__all__ = [
    'FaceVerificationError',
    'FaceNotFoundError',
    'MultipleFacesError',
    'BoundingBoxSizeError',
    'ImageSizeError',
    'PresentationAttackError' 
]
