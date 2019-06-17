# Duplicate Allowed
import random
import collections

class RandomizedCollection(object):

    def __init__(self):
        self.vals, self.idxs = [], collections.defaultdict(set)

    def insert(self, val):
        self.vals.append(val)
        self.idxs[val].add(len(self.vals) - 1)
        return len(self.idxs[val]) == 1

    def remove(self, val):
        if not self.idxs[val]: return False

        i, last_val = self.idxs[val].pop(), self.vals[-1]
        self.vals[i] = last_val
        self.idxs[last_val].add(i)
        self.idxs[last_val].discard(len(self.vals) - 1)
        self.vals.pop()
        return True

    def getRandom(self):
        return random.choice(self.vals)
