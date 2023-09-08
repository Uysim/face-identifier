from mtcnn import MTCNN

face_detector = MTCNN()
def detect_face(image):
    face = face_detector.detect_faces(image)[0]
    return face