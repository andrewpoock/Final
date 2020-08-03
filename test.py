import unittest
import final_project
from string import ascii_uppercase

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.test = final_project.Hangman().reset()

    def tearDown(self):
        del self.test

    def test_word(self):
        self.assertEqual(self.space_word, " ".join(self.word))

    def test_letter(self):
        self.assertTrue(letter in acsii_uppercase)

    def test_guesses(self):
        self.assertTrue(self.guesses > 0)


if __name__ == '__main__':
    unittest.main()
