def to_weird_case(string):
    new_string = ''
    words = string.split(' ')
    for i in range(len(words)):
        for j in range(len(words[i])):
            if j % 2 == 0:
                new_string += words[i][j].upper()
            else:
                new_string += words[i][j].lower()
        if i != len(words) - 1:
            new_string += ' '
    return new_string
    

print(to_weird_case('This'))
print(to_weird_case('is'))
print(to_weird_case('This is a test'))

