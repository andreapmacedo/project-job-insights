from typing import Union, List, Dict
# from functools import lru_cache
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    get_salaries = read(path)
    max_salary = max([
        int(salaries["max_salary"])
        for salaries in get_salaries
        if (salaries["max_salary"]).isdigit()])
    return max_salary


def get_min_salary(path: str) -> int:
    get_salaries = read(path)
    min_salary = min([
        int(salaries["min_salary"])
        for salaries in get_salaries
        if (salaries["min_salary"]).isdigit()])
    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    raise NotImplementedError
