""" Base class for all verificators """

from abc import ABC, abstractmethod
from typing import Optional, Tuple

from faceverification.detection.detector_base import FaceDetector
from faceverification.embedding.embedding_base import FaceEmbeddingModel
from faceverification.distance.metrics import DistanceMetric
from faceverification.utils.image import crop


class FaceVerificator(ABC):
    """Base class for all face verificators"""

    @abstractmethod
    def verify(self, first_photo: bytes, second_photo: bytes, **kwargs) -> bool:
        """
        Verifies person by two photos.

        Args:
            first_photo: first persons' photo.
            second_photo: second persons' photo.
            **kwargs: extra parameters required for verification

        Returns:
            Is a person on two photos the same or not and verification distance (Tuple[bool, float]).
        """


class CustomClassicVerificator(FaceVerificator):
    """
    Custom verificator class using to build verificaiton pipeline.

    Args:
        face_detector: face detecion model.
        face_embedding_model: face embedding model.
        distance_metric: distance metric.
        detector_threshold: face detector probability threshold to keep face coordinates.
        verificator_threshold: face verificator threshold to verify person.
        face_crop_size: face crop size that will be passed to face embedding model.
    """

    def __init__(
        self,
        face_detector: FaceDetector,
        face_embedding_model: FaceEmbeddingModel,
        distance_metric: DistanceMetric,
        detector_threshold: float = 0.8,
        verificator_threshold: float = 0.8,
        face_crop_size: Optional[tuple[int, int]] = None,
    ) -> None:
        self.face_detector = face_detector
        self.face_embedding_model = face_embedding_model
        self.distance_metric = distance_metric
        self.detector_threshold = detector_threshold
        self.verificator_threshold = verificator_threshold
        self.face_crop_size = face_crop_size

    def _get_face_embedding(self, image: bytes) -> tuple[float]:
        boxes = self.face_detector.detect(image)
        box = boxes[0]
        face_crop = crop(image, box, self.face_crop_size)
        embedding = self.face_embedding_model.get_embedding(face_crop)
        return embedding

    def verify(self, first_photo: bytes, second_photo: bytes) -> Tuple[bool, float]:
        """
        Verifies person by two photos.

        Args:
            first_photo: first persons' photo.
            second_photo: second persons' photo.

        Returns:
            Is a person on two photos the same or not and verification score (Tuple[bool, float]).
        """
        first_emb = self._get_face_embedding(first_photo)
        second_emb = self._get_face_embedding(second_photo)
        distance = self.distance_metric.calculate(first_emb, second_emb)
        is_verified = True if distance < self.verificator_threshold else False
        return is_verified, distance
