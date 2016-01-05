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
