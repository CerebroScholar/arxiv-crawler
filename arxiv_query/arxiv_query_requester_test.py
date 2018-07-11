import unittest
from .arxiv_query_requester import *
from .arxiv_query_options import *
from arxiv_classification import arxiv_classification


class QueryRequesterTest(unittest.TestCase):
    def setUp(self):
        self.url = generate_query_url(QueryData(
            "machine learning",
            [arxiv_classification["computer_science"], arxiv_classification["statistics"]],
            sort_by["submittedDate"],
            sort_order["ascending"],
            start=0,
            max_results=100
        ))

    def test_generate_query_url(self):
        self.assertEqual(
            "http://export.arxiv.org/api/query?"
            "search_query=all:%22machine+learning%22+AND+%28cat:cs+OR+cat:stat%29&"
            "sortBy=submittedDate&"
            "sortOrder=ascending&"
            "start=0&"
            "max_results=100",
            self.url
        )

if __name__ == "__main__":
    unittest.main()
