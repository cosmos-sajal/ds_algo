# https://leetcode.com/problems/valid-anagram/


def get_initialised_freq_list():
    return [0] * 26


def populate_freq_list(str):
    freq_list = get_initialised_freq_list()

    for i in range(len(str)):
        freq_list[ord(str[i]) - ord('a')] += 1

    return freq_list


def is_anagram(str1, str2):
    freq_list_1, freq_list_2 = populate_freq_list(
        str1), populate_freq_list(str2)

    return freq_list_1 == freq_list_2


def main():
    print(is_anagram('abc', 'bcaa'))


main()
