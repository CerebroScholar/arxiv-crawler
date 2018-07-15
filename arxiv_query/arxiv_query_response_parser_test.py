import pprint
from .arxiv_query_response_parser import *
from .arxiv_query_requester import request_query
from .arxiv_query_data import QueryData
from .arxiv_query_options import sort_by, sort_order
from arxiv_classification import get_computer_science_category_list, get_statistics_category_list


def test_parse_query_response():
    query_data = QueryData(
        'machine learning',
        [*get_computer_science_category_list(), *get_statistics_category_list()],
        sort_by['submittedDate'],
        sort_order['ascending'],
        0,
        10
    )
    pprint.pprint(parse_query_response(request_query(query_data)))
