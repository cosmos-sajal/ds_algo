# https://www.educative.io/courses/grokking-the-coding-interview/3YlQz7PE7OA
# https://leetcode.com/problems/3sum-closest/

import sys


def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    arr_len = len(arr)
    min_val = sys.maxsize

    for i in range(arr_len - 1):
        ptr1 = i + 1
        ptr2 = arr_len - 1
        sum = target_sum - arr[i]

        while ptr1 < ptr2:
            val = arr[ptr1] + arr[ptr2] + arr[i]
            difference = abs(target_sum - val)

            if difference < min_val:
                min_val = difference
                result = val

            if arr[ptr1] + arr[ptr2] == sum:
                min_val = 0
                break
            elif arr[ptr1] + arr[ptr2] > sum:
                ptr2 -= 1
            else:
                ptr1 += 1

    return result


def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()
