def merge_the_tools(string, k):
    # your code goes here
    dist = ''
    split = len(string) // k
    i = 0
    while i <= len(string)-split:
        sub = string[i:split+i]
        for j in range(len(sub)):
            if sub[j] not in dist:
                dist += sub[j]
        print(dist)
        dist = ''
        i += split

# merge_the_tools('AABCAAADA', 3)

merge_the_tools('FJKKABHHROOPPPPS', 4)
