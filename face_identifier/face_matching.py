from face_identifier.face_detection import detect_face
from face_identifier.face_extraction import extract_image_box
from face_identifier.face_vector_embedding import predict_features
from face_identifier.face_comparation import is_features_matched
import cv2

def is_faces_matched(image1, image2):
    face1 = detect_face(image1)
    face2 = detect_face(image2)
    box1 = face1['box']
    box2 = face2['box']
    face_img1 = extract_image_box(image1, box1)
    face_img2 = extract_image_box(image2, box2)
    face_img1 = cv2.resize(face_img1, (224, 224))
    face_img2 = cv2.resize(face_img2, (224, 224))
    features1 = predict_features(face_img1)
    features2 = predict_features(face_img2)
    return is_features_matched(features1, features2)