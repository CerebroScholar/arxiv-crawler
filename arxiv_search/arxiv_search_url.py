from datetime import date


BASE_URL = "https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND"


# no operator options yet
def get_keyword_param(keyword: str):
    return "&".join(["=".join(["terms-0-term", "+".join(keyword.split(" "))]), "terms-0-field=all"])


# This function should called with arxiv_classification functinos
def get_classification_param(classification: str):
    return classification + "=y"


# Example) start: 2018-06-08, end: 2018-07-08
def get_date_range_param(start: date, end: date):
    start = "=".join(["date-from_date", start.isoformat()])
    end = "=".join(["date-to_date", end.isoformat()]) # ("date-from-date=".join(start, "="))
    return "&".join([start, end])
    

def get_size_param(size: int):
    return "=".join(["size", str(size)])


# Example) announced_date_first
def get_order_param(order: str):
    return "=-".join(["order", order])


# Example) date_range
def get_date_filter_by_param(filter_by: str):
    return "=".join(["date-filter_by", filter_by])


def get_url(keyword: str, classification: list, start, end, size, order):
    classification = [get_classification_param(c) for c in classification]
    return "&".join([BASE_URL, get_keyword_param(keyword), *classification, get_date_range_param(start, end), get_size_param(size), get_order_param(order)])

