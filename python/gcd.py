def eucl_gcd(a,b):
    if b == 0:
        return a
    else:
        a_ = a % b 
    return eucl_gcd(b, a_)


# print(eucl_gcd(49,260))
# print(eucl_gcd(1653264,3918848))
print(eucl_gcd(357,234))

