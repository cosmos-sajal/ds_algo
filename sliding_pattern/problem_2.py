# https://www.educative.io/courses/grokking-the-coding-interview/YQ8N2OZq0VM
# https://leetcode.com/problems/find-all-anagrams-in-a-string/


def get_initialised_freq_list():
    return [0] * 26


def create_pattern_freq_list(pattern):
    pattern_freq_list = get_initialised_freq_list()
    for i in range(len(pattern)):
        pattern_freq_list[ord(pattern[i]) - ord('a')] += 1

    return pattern_freq_list


def add_in_list(freq_list, str, pos):
    freq_list[ord(str[pos]) - ord('a')] += 1

    return freq_list


def delete_from_list(freq_list, str, pos):
    if freq_list[ord(str[pos]) - ord('a')] == 0:
        return freq_list
    else:
        freq_list[ord(str[pos]) - ord('a')] -= 1

        return freq_list


def add_in_result_if_match(freq_list, pattern_freq_list, result_arr, pos):
    if freq_list == pattern_freq_list:
        result_arr.add(pos)

    return result_arr


def find_string_anagrams(str, pattern):
    pattern_freq_list = create_pattern_freq_list(pattern)
    ptr1, ptr2 = 0, 0
    result_arr, freq_list = set(), get_initialised_freq_list()

    for ptr2 in range(len(str)):
        freq_list = add_in_list(freq_list, str, ptr2)

        result_arr = add_in_result_if_match(
            freq_list, pattern_freq_list, result_arr, ptr1)

        while pattern_freq_list[ord(str[ptr2]) - ord('a')] < freq_list[ord(str[ptr2]) - ord('a')]:
            freq_list = delete_from_list(freq_list, str, ptr1)
            ptr1 += 1

            result_arr = add_in_result_if_match(
                freq_list, pattern_freq_list, result_arr, ptr1)

    result_arr = add_in_result_if_match(
        freq_list, pattern_freq_list, result_arr, ptr1)

    return list(result_arr)


def main():
    print(find_string_anagrams("abbcabc", "abc"))


main()
