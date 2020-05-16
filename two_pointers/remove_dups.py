# https://www.educative.io/courses/grokking-the-coding-interview/mEEA22L5mNA


def remove_duplicates(arr):
    arr_len = len(arr)

    if arr_len == 0 or arr_len == 1:
        return arr_len

    ptr1, ptr2 = 0, 1

    while ptr2 < arr_len:
        if arr[ptr1] == arr[ptr2]:
            ptr2 += 1
            continue

        arr[ptr1 + 1] = arr[ptr2]
        ptr1 += 1
        ptr2 += 1

    return ptr1 + 1


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()
