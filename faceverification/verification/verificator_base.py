""" Base class for all verificators """

from abc import ABC, abstractmethod


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
            Is a person on two photos the same or not.
        """
