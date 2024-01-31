#!/usr/bin/python3

""" FIFO caching """
from collections import OrderedDict

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Put an item"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first = self.cache_data.popitem(last=False)[0]
                print("DISCARD: {}".format(first))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

    def get(self, key):
        """get item"""
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data[key]
        self.cache_data.move_to_end(key)
        return value
