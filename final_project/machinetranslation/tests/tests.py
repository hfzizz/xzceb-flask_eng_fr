import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french1(self):
        #test for null
        self.assertNotEqual(english_to_french("None"),'')
    def test_english_to_french2(self):
        #Test for the translation of the word ‘Hello’ and ‘Bonjour’
        self.assertEqual(english_to_french('Hello'),'Bonjour')

    def test_french_to_english1(self):
        #test for null
        self.assertNotEqual(french_to_english("None"),'')
    def test_french_to_english2(self):
        #Test for the translation of the word ‘Bonjour’ and ‘Hello’.
        self.assertEqual(french_to_english('Bonjour'),'Hello')

if __name__ == "__main__":
    unittest.main()