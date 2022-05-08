""" Base class for face detectors """

from abc import ABC, abstractmethod


class FaceDetector(ABC):
    """Base class for all face detectors"""

    @abstractmethod
    def detect(self, image: bytes, **kwargs) -> list[tuple[int, int, int, int]]:
        """
        Detects faces on image.

        Args:
            image: input image.
            **kwargs: extra parameters required for detection.

        Returns:
            List of face bounding box coordinates in following format:
              [(xmin, ymin, xmax, ymax), ...]
        """
