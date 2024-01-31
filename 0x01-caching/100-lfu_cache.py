#!/usr/bin/env python3

""" LFU caching """

BaseCaching = __import__("base_caching").BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """LFU class"""

    def __init__(self):
        super().__init__()
        self.frequency = defaultdict(int)

    def put(self, key, item):
        """put an item"""
        if key is not None and item is not None:
            if (
                len(self.cache_data) >= BaseCaching.MAX_ITEMS
                and key not in self.cache_data
            ):
                evict_key = min(self.frequency, key=self.frequency.get)
                self.cache_data.pop(evict_key)
                self.frequency.pop(evict_key)
                print("DISCARD: {}".format(evict_key))
            self.cache_data[key] = item
            self.frequency[key] += 1

    def get(self, key):
        "get the item"
        if key in self.cache_data:
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
