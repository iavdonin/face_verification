""" 
Distance metrics classes.
Here are used metrics implementations from deepface library 
https://github.com/serengil/deepface
"""

from abc import ABC, abstractmethod
from typing import Tuple

import numpy as np


class DistanceMetric(ABC):
    """Base class for distance metric classes"""

    @abstractmethod
    def get_distance(
        self, first_vector: Tuple[float], second_vector: Tuple[float]
    ) -> float:
        """Calculates distance metric between two vectors"""


class CosineDistance(DistanceMetric):
    """Cosine distance metric calculator"""

    def get_distance(
        self, first_vector: Tuple[float], second_vector: Tuple[float]
    ) -> float:
        """Calculates cosine distance metric between two vectors"""
        first_vector = np.asarray(first_vector)
        second_vector = np.asarray(second_vector)
        a = np.matmul(np.transpose(first_vector), second_vector)
        b = np.sum(np.multiply(first_vector, second_vector))
        c = np.sum(np.multiply(first_vector, second_vector))
        return 1 - (a / (np.sqrt(b) * np.sqrt(c)))


class EuclideanDistance(DistanceMetric):
    """
    Euclidean distance metric calculator

    Args:
        l2_normalization: use vector l2 normalization.
    """

    def __init__(self, l2_normalization: bool = False) -> None:
        self.l2_normalization = l2_normalization

    def get_distance(
        self, first_vector: Tuple[float], second_vector: Tuple[float]
    ) -> float:
        """Calculates Euclidean distance metric between two vectors"""
        first_vector = np.asarray(first_vector)
        second_vector = np.asarray(second_vector)
        if self.l2_normalization:
            first_vector = l2_normalize(first_vector)
            second_vector = l2_normalize(second_vector)
        euclidean_distance = first_vector - second_vector
        euclidean_distance = np.sum(np.multiply(euclidean_distance, euclidean_distance))
        euclidean_distance = np.sqrt(euclidean_distance)
        return euclidean_distance


def l2_normalize(x):
    return x / np.sqrt(np.sum(np.multiply(x, x)))
