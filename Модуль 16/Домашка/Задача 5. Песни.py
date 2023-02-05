violator_songs = [['World in My Eyes', 4.86],['Sweetest Perfection', 4.43],['Personal Jesus', 4.56],['Halo', 4.9],['Waiting for the Night', 6.07],['Enjoy the Silence', 4.20],['Policy of Truth', 4.76],['Blue Dress', 4.29],['Clean', 5.83]]
n = int(input('Сколько песен выбрать? '))
print()
count = 0

for songs in range(n):
  print('Название', songs+1, 'песни:', end=' ')
  song = input()
  for i in range(len(violator_songs)):
    if violator_songs[i][0] == song:
      count += violator_songs[i][1]

print()
print('Общее время звучания:', round(count,2))