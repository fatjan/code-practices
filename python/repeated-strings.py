def repeatedString(s, n):
    # start_time = time.time()
    # print(start_time)
    subs = n // len(s) * s + s[: n % len(s)]
    # end_time = time.time()
    # print(end_time)
    return subs.count('a')

print(repeatedString('aba', 1000000000))
# print("\nThe amount of a is and time to print the repeated strings:", repeatedString('aba', 1000))
