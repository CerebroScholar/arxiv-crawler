import unittest
from datetime import date

import arxiv_classification
from arxiv_search import arxiv_search_url


class ArxivUrlTest(unittest.TestCase):
    def test_get_keyword_param(self):
        keyword = 'machine learning'
        self.assertEqual(arxiv_search_url.get_keyword_param(keyword), 'terms-0-term=machine+learning&terms-0-field=all')

    def test_get_classification_param(self):
        self.assertEqual(arxiv_search_url.get_classification_param(arxiv_classification.computer_science()), 'classification-computer_science=y')
        self.assertEqual(arxiv_search_url.get_classification_param(arxiv_classification.statistics()), 'classification-statistics=y')

    def test_get_date_range_param(self):
        start = date(2018, 6, 8)
        end = date(2018, 7, 8)
        self.assertEqual(arxiv_search_url.get_date_range_param(start, end), 'date-from_date=2018-06-08&date-to_date=2018-07-08')

    def test_get_size_param(self):
        size = 50
        self.assertEqual(arxiv_search_url.get_size_param(size), 'size=50')
        size += 1
        self.assertEqual(arxiv_search_url.get_size_param(size), 'size=51')

    def test_get_order_param(self):
        order = "announced_date_first"
        self.assertEqual(arxiv_search_url.get_order_param(order=order), 'order=-announced_date_first')

    def test_get_filter_by_param(self):
        filter_by = "date_range"
        self.assertEqual(arxiv_search_url.get_date_filter_by_param(filter_by=filter_by), 'date-filter_by=date_range')

    def test_get_url(self):
        keyword = "machine learning"
        start = date(2018, 6, 8)
        end = date(2018, 7, 8)
        url = arxiv_search_url.get_url(keyword=keyword, classification=[arxiv_classification.computer_science(), arxiv_classification.statistics()], start=start, end=end, size=50, order='announced_date_first')
        self.assertEqual(url, 'https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term=machine+learning&terms-0-field=all&classification-computer_science=y&classification-statistics=y&date-from_date=2018-06-08&date-to_date=2018-07-08&size=50&order=-announced_date_first')

if __name__ == '__main__':
    unittest.main()
