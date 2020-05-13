# https://www.educative.io/courses/grokking-the-coding-interview/3wDJAYG2pAR
# https://leetcode.com/problems/minimum-window-substring/


def get_initialised_freq_list():
    return [0] * 256


def create_freq_list(str):
    freq_list = get_initialised_freq_list()
    for i in range(len(str)):
        freq_list[ord(str[i])] += 1

    return freq_list


def add_in_list(freq_list, str, pos):
    freq_list[ord(str[pos])] += 1

    return freq_list


def delete_from_list(freq_list, str, pos):
    freq_list[ord(str[pos])] -= 1

    return freq_list


def is_pattern_contained(freq_list, pattern_freq_list):
    for i in range(len(pattern_freq_list)):
        if pattern_freq_list[i] > freq_list[i]:
            return False

    return True


def find_substring(str, pattern):
    pattern_freq_list = create_freq_list(pattern)
    ptr1, ptr2 = 0, 0
    result_ptr1, result_ptr2 = len(str) + 10, len(str) + 10
    freq_list = get_initialised_freq_list()
    min_len = len(str) + 10

    for ptr2 in range(len(str)):
        freq_list = add_in_list(freq_list, str, ptr2)

        if is_pattern_contained(freq_list, pattern_freq_list):
            if min_len > (ptr2 - ptr1 + 1):
                min_len = ptr2 - ptr1 + 1
                result_ptr1 = ptr1
                result_ptr2 = ptr2

        while is_pattern_contained(freq_list, pattern_freq_list):
            freq_list = delete_from_list(freq_list, str, ptr1)
            ptr1 += 1

            if is_pattern_contained(freq_list, pattern_freq_list):
                if min_len > (ptr2 - ptr1 + 1):
                    min_len = ptr2 - ptr1 + 1
                    result_ptr1 = ptr1
                    result_ptr2 = ptr2

    if is_pattern_contained(freq_list, pattern_freq_list):
        if min_len > (ptr2 - ptr1 + 1):
            min_len = ptr2 - ptr1 + 1
            result_ptr1 = ptr1
            result_ptr2 = ptr2

    if result_ptr1 == len(str) + 10:
        return ""
    else:
        return str[result_ptr1:result_ptr2 + 1]


def main():
    print(find_substring("aaaaaaaaaaaabbbbbcdd", "abcdd"))


main()
