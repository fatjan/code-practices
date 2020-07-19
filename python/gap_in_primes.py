def find_primes(start, end):
    nums = []
    for val in range(start, end + 1): 
        if val > 1: 
            for n in range(2, val//2 + 2): 
                if (val % n) == 0: 
                    break
                else: 
                    if n == val//2 + 1: 
                        nums.append(val)
    return nums

def gap(g, m, n):
    prime_nums = find_primes(m,n)
    print(prime_nums)
    for i in range(len(prime_nums)-1):
        if prime_nums[i+1] - prime_nums[i] == g:
            return [prime_nums[i], prime_nums[i+1]]
    return None

print(gap(2,100,110))
print(gap(4,100,110))