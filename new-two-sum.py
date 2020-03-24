def twoSum(nums, target):
        result = []
        number = sorted(nums)
        for i in range(len(number)-1):
            if number[i] + number[i + 1] == target:
                result.append(i)
                result.append(i+1)
        return result


print(twoSum([3, 2, 4], 6))
print(twoSum([3, 2, 3], 6))
