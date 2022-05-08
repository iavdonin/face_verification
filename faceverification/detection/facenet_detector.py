""" 
Face detection model with pretrained face detection models from facenet-pytorch 
https://github.com/timesler/facenet-pytorch
"""

import torch
from facenet_pytorch import MTCNN

from .detector_base import FaceDetector
from ..utils.image import read_image_from_bytes


class MTCNNDetector(FaceDetector):
    """
    MTCNN face detector.

    Args:
        threshold: face detection threshold. Should be in range [0.0, 1.0].
        device: device on which The device on which to run neural net passes. Image tensors and
          models are copied to this device before running forward passes. (default: `cpu`)
        **kwargs: other keyword arguments, that will be passed to facnet-pytorch MTCNN
          implementation. See
          https://github.com/timesler/facenet-pytorch/blob/master/models/mtcnn.py
    """

    def __init__(self, threshold: float = 0.5, device: str = "cpu", **kwargs) -> None:
        if device == "gpu":
            device = torch.device("cuda")
        else:
            device = torch.device(device)
        self.threshold = threshold
        self.mtcnn_model = MTCNN(device=device, **kwargs)

    def detect(self, image: bytes, **kwargs) -> list[tuple[int, int, int, int]]:
        """Returns detected faces coordinates"""
        image = read_image_from_bytes(image)
        boxes, probs = self.mtcnn_model.detect(image)
        filtered_boxes = []
        for box, prob in zip(boxes, probs):
            if prob >= self.threshold:
                filtered_boxes.append(tuple(box.tolist()))
        return filtered_boxes
