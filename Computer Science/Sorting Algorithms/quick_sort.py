import unittest


def quick_sort(arr):
    # Create arrays to hold items smaller than, equal to, and greater than the pivot
    left = []
    pivots =[]
    right = []
    # Base case: list is only one item, and therefore is sorted.
    if len(arr) <= 1:
        return arr
    else:
    # Select a pivot.  Doesn't matter where.
        pivot  = arr[len(arr) // 2]
        # iterate through entire list, comparing each item to pivot value
        for i in arr:
            # If less than pivot, add to left array
            if i < pivot:
                left.append(i)
            # if greater than pivot, add to right array
            elif i > pivot:
                right.append(i)
            # item is equal to pivot, add to pivot array
            else:
                pivots.append(i)
        # Recursive step:  call function on left and right arrays to sort them
        left = quick_sort(left)
        right = quick_sort(right)

        # When recursive calls have returned, list is sorted. Concatenate and return the list
        return left + pivots + right




class Test_Sort(unittest.TestCase):

    def test_quick_sort(self):
        test_list = [99, 15, 4, 23, 7, 14, 0, 92]
        print("original: {}".format(str(test_list)))
        expected = sorted(test_list)
        actual = quick_sort(test_list)
        print("expected: {}".format(str(expected)))
        print("actual: {}".format(str(actual)))
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
