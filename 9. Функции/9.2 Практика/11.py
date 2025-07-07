def median(nums):
    nums = sorted(nums)
    len_nums = len(nums)
    if len_nums % 2 != 0:
        return nums[len_nums // 2]
    else:
        return int(round((nums[len_nums // 2] + nums[len_nums // 2 - 1]) / 2, 2))

nums = [int(x) for x in input().split()]

print(round(median(nums), 0))
