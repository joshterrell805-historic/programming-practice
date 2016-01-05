class HashTable:
    @staticmethod
    # http://stackoverflow.com/a/30758270/1433127
    # http://stackoverflow.com/a/2624210/1433127
    def hash(string):
        seed = 7
        modifier = 31
        hash_val = seed
        for c in string:
            hash_val = hash_val * modifier + ord(c)
        return hash_val
