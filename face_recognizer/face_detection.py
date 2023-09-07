from mtcnn import MTCNN
import cv2

class FaceDetector:
    def __init__(self):
        self.detector = MTCNN()

    def detect_face(self, image):
        return self.detector.detect_faces(image)

    def detect_face_in_image(self, image_path):
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return self.detect(image)
