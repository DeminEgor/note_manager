from datetime import datetime, date

from main import issue_date

# Получение текущей даты

today = date.today() # Получение текущей даты с помощью оператора, today
current_date = today.strftime('%d.%m.%Y')# преобразование текущей даты в требуемый формат
print('\nТекущая дата: ', current_date, '\n')

# Ввод и проверка формата ввода дедлайн
while True: # цикл проверки правильного ввода дедлайн
    try:
        issue_date = input(f'Введите дату истечения заметки (дедлайн) в формате - "ДД.ММ.ГГГГ": ')
        datetime.strptime(issue_date, '%d.%m.%Y')

        break # выход из цикла
    except ValueError: # обработка ошибки
        print('Дата некорректна. Повторите ввод дедлайн в требуемой форме.')
print('\nДедлайн: ', '\n') # ввод на экран даты дедлайн в требуемой форме

# Анализ и обработка даты дедлайн
deadline = datetime.strptime(issue_date, '%d.%m.%Y') # преобразование даты дедлайна в формат datetime
deadline = deadline.date() # преобразование даты дедлайна в формат date
delta = deadline - today # получение дельты между датой дедлайна и текущей датой в формат timedelta
day = delta.days # получение дельты между датой дедлайна и текущей датой в днях с помощью аргумента .day класс timedelta

if day > 0:
    print(f'До дедлайна осталось {day} дн.')
elif day == 0:
    print('Внимание, дедлайн истекает сегодня!')
else:
    day = day * -1 # делаем положительной дельту для вывода на экран
    print(f'Внимание дедлайн истек {day} дней назад!')
