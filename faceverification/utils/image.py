""" Utils for image processing """

import cv2
import numpy as np


def read_image_from_bytes(image: bytes) -> np.ndarray:
    """Read image from bytes. Returns NumPy array with image in BGR format"""
    image = cv2.imdecode(np.frombuffer(image, dtype=np.uint8), cv2.IMREAD_COLOR)
    return image
