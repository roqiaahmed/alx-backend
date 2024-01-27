#!/usr/bin/env python3

""" Simple pagination """

import csv
import math
from typing import List


def index_range(page, page_size) -> tuple:
    """return a tuple of size two containing"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get page from dataset"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        range = index_range(page, page_size)
        if range[0] >= len(self.dataset()):
            return []
        return self.dataset()[range[0] : range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns a dictionary"""
        date = self.get_page(page, page_size)
        total_pages = (len(self.dataset()) + page_size - 1) // page_size
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        hyper = {
            "page_size": len(date),
            "page": page,
            "data": date,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
        return hyper
