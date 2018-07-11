from typing import List
from arxiv_classification import Classification
from .arxiv_query_options import SortBy, SortOrder


CategoryList = List[Classification]


class QueryData:
    def __init__(self, keyword: str, categories: CategoryList, sort_by: SortBy, sort_order: SortOrder, start: int, max_results: int):
        self.keyword = keyword
        self.categories = categories
        self.sort_by = sort_by
        self.sort_order = sort_order
        self.start = start
        self.max_results = max_results

    def go_to_next_query(self):
        self.start += self.max_results
