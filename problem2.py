def indices_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return nums[i], nums[j]


nums = [1, 2, 3, 4, 5]
target = 6
print(indices_sum(nums, target))


def sumOfTwo(array, target):
    i = 0
    j = len(array) - 1
    while i < j:
      add = array[i] + array[j]
      if add == target:
        return array[i],array[j]
      elif add < target:
        i += 1
      else:
        j -= 1
    return 'None'

array = [12,15,10,2,4,7]
target = 14
print(sumOfTwo(array, target))
