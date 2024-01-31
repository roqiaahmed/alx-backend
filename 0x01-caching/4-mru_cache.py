#!/usr/bin/env python3
"""
A class MRUCache that inherits from BaseCaching and is a caching system.
"""

from collections import OrderedDict

BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class.
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
                recent_key = self.cache_data.popitem()[0]
                print("DISCARD: {}".format(recent_key))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """
        Retrieve an item from the cache.
        """
        if key in self.cache_data:
            val = self.cache_data[key]
            self.cache_data.move_to_end(key, last=True)
            return val
