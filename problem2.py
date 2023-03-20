
def indices_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j


nums = []
target=42
print(indices_sum(nums, target))



