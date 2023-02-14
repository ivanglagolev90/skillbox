import random


def change(nums):
    index = random.randint(0, 4)
    value = random.randint(100, 1000)
    nums = list(nums)
    nums[index] = value
    return tuple(nums), value


my_nums = (1, 2, 3, 4, 5)

new_nums, rand_val = change(my_nums)
print(new_nums, rand_val)
new_nums, rand_val1 = change(new_nums)
rand_val += rand_val1
print(new_nums, rand_val)