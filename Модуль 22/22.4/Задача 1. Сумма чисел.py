sum_file = open('C:\\task\\numbers.txt', 'r')
i_sum = 0
for i in sum_file:
    i_sum += int(i)
i_sum=str(i_sum)
sum_file.close()

new_file = open('new_file_name', 'w')
new_file.write(i_sum)
new_file.close()
