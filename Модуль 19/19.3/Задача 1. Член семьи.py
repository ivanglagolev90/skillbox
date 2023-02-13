family_member = {
    "name": "Jane",
    "surname": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "name": "Alice",
            "age": 6
        },
        {
            "name": "Bob",
            "age": 8
        }
    ]
}

for i in family_member:
    print(i, ':', family_member[i])

na = input('Имя: ')
flag = False
for i in family_member.get('children', {}):
  if i.get('name', {}) == na:
    flag = True
    break

if flag:
  print('Есть')
else:
  print('нет')

