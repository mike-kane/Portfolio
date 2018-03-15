import unittest


def heap_sort(list_to_sort):
    pass


class Test_Sort(unittest.TestCase):

    def test_heap_sort(self):
        test_list = [99, 15, 4, 23, 7, 14, 0, 92]
        print("original: {}".format(str(test_list)))
        expected = sorted(test_list)
        actual = heap_sort(test_list)
        print("expected: {}".format(str(expected)))
        print("actual: {}".format(str(actual)))
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
