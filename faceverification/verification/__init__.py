""" Module with face verification tools """

from faceverification.detection import MTCNNDetector
from faceverification.embedding import InceptionResnetV1EmbeddingModel
from faceverification.distance.metrics import EuclideanDistance
from .verificator_base import FaceVerificator, CustomClassicVerificator

__all__ = [
    "FaceVerificator",
    "CustomClassicVerificator",
    "get_default_face_verificator",
]


def get_default_face_verificator(device: str = "cpu") -> FaceVerificator:
    return CustomClassicVerificator(
        face_detector=MTCNNDetector(device=device),
        face_embedding_model=InceptionResnetV1EmbeddingModel(device=device),
        distance_metric=EuclideanDistance(l2_normalization=True),
        detector_threshold=0.8,
        verificator_threshold=0.9,
        face_crop_size=(160, 160),
    )
