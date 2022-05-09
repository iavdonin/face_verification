""" faceverification lib exceptions """


class FaceVerificationError(Exception):
    """Base exception class for all faceverification lib exceptions"""


class FaceNotFoundError(FaceVerificationError):
    """Exception raised when no faces found on passed image"""
    
    
class MultipleFacesError(FaceVerificationError):
    """Exception raised when there are more than one face on image"""


class BoundingBoxSizeError(FaceVerificationError):
    """Exception raised when face bounding box is too small"""
    
    
class ImageSizeError(FaceVerificationError):
    """Exception raised when passed image is too small"""
    
    
class PresentationAttackError(FaceVerificationError):
    """Exception raised when presentation attack is detected"""