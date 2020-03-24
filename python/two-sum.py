def twoSum( nums, target):
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j>=i:
                    if nums[i]+nums[j] == target and i != j:
                        result.append(i)
                        result.append(j)
                        break
                else:
                    continue
            if result != []:
                break
        return result


print(twoSum([3, 2, 4], 6))
print(twoSum([1, 1, 2]))
