""" Module with models to get face embeddings """

from .embedding_base import FaceEmbeddingModel
from .facenet_embedding import InceptionResnetV1EmbeddingModel

__all__ = ["FaceEmbeddingModel", "InceptionResnetV1EmbeddingModel"]
