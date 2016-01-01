import unittest
import quicksort as qs
from random import shuffle

class TestQuickSort(unittest.TestCase):
    def test_sort_len_small(self):
        A = []
        qs.sort(A)
        self.assertEqual(A, [])

        A = [1]
        qs.sort(A)
        self.assertEqual(A, [1])

        A = [2, 1]
        qs.sort(A, 0, 0)
        self.assertEqual(A, [2, 1])

        A = [2, 1]
        qs.sort(A, 0, 1)
        self.assertEqual(A, [2, 1])

    def test_sort_no_change(self):
        A = [1, 2]
        qs.sort(A)
        self.assertEqual(A, [1, 2])

        A = [1, 2, 3]
        qs.sort(A)
        self.assertEqual(A, [1, 2, 3])

        A = [1, 2, 3, 4, 5]
        qs.sort(A)
        self.assertEqual(A, [1, 2, 3, 4, 5])

        A = [1, 2, 3, 4, 5, 6, 7, 8]
        qs.sort(A)
        self.assertEqual(A, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_opposite(self):
        A = [2, 1]
        qs.sort(A)
        self.assertEqual(A, [1, 2])

        A = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]
        qs.sort(A)
        self.assertEqual(A, [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])

    def test_sort_partial(self):
        A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        qs.sort(A, 1, 3)
        self.assertEqual(A, [10, 7, 8, 9, 6, 5, 4, 3, 2, 1])

        A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        qs.sort(A, 8, 2)
        self.assertEqual(A, [10, 9, 8, 7, 6, 5, 4, 3, 1, 2])

        A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        qs.sort(A, 5, 5)
        self.assertEqual(A, [10, 9, 8, 7, 6, 1, 2, 3, 4, 5])

    def test_z_breaking_1(self):
        A = [1, 3, 2]
        qs.sort(A)
        self.assertEqual(A, [1, 2, 3])

        A = [0, 1, 3, 2, 4]
        qs.sort(A, 1, 3)
        self.assertEqual(A, list(range(5)))

        A = [0, 4, 1, 3, 2]
        qs.sort(A)
        self.assertEqual(A, list(range(5)))

    def test_sort_random(self):
        for _ in range(100):
            A = list(range(5))
            shuffle(A)
            qs.sort(A)
            self.assertEqual(A, list(range(5)))

        A = list(range(10))
        shuffle(A)
        qs.sort(A)
        self.assertEqual(A, list(range(10)))

        A = list(range(20))
        shuffle(A)
        qs.sort(A)
        self.assertEqual(A, list(range(20)))

        A = list(range(1000))
        shuffle(A)
        qs.sort(A)
        self.assertEqual(A, list(range(1000)))
        
    def test_swap(self):
        A = [10, 4, 5]
        qs.swap(A, 0, 0)
        self.assertEqual(A, [10, 4, 5])
        qs.swap(A, 1, 1)
        self.assertEqual(A, [10, 4, 5])
        qs.swap(A, 0, 1)
        self.assertEqual(A, [4, 10, 5])
        qs.swap(A, 0, 1)
        self.assertEqual(A, [10, 4, 5])
        qs.swap(A, 1, 0)
        self.assertEqual(A, [4, 10, 5])
        qs.swap(A, 1, 2)
        self.assertEqual(A, [4, 5, 10])
