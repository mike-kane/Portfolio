import unittest


def insertion_sort(list_to_sort):
    pass


class Test_Sort(unittest.TestCase):

    def test_insertion_sort(self):
        test_list = [99, 15, 4, 23, 7, 14, 0, 92]
        print("original: {}".format(str(test_list)))
        expected = sorted(test_list)
        actual = insertion_sort(test_list)
        print("expected: {}".format(str(expected)))
        print("actual: {}".format(str(actual)))
        self.assertEqual(expected, actual)
