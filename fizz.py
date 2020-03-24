import timeit

code_to_test = """
for i in range(1,101):
    
    if i % 15 == 0:
        print("FizzBuzz")
        
    elif i % 3 == 0:
        print("Fizz")
        
    elif i % 5 == 0:
        print("Buzz")
      
    else:
        print(i)
"""
elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)
