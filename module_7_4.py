team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score1 + score2
time_avg = (team1_time + team2_time) / tasks_total
#challenge_result = 'Победа команды Волшебники данных!'

#Использование %:
print('В команде Мастера кода участников: %s!' % team1_num)
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))

#Использование format():
print('Команда Волшебники данных решила задач: {}!'.format(score2))
print('Волшебники данных решили задачи за {} c'.format(team1_time))

#Использование f-строк:
print(f'Команды решили {score1} и {score2} задач')

if score1 > score2 or score1 == score2 and team1_time > team2_time:
    challenge_result = 'победа команды Мастер кода!'
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    challenge_result = 'победа команды Волшебники данных!'
else:
    challenge_result = 'ничья'

print(f'Результат битвы: {challenge_result}')

print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!.')