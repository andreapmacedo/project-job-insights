from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    get_all_industries = read(path)
    industries = set()
    for industry in get_all_industries:
        if industry["industry"] != '':
            industries.add(industry["industry"])
    return industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered_by_industry = [job for job in jobs if job["industry"] == industry]
    return filtered_by_industry
