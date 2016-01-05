from hashtable import HashTable, Bucket
import unittest
import random

class TestHashTable(unittest.TestCase):
    # helpers
    def rand_char(self):
        return chr(random.randint(ord('a'), ord('z')))

    def rand_string(self):
        length = random.randint(0, 10)
        return ''.join(self.rand_char() for _ in range(length))

    # tests
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

        # make sure all indexes get used
        while i < max_iter and not all_used():
            key = self.rand_string()
            index = table._index(key)
            self.assertTrue(index >= 0 and index < size)
            used[index] += 1
            i += 1

        self.assertTrue(all_used())

        # make sure all indexes about equal usage
        while i < max_iter:
            key = self.rand_string()
            used[table._index(key)] += 1
            i += 1

        try:
            # min and max are no more than 4x apart
            self.assertTrue(max(used) < 4 * min(used))
        except Exception as e:
            print(used)
            raise e

    def test_get_set_del(self):
        t = HashTable(2)
        t._table = [GetSetDelSpy() for _ in range(2)]
        t._index = lambda x: int(x / 31) - 1

        _ = t[31]
        self.assertEqual(t._table[0].actions, [('g', 31)])
        self.assertEqual(t._table[1].actions, [])

        _ = t[62]
        self.assertEqual(t._table[0].actions, [('g', 31)])
        self.assertEqual(t._table[1].actions, [('g', 62)])

        del t[31]
        self.assertEqual(t._table[0].actions, [('g', 31), ('d', 31)])
        self.assertEqual(t._table[1].actions, [('g', 62)])

        t[62] = 4
        self.assertEqual(t._table[0].actions, [('g', 31), ('d', 31)])
        self.assertEqual(t._table[1].actions, [('g', 62), ('s', 62, 4)])

    def test_store_stuff(self):
        b = Bucket()
        b['a'] = 4
        b['9'] = 7
        b[12] = None
        b[3] = 'asdf'

        self.assertEqual(b['a'], 4)
        self.assertEqual(b['9'], 7)
        self.assertEqual(b[3], 'asdf')
        self.assertEqual(b[12], None)

        thrown = False
        try:
            b['f']
        except KeyError as e:
            thrown = True
        self.assertTrue(thrown)

        b['f'] = 123092
        self.assertEqual(b['f'], 123092)

        del b[12]
        thrown = False
        try:
            b[12]
        except KeyError as e:
            thrown = True
        self.assertTrue(thrown)

        for _ in range(100):
            key, val = self.rand_string(), random.randint(-7777, 77777)
            b[key] = val
            self.assertEqual(b[key], val)


class GetSetDelSpy:
    def __init__(self):
        self.actions = []
    def __getitem__(self, key):
        self.actions.append(('g', key))
    def __setitem__(self, key, val):
        self.actions.append(('s', key, val))
    def __delitem__(self, key):
        self.actions.append(('d', key))

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
