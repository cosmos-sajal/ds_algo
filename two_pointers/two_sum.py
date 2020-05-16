# https://www.educative.io/courses/grokking-the-coding-interview/xog6q15W9GP
# https://leetcode.com/problems/two-sum/


def create_structure(arr):
    struct_arr = []
    for i in range(len(arr)):
        struct_arr.append({'num': arr[i], 'pos': i})

    return struct_arr


def comparator(struct):
    return struct['num']


def pair_with_targetsum(arr, target_sum):
    struct_arr = create_structure(arr)
    sorted_arr = sorted(struct_arr, key=comparator)
    ptr1, ptr2 = 0, len(arr) - 1

    while ptr1 < ptr2:
        if sorted_arr[ptr1]['num'] + sorted_arr[ptr2]['num'] == target_sum:
            return [sorted_arr[ptr1]['pos'], sorted_arr[ptr2]['pos']]
        elif sorted_arr[ptr1]['num'] + sorted_arr[ptr2]['num'] > target_sum:
            ptr2 -= 1
        else:
            ptr1 += 1

    return []


def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))


main()
