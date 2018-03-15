import unittest


def insertion_sort(list_to_sort):
    # iterate through list starting at index 1 and ending at len(list)
    for i in range(1, len(list_to_sort)):
        # grab the item that was stored at index i
        temp_var = list_to_sort[i]
        # keep track of the index so that it can be manipulated later
        index = i
    # while not at start of list AND item stored is smaller than item before it,
    # move each item by -1.
        while index > 0 and temp_var < list_to_sort[index - 1]:
            list_to_sort[index] = list_to_sort[index - 1]
            index -= 1
        # insert item in spot opened by moving all items back one.
        list_to_sort[index] = temp_var

    return list_to_sort


class Test_Sort(unittest.TestCase):

    def test_insertion_sort(self):
        test_list = [99, 15, 4, 23, 7, 14, 0, 92]
        print("original: {}".format(str(test_list)))
        expected = sorted(test_list)
        actual = insertion_sort(test_list)
        print("expected: {}".format(str(expected)))
        print("actual: {}".format(str(actual)))
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
