# problem - https://www.educative.io/courses/grokking-the-coding-interview/7D5NNZWQ8Wr
# optimized


def find_averages_of_subarrays(K, arr):
    ptr, result = 0, []

    _total = 0.0
    for i in range(ptr, K):
        _total += arr[i]

    result.append(_total / K)

    for i in range(K, len(arr)):
        _total = _total + arr[i] - arr[ptr]
        ptr += 1
        result.append(_total / K)

    return result


def main():
    averages = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print(str(averages))


main()
