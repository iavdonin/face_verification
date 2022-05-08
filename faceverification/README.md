# Face verification library

## Requirements

Python 3.9

## Install dependencies

```bash
pip install -r requirements.txt
```

## Python API Usage

Usage example:
```python
from faceverification import DefaultFaceVerificator


# read images to verify
with open('photo1.png', 'rb') as photo_file_1, open('photo2.png', 'rb') as photo_file_2:
    photo_1 = photo_file_1.read()
    photo_2 = photo_file_2.read()

# create face verificator
face_verificator = DefaultFaceVerificator()

# ferify face
is_verified = face_verificator.verify(photo_1, photo_2)

# print result
if is_verified:
    print('Person is verified')
else:
    print('Person is NOT verified')
```

# CLI usage

```bash
python verify.py path/to/photo1.jpeg path/to/photo2.jpeg
```