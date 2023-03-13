a_file = open('C:\\task\\zen.txt', 'r')

a_list = a_file.readlines()
for i in reversed(a_list):
    print(i)
    