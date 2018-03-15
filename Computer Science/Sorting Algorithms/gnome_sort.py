import unittest


def gnome_sort(list_to_sort):
    i, j = 1, 2
    size = len(list_to_sort)
    while i < size:
        # first item is smaller, no swaps needed
        if list_to_sort[i - 1] <= list_to_sort[i]:
            # increment indexes by 1
            i, j = j, j + 1
        else:
            list_to_sort[i - 1], list_to_sort[i] = list_to_sort[i], list_to_sort[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return list_to_sort


class Test_Sort(unittest.TestCase):

    def test_gnome_sort(self):
        test_list = [99, 15, 4, 23, 7, 14, 0, 92]
        print("original: {}".format(str(test_list)))
        expected = sorted(test_list)
        actual = gnome_sort(test_list)
        print("expected: {}".format(str(expected)))
        print("actual: {}".format(str(actual)))
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
