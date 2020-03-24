def solution(A, K):
    start = len(A) - K
    moveFront = []
    moveBack = []
    for i in range(len(A)):
        if i >= start:
            moveFront.append(A[i])
        else:
            moveBack.append(A[i])
    return moveFront + moveBack


print(solution([3, 4, 9, 12, 8], 6))
