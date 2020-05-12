# https://www.educative.io/courses/grokking-the-coding-interview/R8DVgjq78yR


def add_in_map(freq_map, pos, str):
    if str[pos] in freq_map:
        freq_map[str[pos]] += 1
    else:
        freq_map[str[pos]] = 1

    return freq_map


def delete_from_map(freq_map, pos, str):
    if freq_map[str[pos]] == 1:
        del freq_map[str[pos]]
    else:
        freq_map[str[pos]] -= 1

    return freq_map


def length_of_longest_substring(str, k):
    ptr1, ptr2 = 0, 0
    freq_map = {}
    max_count, max_length = 0, 0

    for i in range(len(str)):
        freq_map = add_in_map(freq_map, ptr2, str)
        current_length = freq_map[str[ptr2]]
        max_count = max(max_count, current_length)

        if (ptr2 - ptr1 - max_count + 1) > k:
            freq_map = delete_from_map(freq_map, ptr1, str)
            ptr1 += 1

        max_length = max(max_length, ptr2 - ptr1 + 1)

        ptr2 += 1

    return max_length


def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))


main()
