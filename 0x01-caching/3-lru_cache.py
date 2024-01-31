#!/usr/bin/env python3
"""
A class LRUCache that inherits from BaseCaching and is a caching system.
"""

from collections import OrderedDict

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class.
    """

    def __init__(self):
        """
        Initialize the LRUCache object.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add or update an item in the cache.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first = self.cache_data.popitem(last=False)[0]
                print("DISCARD: {}".format(first))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

    def get(self, key):
        """
        Retrieve an item from the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data[key]
        self.cache_data.move_to_end(key)
        return value
