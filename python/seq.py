cases = int(input())
for case_num in range(1,cases+1):
    line1 = input()
    l1 = line1.split(' ')
    n = int(l1[0])
    s = int(l1[1])
    l2 = input()
    prices = [int(x) for x in l2.split(" ")]
    items = 0
    cost = 0
    while items < s:
        min_p = min(prices)
        items += 1
        cost += min_p
        i_min = prices.index(min_p)
        if i_min == 0:
            larger = prices[i_min + 1]
        elif i_min == len(prices)-1:
            larger = prices[i_min - 1]
        else:
            a = prices[i_min - 1]
            b = prices[i_min + 1]
            larger = max(a,b)
        items += 1
        prices[prices.index(min_p)] = 10**9 + 1 
        prices[prices.index(larger)] = 10**9 + 1
    print('Case ' + str(case_num) + ': ' + str(cost) )


