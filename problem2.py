def indices(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            else:
                return "no pair in nums list sums to target"

nums = [2, 5, 3, 7, 3, 8]

target = 7
print(indices(nums, target))