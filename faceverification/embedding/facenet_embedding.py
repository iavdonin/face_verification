""" 
Face embedding model with pretrained face recognition models from facenet-pytorch 
https://github.com/timesler/facenet-pytorch
"""

from typing import Literal, Tuple

import torch
from facenet_pytorch import InceptionResnetV1

from .embedding_base import FaceEmbeddingModel
from ..utils.image import read_image_from_bytes


class InceptionResnetV1EmbeddingModel(FaceEmbeddingModel):
    """
    Face embedding model with Inception ResNet v1 backbone

    Args:
        pretrained: pretrained weights. Should be one of: None, `vggface2`, `casia-webface`
    """

    def __init__(
        self,
        pretrained: Literal["vggface2", "casia-webface"] = "vggface2",
        device: str = "cpu",
    ) -> None:
        if device == "gpu":
            device = torch.device("cuda")
        else:
            device = torch.device(device)
        self.device = device
        self.inception_resnet_model = (
            InceptionResnetV1(pretrained=pretrained).to(device).eval()
        )

    def get_embedding(self, face_image: bytes) -> Tuple[float]:
        """Returns face embedding"""
        face_image = read_image_from_bytes(face_image)
        face_image = torch.from_numpy(face_image).to(self.device)
        with torch.no_grad():
            embedding = self.inception_resnet_model(face_image.unsqueeze(0))
        embedding = embedding.squeeze().detach().cpu().tolist()
        return tuple(embedding)
