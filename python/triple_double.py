def triple_double(num1, num2):
    #code me ^^
    s_num1 = str(num1)
    s_num2 = str(num2)
    for i in range(len(s_num1)-2):
        if s_num1.count(s_num1[i]) == 3 and s_num2.count(s_num1[i]) == 2:
            return 1
        if s_num1[i] == s_num1[i+1] and s_num1[i+1] == s_num1[i+2]:
            for j in range(len(s_num2)-1):
                if s_num2[j] == s_num2[j+1] and s_num1[i] == s_num2[j]:
                    return 1
    return 0

print(triple_double(451999277, 41177722899))
print(triple_double(1222345, 12345))
print(triple_double(12345, 12345))
print(triple_double(666789, 12345667))
print(triple_double(10560002, 100))
print(triple_double(1112, 122))

