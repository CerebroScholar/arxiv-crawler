import requests
from typing import NewType
from arxiv_query.arxiv_query_data import QueryData
from arxiv_query.arxiv_query_generator import generate_query_string


RawQueryResponse = NewType('QueryResponse', str)
BASE_URL = 'http://export.arxiv.org/api/query?'


def generate_query_url(query_data: QueryData) -> str:
    return BASE_URL + generate_query_string(query_data)


def request_query(query_data: QueryData) -> RawQueryResponse:
    return requests.get(generate_query_url(query_data)).text

