def max_pairwise(arr):
    arr.sort()
    return arr[-2] * arr[-1]



if __name__ == '__main__':
    num = int(input())
    a = [int(x) for x in input().split(" ")]
    print(max_pairwise(a))

