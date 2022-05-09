""" Utils for image processing """

from typing import Optional, Tuple

import cv2
import torch
import numpy as np


def read_image_from_bytes(image: bytes) -> np.ndarray:
    """Read image from bytes. Returns NumPy array with image in BGR format"""
    image = cv2.imdecode(np.frombuffer(image, dtype=np.uint8), cv2.IMREAD_COLOR)
    return image


def crop(
    image: bytes,
    coordinates: tuple[int, int, int, int],
    out_size: Optional[Tuple[int, int]] = None,
) -> bytes:
    """
    Crops image by coordinates.

    Args:
        image: full image.
        coordinates: crop coordinates in following format [xmin, ymin, xmax, ymax].
        out_size: out image size (height, width). If passed, face crop will be resized to
          that size.

    Returns:
        Cropped image.
    """
    image = read_image_from_bytes(image)
    xmin, ymin, xmax, ymax = coordinates
    crop = image[ymin:ymax, xmin:xmax]
    if out_size is not None:
        crop = cv2.resize(crop, out_size)
    return cv2.imencode(".png", crop)[1].tostring()


def fixed_image_standardization(image_tensor: torch.Tensor) -> torch.Tensor:
    """Returns standartized tensor"""
    processed_tensor = (image_tensor - 127.5) / 128.0
    return processed_tensor
