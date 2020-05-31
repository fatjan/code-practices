nums = [7,5,4,4,3,1,-2,-3,-5,-7]
total = 0
i = 0
while i < len(nums):
    if nums[i] > 0:
        total += nums[i]
    i += 1
print(total)

total = 0
for num in nums:
    if num > 0:
        