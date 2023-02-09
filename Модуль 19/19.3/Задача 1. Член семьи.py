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
for i in family_member.get('children', {}):
   for m in i:
    if (m.get('name', {}).get(na, {})):
        print('есть')

#print(family_member.get('children', {}) .get('name', {}).get(na, 'Nochild'))

