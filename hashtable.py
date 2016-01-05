class HashTable:
    def __init__(self, size=100):
        self._table = [None] * size

    @property
    def _size(self):
        return len(self._table)

    def _index(self, key):
        return self._hash(key) % self._size

    @staticmethod
    # http://stackoverflow.com/a/30758270/1433127
    # http://stackoverflow.com/a/2624210/1433127
    def _hash(string):
        seed = 7
        modifier = 31
        hash_val = seed
        for c in string:
            hash_val = hash_val * modifier + ord(c)
        return hash_val

class Bucket:
    def __init__(self):
        self._vals = []

    def __getitem__(self, search_key):
        for key, val in self._vals:
            if key == search_key:
                return val
        raise KeyError

    def __setitem__(self, search_key, val):
        entry = (search_key, val)

        for i, (key, val) in enumerate(self._vals):
            if key == search_key:
                self._vals[i] = entry
                return

        self._vals.append(entry)

    def __delitem__(self, search_key):
        for i, (key, val) in enumerate(self._vals):
            if key == search_key:
                del self._vals[i]
                return

        raise KeyError
