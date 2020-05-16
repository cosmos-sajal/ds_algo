# https://www.educative.io/courses/grokking-the-coding-interview/gxk639mrr5r
# https://leetcode.com/problems/3sum/


def search_triplets(arr):
    arr.sort()
    result_arr = []

    for i in range(len(arr) - 1):
        if i != 0 and arr[i] == arr[i - 1]:
            continue
        ptr1 = i + 1
        ptr2 = len(arr) - 1
        sum = 0 - arr[i]

        while ptr1 < ptr2:
            if ptr1 > (i + 1) and arr[ptr1] == arr[ptr1 - 1] and (ptr2 + 1) <= (len(arr) - 1) and arr[ptr2] == arr[ptr2 + 1]:
                ptr1 += 1
                ptr2 -= 1
                continue

            if arr[ptr1] + arr[ptr2] == sum:
                result_arr.append([arr[i], arr[ptr1], arr[ptr2]])
                ptr1 += 1
                ptr2 -= 1
            elif arr[ptr1] + arr[ptr2] < sum:
                ptr1 += 1
            else:
                ptr2 -= 1

    return result_arr


def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))
    print(search_triplets([-1, 0, 1, 2, -1, -4]))
    print(search_triplets([-2, 0, 0, 2, 2]))
    print(search_triplets([-1, 0, 1, 2, -1, -4]))
    print(search_triplets(
        [-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]))


main()
