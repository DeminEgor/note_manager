from datetime import datetime, date

# Получение текущей даты
today = date.today()  # Получение текущей даты с помощью оператора today
current_date = today.strftime('%d.%m.%Y')  # преобразование текущей даты в требуемый формат
print(f'\nТекущая дата: {current_date}\n')

# Ввод и проверка формата ввода дедлайн
while True:  # цикл проверки правильного ввода дедлайн
    try:
        issue_date = input(f'Введите дату истечения заметки (дедлайн) в формате - "ДД-ММ-ГГГГ" или "ГГГГ-ММ-ДД": ')
        if datetime.strptime(issue_date, '%d-%m-%Y'):
            break  # выход из цикла при корректном формате ДД.ММ.ГГГГ
        elif datetime.strptime(issue_date, '%Y-%m-%d'):
            break  # выход из цикла при корректном формате ГГГГ.ММ.ДД
        else:
            raise ValueError  # обработка ошибки
    except ValueError:
        print('Дата некорректна. Повторите ввод дедлайн в требуемой форме.')

print(f'\nДедлайн: {issue_date}\n')  # вывод на экран введенной даты

# Анализ и обработка даты дедлайн
deadline = datetime.strptime(issue_date, '%d-%m-%Y').date()  # преобразование даты дедлайна в формат date
delta = deadline - today  # получение дельты между датой дедлайна и текущей датой в формат timedelta
day = delta.days  # получение дельты между датой дедлайна и текущей датой в днях с помощью аргумента .day класс timedelta

if day > 0:
    print(f'До дедлайна осталось {day} дней.')
elif day == 0:
    print('Внимание, дедлайн истекает сегодня!')
else:
    day = day * -1  # делаем положительной дельту для вывода на экран
    print(f'Внимание, дедлайн истек {day} дней назад!')
