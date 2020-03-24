def addStrings(num1, num2):
    total = 0
    if len(num1) == len(num2):
        for i in range(len(num2) - 1, -1, -1):
            # print(i)
            # print(len(num1)-1)
            total += int(num2[i])*10**(len(num1)-1-i) + \
                int(num1[i])*10**(len(num1)-1-i)
    elif len(num1) < len(num2):
        for i in range(len(num2)):
            print(i)
            if i + 1 > len(num1):
                break
            else:
                total += int(num2[len(num2)-i-1])*10**i + \
                    int(num1[len(num1)-i-1])*10**i
        total += int(num2[:len(num2)-len(num1)])*10**len(num1)
    else:
        for i in range(len(num1)):
            print(i)
            if i + 1 > len(num2):
                break
            else:
                total += int(num2[len(num2)-i-1]) * \
                    10**i + int(num1[len(num1)-i-1])*10**i
        total += int(num1[:len(num1)-len(num2)])*10**len(num2)
    return str(total)


# print(addStrings('9', '99'))
# print(addStrings('9', '999'))
# print(addStrings('123', '456'))
# print(addStrings('98', '9'))
print(addStrings('31', '121'))
