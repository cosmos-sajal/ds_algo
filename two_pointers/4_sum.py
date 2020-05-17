# https://www.educative.io/courses/grokking-the-coding-interview/gxDOJJ7xAJl
# https://leetcode.com/problems/4sum/


def search_quadruplets(arr, target):
    arr.sort()
    result_set = set()
    result_arr_list = []
    total_count = 0

    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            sum_to_search = target - arr[i] - arr[j]
            ptr1, ptr2 = i + 1, len(arr) - 1

            if ptr1 >= len(arr) - 2:
                continue

            while ptr1 < len(arr) and ptr2 < len(arr) and ptr1 != i and ptr2 != j and ptr1 != j and ptr2 != i and ptr1 < ptr2:
                if arr[ptr1] + arr[ptr2] == sum_to_search:
                    pos_array = [arr[i], arr[j], arr[ptr1], arr[ptr2]]
                    pos_array.sort()
                    pos_tuple = tuple(pos_array)
                    if pos_tuple not in result_set:
                        result_set.add(pos_tuple)
                        result_arr_list.append(pos_array)
                        total_count += 1
                    ptr1 += 1
                    ptr2 -= 1
                elif arr[ptr1] + arr[ptr2] > sum_to_search:
                    ptr2 -= 1
                else:
                    ptr1 += 1

    return result_arr_list


def main():
    print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
    print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))


main()
