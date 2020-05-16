# https://www.educative.io/courses/grokking-the-coding-interview/mElknO5OKBO


def triplet_with_smaller_sum(arr, target):
    arr.sort()
    arr_len = len(arr)
    result = 0

    for i in range(arr_len - 1):
        ptr1 = i + 1
        ptr2 = arr_len - 1
        sum = target - arr[i]

        while ptr1 < ptr2:
            if arr[ptr1] + arr[ptr2] < sum:
                result += (ptr2 - ptr1)
                ptr1 += 1
            else:
                ptr2 -= 1

    return result


def main():
    print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
    print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()
