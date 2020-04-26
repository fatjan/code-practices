def interpolate(n, instances, price):
    # Write your code here

    # if n is found in instances
    if n in instances:
        index_found = instances.index(n)
        return price[index_found]

    # remove item where price is 0.0
    new_ins = []
    new_price = []
    for i in range(len(instances)):
        if price[i]:
            new_ins.append(instances[i])
            new_price.append(price[i])

    # if there's only 1 price which is not 0.0 
    if len(new_price) == 1:
        index_found = price.index(new_price[0])
        return str(price[index_found])

    # find the position of n as regards to instances
    found_below = False
    # if n is below all the instances range
    if n < new_ins[0]:
        found_below = True
        ins1 = new_ins[0]
        ins2 = new_ins[1]
        p1 = new_price[0]
        p2 = new_price[1]

    found_above = False
    # if n is above all the new_ins range
    if n > new_ins[len(new_ins)-1]:
        found_above = True
        ins1 = new_ins[len(new_ins)-2]
        ins2 = new_ins[len(new_ins)-1]
        p1 = new_price[len(new_ins)-2]
        p2 = new_price[len(new_ins) - 1]

    found_within = False
    # if n is within any of the new_ins range
    for i in range(len(new_ins)-1):
        if new_ins[i] < n < new_ins[i+1]:
            found_within = True
            i1 = i
            i2 = i+1
            # i1 and i2 are the indexes at which n falls between these two new_ins
            break

    # x is the desired new_price, below is to find x with interpolation
    if found_within:
        x = (new_price[i2] - new_price[i1]) * (n - new_ins[i1]) / \
            (new_ins[i2] - new_ins[i1])
        x += new_price[i1]
    else:
        new_price_diff = p1 - p2
        amount = ins2 - ins1
        if found_above:
            jumps = (n - ins2) / amount
            x = p2 - new_price_diff * jumps
        # if found below
        else:
            jumps = (ins1 - n) / amount
            x = p1 + new_price_diff * jumps
    x = '%.2f' % x
    return x


# print(interpolate(29, [5, 25, 39, 40, 45], [1.78, 4.98, 5.98, 6.12, 7.21]))
# print(interpolate(29, [5, 25, 39, 40, 45], [0.0, 0.0, 0.0, 0.0, 7.21]))
# print(interpolate(29, [5, 25, 39, 40, 45], [0.0, 0.0, 7.21, 0.0, 4.09]))
# print(interpolate(501, [10, 25, 50, 100, 500], [0.0, 0.0, 21.25, 0.0, 15.5]))
# print(interpolate(1999, [10, 25, 50, 100, 500], [27.32, 23.13, 21.25, 18.0, 15.5]))
print(interpolate(9, [10, 25, 50, 100, 500],
                  [27.32, 23.13, 21.25, 18.0, 15.5]))
