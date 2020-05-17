# https://www.educative.io/courses/grokking-the-coding-interview/RMV1GV1yPYz\
# https://leetcode.com/problems/subarray-product-less-than-k/


def find_subarrays(arr, target):
    ptr1, ptr2, temp_product = 0, 0, 1
    result_count = 0

    while ptr1 <= ptr2 and ptr2 < len(arr):
        temp_product *= arr[ptr2]

        if temp_product < target:
            result_count += (ptr2 - ptr1 + 1)
        else:
            while ptr1 < len(arr) and temp_product >= target:
                temp_product /= arr[ptr1]
                ptr1 += 1
                if temp_product < target:
                    result_count += (ptr2 - ptr1 + 1)

        ptr2 += 1

    return result_count


def main():
    print(find_subarrays([2, 5, 3, 10], 30))
    print(find_subarrays([8, 2, 6, 5], 50))
    print(find_subarrays([1, 2, 3], 0))


main()
