def removeDuplicates(nums):
    new = []
    for num in nums:
        if num not in new:
            new.append(num)
    return new


print(removeDuplicates([1, 1, 2]))
