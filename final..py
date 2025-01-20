note{}

note['Username: '] = input('Введите имя пользователя: ')
note['Content: '] = input("Введите описание заметки: ")
note['Statis: '] = input("Введите статус заметки:  ")
note['Created_data: '] = input("Введите дату создания заметки в формате-'ДД.ММ.ГГГГ': ")
note['Issue_date: '] = input("Введите дату истечения заметки (дедлайн)в формате-'ДД.ММ.ГГГГ': ")

title1 = input('Введите заголовок заметки №1: ')
title2 = input('Введите заголовок заметки №2: ')
title3 = input('Введите заголовок заметки №3: ')
titles = [title1, title2, title3]
note['Список заголовок заметок: '] = titles

for key,value in note.items():
   print(key,value)
