import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("I am glad this happened")
        self.assertIn("joy", result)

    def test_anger(self):
        result = emotion_detector("I am really mad about this")
        self.assertIn("anger", result)

    def test_disgust(self):
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertIn("disgust", result)

    def test_sadness(self):
        result = emotion_detector("I am so sad about this")
        self.assertIn("sadness", result)

    def test_fear(self):
        result = emotion_detector("I am really afraid that this will happen")
        self.assertIn("fear", result)

if __name__ == '__main__':
    unittest.main()
