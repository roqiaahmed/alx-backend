#!/usr/bin/env python3

"""
A class LFUCache that inherits from BaseCaching and is a caching system.
"""

BaseCaching = __import__("base_caching").BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """
    LRUCache class.
    """

    def __init__(self):
        """
        Initialize the LRUCache object.
        """
        super().__init__()
        self.frequency = defaultdict(int)

    def put(self, key, item):
        """
        Add or update an item in the cache.
        """
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
        """
        Retrieve an item from the cache.
        """
        if key in self.cache_data:
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
