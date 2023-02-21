import unittest
from translator import english_to_french, french_to_english

class Testenglish_to_french1(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french("Hello, it is a pleasure to speak with you"), "Bonjour, c'est un plaisir de parler avec vous")

class Testenglish_to_french2(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french("Let's learn together"), "Allons apprendre ensemble")

class Testfrench_to_english1(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour, c'est un plaisir de parler avec vous"), "Hello, it is a pleasure to speak with you")

class Testfrench_to_english2(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english("Allons apprendre ensemble"), "Let's learn together")

class Testenglish_to_french3(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french(None), None)

class Testfrench_to_english3(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english(None), None)

class Testenglish_to_french4(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

class Testfrench_to_english4(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

if __name__ == '__main__':
    unittest.main()