""" Base class for all face embeddings models """

from abc import ABC, abstractmethod
from typing import Collection


class FaceEmbeddingModel(ABC):
    """Base class for models that calculates face embedding"""

    @abstractmethod
    def get_embedding(self, face_image: bytes, **kwargs) -> Collection[float]:
        """Returns face image emgedding"""
