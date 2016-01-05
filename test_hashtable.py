from hashtable import HashTable
import unittest
import random

class TestHashTable(unittest.TestCase):
    def test_hash(self):
        s = 7
        m = 31
        self.assertEqual(HashTable._hash(''), s)
        self.assertEqual(HashTable._hash('a'), s*m + ord('a'))
        self.assertEqual(HashTable._hash('hi'), (s*m + ord('h'))*m + ord('i'))

    def test_size(self):
        self.assertEqual(HashTable(50)._size, 50)
        self.assertEqual(HashTable(7)._size, 7)
        self.assertEqual(HashTable()._size, 100)

    def test_index(self):
        size = 7
        table = HashTable(size)
        used = [0] * size
        max_iter = 10 ** 3
        i = 0

        def all_used():
            return all(x > 0 for x in used)

        def rand_char():
            return chr(random.randint(ord('a'), ord('z')))

        def rand_string():
            length = random.randint(0, 10)
            return ''.join(rand_char() for _ in range(length))

        # make sure all indexes get used
        while i < max_iter and not all_used():
            key = rand_string()
            index = table._index(key)
            self.assertTrue(index >= 0 and index < size)
            used[index] += 1
            i += 1

        self.assertTrue(all_used())

        # make sure all indexes about equal usage
        while i < max_iter:
            key = rand_string()
            used[table._index(key)] += 1
            i += 1

        try:
            # min and max are no more than 4x apart
            self.assertTrue(max(used) < 4 * min(used))
        except Exception as e:
            print(used)
            raise e
