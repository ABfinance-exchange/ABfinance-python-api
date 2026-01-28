from enum import Enum


class ApiLimit(str, Enum):
    QUERY = "/v5/apilimit/query"
    QUERY_ALL = "/v5/apilimit/query-all"
    QUERY_CAP = "/v5/apilimit/query-cap"
    SET = "/v5/apilimit/set"

    def __str__(self) -> str:
        return self.value
