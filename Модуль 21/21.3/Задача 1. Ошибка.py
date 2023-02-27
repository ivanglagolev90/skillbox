import random


def change_dict(dct):
    num = random.randint(1, 100)
    for i_key, i_value in dct.items():
        if isinstance(i_value, list):
            i_value.append(num)
        if isinstance(i_value, dict):
            i_value[num] = i_key
        if isinstance(i_value, set):
            i_value.add(num)


nums_list = [1, 2, 3]
some_dict = {1: 'text', 2: 'another text'}
uniq_nums = {1, 2, 3}
nums_list1 = nums_list.copy()
some_dict1 = some_dict.copy()
uniq_nums1 = uniq_nums.copy()
common_dict = {1: nums_list1, 2: some_dict1, 3: uniq_nums1, 4: (10, 20, 30)}

change_dict(common_dict)
print(common_dict)

print()
print(nums_list)
print(some_dict)
print(uniq_nums)