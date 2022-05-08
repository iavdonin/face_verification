""" Base class for all face embeddings models """

from abc import ABC, abstractmethod
from typing import Tuple


class FaceEmbeddingModel(ABC):
    """Base class for models that calculates face embedding"""

    @abstractmethod
    def get_embedding(self, face_image: bytes, **kwargs) -> Tuple[float]:
        """Returns face image emgedding"""
