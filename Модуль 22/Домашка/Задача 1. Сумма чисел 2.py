sum_file = open('C:\\task\\numbers2.txt', 'r')
i_sum = 0
for i in sum_file.readlines():
    tmp_str = i.strip()
    print(tmp_str)
    if tmp_str != '':
        i_sum += int(tmp_str)
sum_file.close()

new_file = open('new_file_name', 'w')
new_file.write(str(i_sum))
new_file.close()
