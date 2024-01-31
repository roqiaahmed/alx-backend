#!/usr/bin/env python3

"""mru cache"""
from collections import OrderedDict

BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """put an item"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                recent_key = self.cache_data.popitem()[0]
                print("DISCARD: {}".format(recent_key))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """get the item"""
        if key in self.cache_data:
            val = self.cache_data[key]
            self.cache_data.move_to_end(key, last=True)
            return val
