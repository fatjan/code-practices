def move_zeroes(nums):
    for i in range(len(nums)):
        j = i + 1
        for j in range(j, len(nums)):
            if nums[i] == 0:
                nums[j], nums[i] = nums[i], nums[j]
    print(nums)


move_zeroes([4, 2, 4, 0, 0, 3, 0, 5, 1, 0])
