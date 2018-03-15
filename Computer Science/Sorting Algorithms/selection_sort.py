import unittest


def selection_sort(list_to_sort):
    # iterate from back of list towards front of list
    for slot_to_fill in range(len(list_to_sort) - 1, 0, -1):
        index_of_max = 0
        # iterate from index 1 to slot being filled looking for max item
        # (we don't start at 0 since first item will always be largest item seen
        # during first iteration of loop)
        for item in range(1, slot_to_fill + 1):
            if list_to_sort[item] > list_to_sort[index_of_max]:
                index_of_max = item
        # store item at current position in slot to fill in temp variable so it
        # isnt garbage collected
        temp_var = list_to_sort[slot_to_fill]
        # switch positions of current item in slot and largest item found
        list_to_sort[slot_to_fill] = list_to_sort[index_of_max]
        list_to_sort[index_of_max] = temp_var

    return list_to_sort


class Test_Sort(unittest.TestCase):

    def test_selection_sort(self):
        test_list = [5, 15, 23, 1, 99, 443, 42, 7]
        print("original list: {}".format(str(test_list)))
        expected = sorted(test_list)
        actual = selection_sort(test_list)
        print("expected: {}".format(str(expected)))
        print("actual: {}".format(str(actual)))
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
