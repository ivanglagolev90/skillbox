def palind(num):
    reverse_list = []
    for i_1 in range(len(num)-1, -1, -1):
        reverse_list.append(num[i_1])
    if num == reverse_list:
        return True
    else:
        return False

nums = [1, 2, 3, 4, 3, 2]
new_nums = []
answer = []

for i in range(0, len(nums)):
    for j in range (i, len(nums)):
        new_nums.append(nums[j])
    if palind(new_nums):
        for i_ans in range(0, i):
            answer.append(nums[i_ans])
        answer.reverse()
        break
    new_nums = []

print('Исходный список', nums)
print('Чисел для палиндрома', len (answer))
print('Список этих чисел', answer)
