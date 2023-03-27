def count(n):
    count = 0
    for _ in n.split():
        count += int(_)
    yield count


nums = '3 5 7 6 2 3 8 5 7 5'

for i in count(nums):
    print(i)

print(count(nums))
