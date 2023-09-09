
# Installation
```
pip install git+https://github.com/rcmalli/keras-vggface.git@bee35376e76e35d00aeec503f2f242611a97b38a
pip install face_identifier
```

# Usage
```python
import face_identifier
import cv2

image1 = cv2.imread('path/to/image1.jpg')
image2 = cv2.imread('path/to/image2.jpg')
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
face_identifier.is_faces_matched(image1, image2) # True or False
```