import unittest


def merge_sort(list_to_sort):
    # divide and conquer!
    # if len(list) > 1, keep dividing
    if len(list_to_sort) > 1:
        mid_point = len(list_to_sort) // 2
        left_half = list_to_sort[:mid_point]
        right_half = list_to_sort[mid_point:]

        merge_sort(left_half)
        merge_sort(right_half)

        # Establish a pointer to walk each list being merged, as well as a
        # main pointer to keep track of where the next smallest value should be
        # placed
        left_pointer = 0
        right_pointer = 0
        main_pointer = 0

        # Condition: Both pointers have not yet reached the end of their
        # respective lists
        while left_pointer < len(left_half) and right_pointer < len(right_half):
            if left_half[left_pointer] < right_half[right_pointer]:
                list_to_sort[main_pointer] = left_half[left_pointer]
                left_pointer += 1
            else:
                list_to_sort[main_pointer] = right_half[right_pointer]
                right_pointer += 1
            main_pointer += 1

        # Condition: Only the left pointer has not reached the end of its list
        while left_pointer < len(left_half):
            list_to_sort[main_pointer] = left_half[left_pointer]
            left_pointer += 1
            main_pointer += 1

        # Condition Only the right pointer has not reached the end of its list
        while right_pointer < len(right_half):
            list_to_sort[main_pointer] = right_half[right_pointer]
            right_pointer += 1
            main_pointer += 1

        return list_to_sort


class Test_Sort(unittest.TestCase):

    def test_merge_sort(self):
        test_list = [99, 15, 4, 23, 7, 14, 0, 92]
        print("original: {}".format(str(test_list)))
        actual = merge_sort(test_list)
        expected = sorted(test_list)
        print("expected: {}".format(str(expected)))
        print("actual: {}".format(str(actual)))
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
