# https://www.educative.io/courses/grokking-the-coding-interview/YMzBx1gE5EO


def add_in_set(alpha_set, character):
    alpha_set.add(character)

    return alpha_set


def delete_from_set(alpha_set, character):
    alpha_set.discard(character)

    return alpha_set


def get_max_length(max_len, ptr1, ptr2):
    if max_len < (ptr2 - ptr1 + 1):
        return (ptr2 - ptr1 + 1)
    else:
        return max_len


def non_repeat_substring(str):
    alpha_set = set()
    ptr1, ptr2, max_len = 0, 0, -1
    str_len = len(str)

    while ptr1 < str_len and ptr2 < str_len:
        if str[ptr2] in alpha_set:
            alpha_set = delete_from_set(alpha_set, str[ptr1])
            ptr1 += 1
        else:
            alpha_set = add_in_set(alpha_set, str[ptr2])
            max_len = get_max_length(max_len, ptr1, ptr2)
            ptr2 += 1

    return max_len


def main():
    print("Length of the longest substring: " +
          str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " +
          str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " +
          str(non_repeat_substring("abccde")))


main()
