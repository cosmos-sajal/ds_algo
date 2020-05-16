# https://www.educative.io/courses/grokking-the-coding-interview/Y5YDWzqPn7O
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/


def get_words_freq(words):
    word_freq = {}

    for word in words:
        if word not in word_freq:
            word_freq[word] = 0
        word_freq[word] += 1

    return word_freq


def find_word_concatenation(str, words):
    if len(words) == 0 or len(words[0]) == 0:
        return []

    word_freq = get_words_freq(words)
    result_arr = []
    word_len = len(words[0])
    word_count = len(words)

    for i in range((len(str) - word_count * word_len) + 1):
        words_seen = {}

        for j in range(0, word_count):
            next_word_index = i + (j * word_len)
            word = str[next_word_index: next_word_index + word_len]

            if word not in word_freq:
                break

            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1

            if words_seen[word] > word_freq[word]:
                break

            if j + 1 == word_count:
                result_arr.append(i)

    return result_arr


def main():
    print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
    print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))
    print(find_word_concatenation("barfoothefoobarman", ["foo", "bar"]))
    print(find_word_concatenation(
        "wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))


main()
