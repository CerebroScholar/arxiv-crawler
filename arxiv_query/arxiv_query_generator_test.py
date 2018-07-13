import unittest
from arxiv_classification import get_computer_science_category_list, get_statistics_category_list
from .arxiv_query_data import QueryData
from .arxiv_query_options import sort_by, sort_order
from .arxiv_query_generator import *


class QueryGeneratorTest(unittest.TestCase):
    def test_generate_query_element(self):
        key = "key"
        value = "value"
        query_element = generate_query_element(key, value)
        self.assertEqual("key=value", query_element)

    def test_generate_search_query_element(self):
        key = "key"
        value = "value"
        search_query_element = generate_search_query_element(key, value)
        self.assertEqual("key:value", search_query_element)

    def test_generate_group_query(self):
        query = "abc"
        group_query = generate_group_query(query)
        self.assertEqual("%28abc%29", group_query)

    def test_generate_and_query(self):
        search_query_element1 = generate_search_query_element("key1", "value1")
        search_query_element2 = generate_search_query_element("key2", "value2")
        and_query = generate_and_query(search_query_element1, search_query_element2)
        self.assertEqual("key1:value1+AND+key2:value2", and_query)

    def test_generate_or_query(self):
        search_query_element1 = generate_search_query_element("key1", "value1")
        search_query_element2 = generate_search_query_element("key2", "value2")
        or_query = generate_or_query(search_query_element1, search_query_element2)
        self.assertEqual("key1:value1+OR+key2:value2", or_query)

    def test_generate_all_keyword_query(self):
        keyword = "keyword"
        keyword_query = generate_all_keyword_query(keyword)
        self.assertEqual("all:%22keyword%22", keyword_query)
        keyword = "machine learning"
        keyword_query = generate_all_keyword_query(keyword)
        self.assertEqual("all:%22machine+learning%22", keyword_query)

    def test_generate_category_query(self):
        category = get_computer_science_category_list()[0]
        category_query = generate_category_query(category)
        self.assertEqual("cat:cs.AI", category_query)

    def test_generate_categories_query(self):
        categories = [get_computer_science_category_list()[0], get_statistics_category_list()[0]]
        categories_query = generate_categories_query(categories)
        self.assertEqual("%28cat:cs.AI+OR+cat:stat.AP%29", categories_query)

    def test_generate_search_query(self):
        keyword = "machine learning"
        categories = [get_computer_science_category_list()[0], get_statistics_category_list()[0]]
        search_query = generate_search_query(keyword, categories)
        self.assertEqual("search_query=all:%22machine+learning%22+AND+%28cat:cs.AI+OR+cat:stat.AP%29", search_query)

    def test_generate_query_string(self):
        query_data = QueryData(
            "machine learning",
            [get_computer_science_category_list()[0], get_statistics_category_list()[0]],
            sort_by["submittedDate"],
            sort_order["ascending"],
            start=0,
            max_results=100
        )
        query_string = generate_query_string(query_data)
        self.assertEqual(
            "search_query=all:%22machine+learning%22+AND+%28cat:cs.AI+OR+cat:stat.AP%29&"
            "sortBy=submittedDate&"
            "sortOrder=ascending&"
            "start=0&"
            "max_results=100",
            query_string
        )


if __name__ == "__main__":
    unittest.main()
