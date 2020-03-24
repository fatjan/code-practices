import timeit

code_to_test = """
for i in range(1, 101):
    isFizz = i % 3 == 0
    isBuzz = i % 5 == 0

    if isFizz and isBuzz:
        print("FizzBuzz")
        continue

    if isFizz:
        print("Fizz")
        continue

    if isBuzz:
        print("Buzz")
        continue

    if (not isFizz and not isBuzz):
        print(i)
"""
elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)
