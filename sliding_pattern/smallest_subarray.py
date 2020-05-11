# https://www.educative.io/courses/grokking-the-coding-interview/7XMlMEQPnnQ


def get_sum_between_ptr(sum_array, i, j):
    if i == 0:
        return sum_array[j]
    else:
        return sum_array[j] - sum_array[i - 1]


def get_smallest_subarray_size(size, ptr1, ptr2):
    if size > (ptr2 - ptr1 + 1):
        return (ptr2 - ptr1 + 1)
    else:
        return size


def smallest_subarray_with_given_sum(s, arr):
    _sum_array = []

    _total = 0
    for i in range(len(arr)):
        _total += arr[i]
        _sum_array.append(_total)

    ptr1, ptr2, _sum = 0, 0, 0
    smallest_subarray_size = len(arr) + 10

    while ptr1 < len(arr) and ptr2 < len(arr):
        # sum is the variable that will hold the sum between
        # ptr1 and ptr2
        _sum = get_sum_between_ptr(_sum_array, ptr1, ptr2)
        if _sum >= s:
            smallest_subarray_size = get_smallest_subarray_size(
                smallest_subarray_size, ptr1, ptr2)
            ptr1 += 1

        else:
            ptr2 += 1

    if smallest_subarray_size == len(arr) + 10:
        return -1
    else:
        return smallest_subarray_size


def main():
    print("Smallest subarray length: " +
          str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " +
          str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " +
          str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()
