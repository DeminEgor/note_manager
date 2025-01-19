username = input('Введите имя пользователя: ')
print('Username: ', username.capitalize())

title1 = input('Введите заголовок заметки №1: ')
print('Title: ',title1)
title2 = input('Введите заголовок заметки №2: ')
print('Title: ',title2)
title3 = input('Введите заголовок заметки №3: ')
print('Title: ',title3)
titles = [title1, title2, title3]
print('Список заголовок заметок: ''Заметка №1 - ', title1 +';', 'Заметка №2- ', title2+ ';' ,'Заметка №3 - ', title3+'.' )

content = input("Введите описание заметки: ")
print('Content: ', content)

statis = input("Введите статус заметки:  ")
print('Statis: ', statis)

created_data = input("Введите дату создания заметки в формате-'ДД.ММ.ГГГГ': ")
print('Created_data: ',created_data )
issue_date = input("Введите дату истечения заметки (дедлайн)в формате-'ДД.ММ.ГГГГ': ")
print('Issue_date: ', issue_date)


