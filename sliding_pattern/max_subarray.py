# https://www.educative.io/courses/grokking-the-coding-interview/JPKr0kqLGNP


def get_max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


def max_sub_array_of_size_k(k, arr):
    _max_sum = 0
    _total = 0
    _ptr = 0

    for i in range(k):
        _total += arr[i]

    _max_sum = get_max(_total, _max_sum)

    for i in range(k, len(arr)):
        _total = _total + arr[i] - arr[_ptr]
        _ptr += 1
        _max_sum = get_max(_total, _max_sum)

    return _max_sum


def main():
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()
