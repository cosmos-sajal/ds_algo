# https://www.educative.io/courses/grokking-the-coding-interview/Bn2KLlOR0lQ


def add_in_map(freq_map, str, pos):
    if str[pos] in freq_map:
        freq_map[str[pos]] += 1
    else:
        freq_map[str[pos]] = 1

    return freq_map


def delete_from_map(freq_map, str, pos):
    if freq_map[str[pos]] == 1:
        del freq_map[str[pos]]
    else:
        freq_map[str[pos]] -= 1

    return freq_map


def longest_substring_with_k_distinct(str, k):
    freq_map = {}
    ptr1, ptr2, longest_subarray = 0, 0, -1
    len_array = len(str)
    can_add_in_map = True

    while ptr1 < len_array and ptr2 < len_array:
        if can_add_in_map:
            freq_map = add_in_map(freq_map, str, ptr2)
        if len(freq_map) <= k:
            if longest_subarray < (ptr2 - ptr1 + 1):
                longest_subarray = (ptr2 - ptr1 + 1)
            ptr2 += 1
            can_add_in_map = True
        else:
            ptr1 += 1
            can_add_in_map = False
            freq_map = delete_from_map(freq_map, str, ptr1 - 1)

    return longest_subarray


def fruits_into_baskets(fruits):
    return longest_substring_with_k_distinct(fruits, 2)


def main():
    print("Maximum number of fruits: " +
          str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " +
          str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
