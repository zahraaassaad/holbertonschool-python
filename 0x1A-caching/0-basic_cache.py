#!/usr/bin/python3
""" BasicCache module"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """caching system."""
    
    def put(self, key, item):
        """put item for key."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data."""
        if key is None or key not in self.cache_data.keys():
            return
        return self.cache_data.get(key)
