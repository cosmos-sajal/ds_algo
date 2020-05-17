# https://www.educative.io/courses/grokking-the-coding-interview/RMBxV6jz6Q0


def dutch_flag_sort(arr):
    # sort 2 at the end
    ptr1, ptr2 = 0, len(arr) - 1

    while ptr1 < ptr2:
        if arr[ptr1] == 1 or arr[ptr1] == 0:
            ptr1 += 1
        elif arr[ptr1] == 2:
            while ptr2 > 0 and arr[ptr2] == 2:
                ptr2 -= 1
            if ptr2 <= ptr1:
                break
            arr[ptr1], arr[ptr2] = arr[ptr2], arr[ptr1]
            ptr1 += 1
            ptr2 -= 1

    # sort 0 and 1
    ptr1 = 0
    if arr[ptr2] == 2:
        ptr2 -= 1

    while ptr1 < ptr2:
        if arr[ptr1] == 0:
            ptr1 += 1
        else:
            while ptr2 > 0 and arr[ptr2] == 1:
                ptr2 -= 1
            if ptr2 <= ptr1:
                break
            arr[ptr1], arr[ptr2] = arr[ptr2], arr[ptr1]
            ptr1 += 1
            ptr2 -= 1

    return arr


def main():
    arr = [2, 0, 2, 1, 1, 0]
    dutch_flag_sort(arr)
    print(arr)

    arr = [2, 2, 0, 1, 2, 0]
    dutch_flag_sort(arr)
    print(arr)

    arr = [1, 1]
    dutch_flag_sort(arr)
    print(arr)

    arr = [1, 2]
    dutch_flag_sort(arr)
    print(arr)

    arr = [0, 1, 2]
    dutch_flag_sort(arr)
    print(arr)

    arr = [1, 2, 0]
    dutch_flag_sort(arr)
    print(arr)

    arr = [1, 0, 2]
    dutch_flag_sort(arr)
    print(arr)

    arr = [2, 1, 2]
    dutch_flag_sort(arr)
    print(arr)


main()
