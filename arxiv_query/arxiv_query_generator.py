from typing import NewType
from arxiv_classification import Classification
from .arxiv_query_data import QueryData, CategoryList


QueryElement = NewType('QueryElement', str)
SearchQueryElement = NewType('SearchQueryElement', str)
GroupQuery = NewType('GroupQuery', SearchQueryElement)
AndQuery = NewType('AndQuery', SearchQueryElement)
OrQuery = NewType('OrQuery', SearchQueryElement)
KeywordQuery = NewType('KeywordQuery', SearchQueryElement)
CategoryQuery = NewType('CategoryQuery', SearchQueryElement)
CategoriesQuery = NewType('CategoriesQuery', OrQuery)
SearchQuery = NewType('SearchQuery', QueryElement)
QueryString = NewType('QueryString', str)


def generate_query_element(key: str, value: str) -> QueryElement:
    return key + '=' + value


def generate_search_query_element(key: str, value: str) -> SearchQueryElement:
    return key + ':' + value


def generate_group_query(query: SearchQueryElement) -> GroupQuery:
    return '%28' + query + '%29'


def generate_and_query(query1: SearchQueryElement, query2: SearchQueryElement) -> AndQuery:
    return query1 + '+AND+' + query2


def generate_or_query(query1: SearchQueryElement, query2: SearchQueryElement) -> OrQuery:
    return query1 + '+OR+' + query2


def generate_all_keyword_query(keyword: str) -> KeywordQuery:
    return generate_search_query_element('all', '%22' + '+'.join(keyword.split(' ')) + '%22')


def generate_category_query(category: Classification) -> CategoryQuery:
    return generate_search_query_element('cat', category)


def generate_categories_query(categories: CategoryList) -> CategoriesQuery:
    category_search_query_elements = []
    for category in categories:
        category_search_query_elements.append(generate_category_query(category))
    categories_query = category_search_query_elements[0]
    for category_search_query_element in category_search_query_elements[1:]:
        categories_query = generate_or_query(categories_query, category_search_query_element)
    return generate_group_query(categories_query)


def generate_search_query(keyword: str, categories: CategoryList) -> QueryElement:
    keyword_query = generate_all_keyword_query(keyword)
    categories_query = generate_categories_query(categories)
    return 'search_query=' + generate_and_query(keyword_query, categories_query)


def generate_query_string(query_data: QueryData) -> QueryString:
    search_query = generate_search_query(query_data.keyword, query_data.categories)
    sort_by_query = generate_query_element('sortBy', query_data.sort_by)
    sort_order_query = generate_query_element('sortOrder', query_data.sort_order)
    start_query = generate_query_element('start', str(query_data.start))
    max_results_query = generate_query_element('max_results', str(query_data.max_results))
    return '&'.join([search_query, sort_by_query, sort_order_query, start_query, max_results_query])
