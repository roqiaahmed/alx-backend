#!/usr/bin/env python3

""" Simple helper function """


def index_range(page, page_size) -> tuple:
    """return a tuple of size two containing"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
