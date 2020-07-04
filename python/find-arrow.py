line = input()
while line != 'return 0;':
    found_arrow = line.find('->')
    found_comment = line.find('//')
    if found_arrow and found_comment == -1:
        new_line = line.replace('->', '.')
    elif found_arrow < found_comment:
        arrow_count = line.count('->', 0,found_comment)
        new_line = line.replace('->', '.', arrow_count)
    else:
        new_line = line
    print(new_line)
    line = input()
print(line)