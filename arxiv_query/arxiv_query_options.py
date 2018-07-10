from typing import NewType


SortBy = NewType('SortBy', str)
SortOrder = NewType('SortOrder', str)


sort_by = {
    "relevance": SortBy("relevance"),
    "lastUpdatedDate": SortBy("lastUpdatedDate"),
    "submittedDate": SortBy("submittedDate")
}


sort_order = {
    "ascending": SortOrder("ascending"),
    "descending": SortOrder("descending")
}
