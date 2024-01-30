#!/usr/bin/python3

""" FIFO caching """

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """FIFO cache class"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first = list(self.cache_data.keys())[0]
                print("DISCARD: {}".format(first))
                self.cache_data.pop(first)
            self.cache_data[key] = item

    def get(self, key):
        """Get an item in the cache"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
