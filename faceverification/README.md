# Face verification library

## Requirements

Python 3.9

## Install package

### With pip
```bash
pip install .
```

### With poetry
```bash
poetry install
```

## Python API Usage

Usage example:
```python
from faceverification.verification import get_default_face_verificator


# read images to verify
with open('photo1.png', 'rb') as photo_file_1, open('photo2.png', 'rb') as photo_file_2:
    photo_1 = photo_file_1.read()
    photo_2 = photo_file_2.read()

# create face verificator
face_verificator = get_default_face_verificator()

# ferify face
is_verified, _ = face_verificator.verify(photo_1, photo_2)

# print result
if is_verified:
    print('Verification is passed')
else:
    print('Verification is NOT passed')
```

## CLI usage

```bash
python verify.py path/to/photo1.jpeg path/to/photo2.jpeg
```