from hashtable import HashTable
import unittest

class TestHashTable(unittest.TestCase):
    def test_hash(self):
        s = 7
        m = 31
        self.assertEqual(HashTable.hash(''), s)
        self.assertEqual(HashTable.hash('a'), s*m + ord('a'))
        self.assertEqual(HashTable.hash('hi'), (s*m + ord('h'))*m + ord('i'))

    def test_size(self):
        self.assertEqual(HashTable(50)._size, 50)
        self.assertEqual(HashTable(7)._size, 7)
        self.assertEqual(HashTable()._size, 100)
