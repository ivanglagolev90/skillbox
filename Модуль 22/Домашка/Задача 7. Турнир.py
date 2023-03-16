first_tour = open('C:\\task\\22_7\\first_tour.txt', 'r')

k = ''
for i in first_tour.readline():
    k += str(i)
k = int(k)

first_tour_list = [i.split() for i in first_tour.readlines()
                   if int(i.split()[2]) > k]
# print(first_tour_list)


second_tour = open('C:\\task\\22_7\\second_tour.txt', 'w')
count = 1
winner = ''
for i_list in first_tour_list:
    winner = str(count)+') ' + i_list[1][0]+'. ' + i_list[0] + ' ' + i_list[2]
    count += 1
    second_tour.write(winner)
    second_tour.write('\n')
second_tour.close()




