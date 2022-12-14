from typing import Union, List, Dict
# from functools import lru_cache
from src.insights.jobs import read
import csv

# @lru_cache
# def read(path: str) -> List[Dict]:
#     with open(path, encoding='utf8') as archive:
#         data = csv.DictReader(archive, delimiter=',', quotechar='"')
#         return list(data)

def get_max_salary(path: str) -> int:
    raise NotImplementedError


def get_min_salary(path: str) -> int:
    get_salaries = read(path)
    return min([
        int(salaries["min_salary"])
        for salaries in get_salaries
        if (salaries["min_salary"]).isdigit()])


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    raise NotImplementedError
