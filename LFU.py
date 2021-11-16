# Implement an LFU (Least Frequently Used) cache.
# It should be able to be initialized with a cache size n, and contain the following methods:
# set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item
# should also remove the least frequently used item. If there is a tie, then the least recently used key should be removed.
# get(key): gets the value at key. If no such key exists, return null.
# Each operation should run in O(1) time.
from collections import defaultdict, OrderedDict


class LFUCache(object):
    def __init__(self, capacity):
        self.remain = capacity
        self.least_freq = 1
        self.node_for_freq = defaultdict(OrderedDict)
        self.node_for_key = dict()

    def set_cache(self, key, value):
        if key in self.node_for_key:
            self._update(key, value)
        else:
            self.node_for_key[key] = (value, 1)
            self.node_for_freq[1][key] = (value, 1)
            if self.remain == 0:
                removed = self.node_for_freq[self.least_freq].popitem(last=False)
                self.node_for_key.pop(removed[0])
            else:
                self.remain -= 1
            self.least_freq = 1

    def _update(self, key, value):
        _, freq = self.node_for_key[key]
        self.node_for_freq[freq].pop(key)
        if len(self.node_for_freq[self.least_freq]) == 0:
            self.least_freq += 1
        self.node_for_freq[freq + 1][key] = (value, freq + 1)
        self.node_for_key[key] = (value, freq + 1)

    def get_cache(self, key):
        if key not in self.node_for_key:
            return -1
        value = self.node_for_key.get(key)[0]
        self._update(key, value)
        return value


if __name__ == '__main__':
    cache = LFUCache(2)
    cache.set_cache(1, 1)
    print("******************")
    print(cache.node_for_key)
    cache.set_cache(2, 2)
    print("******************")
    print(cache.node_for_key)
    cache.set_cache(2, 3)
    print(cache.get_cache(1))
    cache.set_cache(3, 3)
    print(cache.get_cache(2))
    cache.set_cache(4, 4)
    print(cache.get_cache(1))
    print(cache.get_cache(3))
    print(cache.get_cache(4))
