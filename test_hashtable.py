from hashtable import HashTable, Bucket
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

class TestBucket(unittest.TestCase):
    def test_get_bad_key(self):
        b = Bucket()

        thrown = False
        try:
            b['']
        except KeyError as e:
            thrown = True
        self.assertTrue(thrown)

        b._vals = [('b', 1)]
        thrown = False
        try:
            b['a']
        except KeyError as e:
            thrown = True
        self.assertTrue(thrown)

    def test_get_good_key(self):
        b = Bucket()
        b._vals = [('a', 12), ('x', 'asdf'), (4, False), (-1, True)]

        self.assertEqual(b['a'], 12)
        self.assertEqual(b[-1], True)
        self.assertEqual(b[4], False)
        self.assertEqual(b['x'], 'asdf')

    def test_set_new(self):
        b = Bucket()
        self.assertEqual(b._vals, [])
        b['z'] = 4
        self.assertEqual(b._vals, [('z', 4)])
        b[4] = 38
        self.assertEqual(b._vals, [('z',4),(4,38)])
        b[12] = '17'
        self.assertEqual(b._vals, [('z', 4), (4, 38), (12, '17')])

    def test_set_overwrite(self):
        b = Bucket()
        b._vals = [('z', 4), (4, 38), (12, '17')]
        b[4] = 'z'
        self.assertEqual(b._vals, [('z', 4), (4, 'z'), (12, '17')])
        b['z'] = 1009
        self.assertEqual(b._vals, [('z', 1009), (4, 'z'), (12, '17')])
        b[12] = False
        self.assertEqual(b._vals, [('z', 1009), (4, 'z'), (12, False)])

    def test_del(self):
        b = Bucket()
        b._vals = [('z', 4), (4, 38), (12, '17'), (18, 2)]
        del b[4]
        self.assertEqual(b._vals, [('z', 4), (12, '17'), (18, 2)])
        del b[18]
        self.assertEqual(b._vals, [('z', 4), (12, '17')])
        del b['z']
        self.assertEqual(b._vals, [(12, '17')])
        del b[12]
        self.assertEqual(b._vals, [])

    def test_del_non_exist(self):
        b = Bucket()
        b._vals = [('z', 4), (4, 38), (12, '17'), (18, 2)]

        thrown = False
        try:
            b['f']
        except KeyError as e:
            thrown = True
        self.assertTrue(thrown)

        b._vals = []
        thrown = False
        try:
            b[4]
        except KeyError as e:
            thrown = True
        self.assertTrue(thrown)
