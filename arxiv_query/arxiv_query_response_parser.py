import feedparser
from .arxiv_query_requester import RawQueryResponse


def parse_query_response(raw_query_response: RawQueryResponse):
    return feedparser.parse(raw_query_response)


