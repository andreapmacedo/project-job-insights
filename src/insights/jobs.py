from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding='utf8') as archive:
        data = csv.DictReader(archive, delimiter=',', quotechar='"')
        return list(data)


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    unique_jobs = set()
    for job in data:
        unique_jobs.add(job['job_type'])
    return list(unique_jobs)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filtered_by_job_type = [job for job in jobs if job["job_type"] == job_type]
    return filtered_by_job_type
