""" Module with models to detect faces """

from .detector_base import FaceDetector
from .facenet_detector import MTCNNDetector

__all__ = ["FaceDetector", "MTCNNDetector"]
