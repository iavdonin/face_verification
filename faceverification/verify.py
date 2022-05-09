""" Script for face verification systems inference """

import argparse

from faceverification.verification import get_default_face_verificator


def main(path_to_first_image: str, path_to_second_image: str) -> None:

    # create face verificator
    face_verificator = get_default_face_verificator()

    # read images to verify
    with open(path_to_first_image, "rb") as imf1, open(
        path_to_second_image, "rb"
    ) as imf2:
        first_image = imf1.read()
        second_image = imf2.read()

    # verify
    is_verified, score = face_verificator.verify(first_image, second_image)

    # print result
    if is_verified:
        print(f"Verification is passed, distance: {score}")
    else:
        print(f"Verificaiton is NOT passed, distance: {score}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path_to_first_image", help="Path to first photo")
    parser.add_argument("path_to_second_image", help="Path to second photo")
    args = parser.parse_args()
    main(args.path_to_first_image, args.path_to_second_image)
