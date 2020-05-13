# https://www.educative.io/courses/grokking-the-coding-interview/N8vB7OVYo2D
# https://leetcode.com/problems/permutation-in-string/


def populate_map(pattern):
    pattern_freq_map = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
                        'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
                        'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
                        'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for i in range(len(pattern)):
        pattern_freq_map[pattern[i]] += 1

    return pattern_freq_map


def add_in_map(freq_map, pos, str):
    if str[pos] not in freq_map:
        freq_map[str[pos]] = 1
    else:
        freq_map[str[pos]] += 1

    return freq_map


def delete_from_map(freq_map, pos, str):
    if freq_map[str[pos]] == 0:
        freq_map[str[pos]] = 0
    else:
        freq_map[str[pos]] -= 1

    return freq_map


def find_permutation(str, pattern):
    freq_map = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
                        'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
                        'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
                        'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    ptr1, ptr2 = 0, 0
    pattern_freq_map = populate_map(pattern)

    for ptr2 in range(len(str)):
        freq_map = add_in_map(freq_map, ptr2, str)

        if freq_map == pattern_freq_map:
            return True

        while pattern_freq_map[str[ptr2]] < freq_map[str[ptr2]]:
            freq_map = delete_from_map(freq_map, ptr1, str)
            ptr1 += 1

    return freq_map == pattern_freq_map


def main():
    print(find_permutation("abcbacab", "abca"))


main()
