import unittest
import arxiv_classification


class ArxivClassificationTest(unittest.TestCase):
    def test_computer_science(self):
        self.assertEqual(arxiv_classification.computer_science(), 'classification-computer_science')

    def test_statistics(self):
        self.assertEqual(arxiv_classification.statistics(), 'classification-statistics')

if __name__ == '__main__':
    unittest.main()
