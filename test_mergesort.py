import unittest
import mergesort as ms
from random import shuffle

class TestMergeSort(unittest.TestCase):
    def test_sort_len_small(self):
        A = []
        ms.sort(A)
        self.assertEqual(A, [])

        A = [1]
        ms.sort(A)
        self.assertEqual(A, [1])

        A = [2, 1]
        ms.sort(A)
        self.assertEqual(A, [1, 2])

    def test_sort_no_change(self):
        A = [1, 2]
        ms.sort(A)
        self.assertEqual(A, [1, 2])

        A = [1, 2, 3]
        ms.sort(A)
        self.assertEqual(A, [1, 2, 3])

        A = [1, 2, 3, 4, 5]
        ms.sort(A)
        self.assertEqual(A, [1, 2, 3, 4, 5])

        A = [1, 2, 3, 4, 5, 6, 7, 8]
        ms.sort(A)
        self.assertEqual(A, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_opposite(self):
        A = [2, 1]
        ms.sort(A)
        self.assertEqual(A, [1, 2])

        A = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]
        ms.sort(A)
        self.assertEqual(A, [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])

    def test_z_breaking_1(self):
        A = [1, 3, 2]
        ms.sort(A)
        self.assertEqual(A, [1, 2, 3])

        A = [0, 1, 3, 2, 4]
        ms.sort(A)
        self.assertEqual(A, list(range(5)))

        A = [0, 4, 1, 3, 2]
        ms.sort(A)
        self.assertEqual(A, list(range(5)))

    def test_sort_random(self):
        for _ in range(100):
            A = list(range(5))
            shuffle(A)
            ms.sort(A)
            self.assertEqual(A, list(range(5)))

        A = list(range(10))
        shuffle(A)
        ms.sort(A)
        self.assertEqual(A, list(range(10)))

        A = list(range(20))
        shuffle(A)
        ms.sort(A)
        self.assertEqual(A, list(range(20)))

        A = list(range(1000))
        shuffle(A)
        ms.sort(A)
        self.assertEqual(A, list(range(1000)))
