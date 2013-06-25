"""Test entity extraction with NLTK.

   (C) 2013 Dalek Labs
"""
import unittest

from app.process.entities import EntityExtractor


class TestExtraction(unittest.TestCase):
    def test_extraction(self):
        extractor = EntityExtractor()
        test_sentence = u'Rich Burdon and Jeff Reynar are building Dalek.'
        entities = extractor.extract_named_entities(test_sentence)
        self.assertTrue('Dalek' in entities)
        self.assertTrue('Jeff Reynar' in entities)
        self.assertTrue('Rich Burdon' in entities)

if __name__ == '__main__':
    unittest.main()
