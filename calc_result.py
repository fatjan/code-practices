def calculate_test_result(scores):
    total = 0

    for i in range(len(scores)):
        if i == 0:
            if scores[i] == 'O':
                total += 1
        elif i == 1:
            if scores[i] == 'O' and scores[i-1] == 'O':
                total += 2
            elif scores[i] == 'O':
                total += 1
        else:
            if scores[i] == 'O' and scores[i-1] == 'O' and scores[i-2] == 'O':
                total += 3
            elif scores[i] == 'O' and scores[i-1] == 'O':
                total += 2
            elif scores[i] == 'O':
                total += 1
    return total


print(calculate_test_result("OOXXOXXOOOXOXOO"))
