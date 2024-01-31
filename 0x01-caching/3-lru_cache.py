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
        """put an item"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first = self.cache_data.popitem(last=False)[0]
                print("DISCARD: {}".format(first))

            if key in self.cache_data:
                self.cache_data.pop(key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

    def get(self, key):
        """get item"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
