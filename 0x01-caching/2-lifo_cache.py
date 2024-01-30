#!/usr/bin/python3

""" FIFO caching """

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()

    def put(self, key, item):
        """put an item"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last = list(self.cache_data.keys())[-1]
                print("DISCARD: {}".format(last))
                self.cache_data.pop(last)
            self.cache_data[key] = item

    def get(self, key):
        """get the item"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
