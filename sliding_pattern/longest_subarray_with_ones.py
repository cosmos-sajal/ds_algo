# https://www.educative.io/courses/grokking-the-coding-interview/B6VypRxPolJ
# https://leetcode.com/problems/max-consecutive-ones-iii/


def length_of_longest_substring(arr, k):
    freq_map = {0: 0, 1: 0}
    ptr1, ptr2 = 0, 0
    max_count, max_len = 0, 0

    for i in range(len(arr)):
        character = arr[ptr2]
        freq_map[character] += 1
        if arr[ptr2] == 1:
            max_count = max(max_count, freq_map[character])

        if (ptr2 - ptr1 - max_count + 1) > k:
            freq_map[arr[ptr1]] -= 1
            ptr1 += 1

        max_len = max(max_len, ptr2 - ptr1 + 1)

        ptr2 += 1

    return max_len


def main():
    print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_substring(
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()
