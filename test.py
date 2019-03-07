import unittest
import arabicnlp


class IntegrationTest(unittest.TestCase):
    """Integration test for package interface"""

    testtext = ""


    def test_tokens(self):
        self.assertTrue(arabicnlp.tokens(self.testtext))

    def test_lemmas(self):
        self.assertTrue(arabicnlp.lemmas(self.testtext))

    def test_tags(self):
        self.assertTrue(arabicnlp.tags(self.testtext))

    def test_spelling(self):
        self.assertTrue(arabicnlp.correct(self.testtext))

    def test_sentiment(self):
        self.assertTrue(arabicnlp.sentiment(self.testtext))

    def test_similarity(self):
        self.assertTrue(arabicnlp.similarity(self.testtext, self.testtext))


class UnitTest(unittest.TestCase):
    """Unit test here"""
    pass


if __name__ == '__main__':
    unittest.main()