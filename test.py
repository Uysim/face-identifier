import unittest
import cv2
from face_identifier import is_faces_matched

class TestFaceMatching(unittest.TestCase):
    def test_same_faces_matching(self):
        image1 = cv2.imread('images/Angelina Jolie/001_fe3347c0.jpg')
        image2 = cv2.imread('images/Angelina Jolie/002_8f8da10e.jpg')
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
        image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
        self.assertTrue(is_faces_matched(image1, image2))

        image1 = cv2.imread('images/Brid Pitt/001_c04300ef.jpg')
        image2 = cv2.imread('images/Brid Pitt/002_cc1b9701.jpg')
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
        image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
        self.assertTrue(is_faces_matched(image1, image2))


    def test_different_faces_matching(self):
        image1 = cv2.imread('images/Angelina Jolie/001_fe3347c0.jpg')
        image2 = cv2.imread('images/Brid Pitt/001_c04300ef.jpg')
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
        image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
        self.assertFalse(is_faces_matched(image1, image2))

        image1 = cv2.imread('images/Angelina Jolie/002_8f8da10e.jpg')
        image2 = cv2.imread('images/Brid Pitt/002_cc1b9701.jpg')
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
        image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
        self.assertFalse(is_faces_matched(image1, image2))

if __name__ == '__main__':
    unittest.main()