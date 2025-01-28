from datetime import datetime, date

def create_note():
    note = {}

    # Ввод и проверка данных
    while True:
        note["Name"] = input("Введите Имя пользователя (поле 'Имя' не может быть пустым): ")
        if note["Name"].strip() == "":
            print("Имя не может быть пустым. Повторите ввод.")
        else:
            break

    while True:
        note["Title"] = input("Введите Заголовок заметки (поле 'Заголовок' не может быть пустым): ")
        if note["Title"].strip() == "":
            print("Заголовок не может быть пустым. Повторите ввод.")
        else:
            break

    while True:
        note["Description"] = input("Введите Описание заметки (поле 'Описание' не может быть пустым): ")
        if note["Description"].strip() == "":
            print("Описание не может быть пустым. Повторите ввод.")
        else:
            break

    status = ['в процессе', 'отложено', 'выполнено']
    while True:
        note["Status"] = input('Введите Статус заметки (в процессе; отложено; выполнено): ')
        if note["Status"].strip() in status:
            break
        else:
            print("Такого Статуса не существует, введите корректный Статус заметки.")

    while True:
        note["CreationDate"] = input("Введите Дату создания заметки в формате 'день.месяц.год': ")
        try:
            datetime.strptime(note["CreationDate"], "%d.%m.%Y")
            break
        except ValueError:
            print("Дата некорректна. Повторите ввод Даты создания заметки в требуемом формате.")

    while True:
        note["Deadline"] = input("Введите дату истечения заметки (дедлайн) в формате 'день.месяц.год': ")
        try:
            datetime.strptime(note["Deadline"], "%d.%m.%Y")
            break
        except ValueError:
            print("Дата Дедлайна некорректна. Повторите ввод Дедлайна в требуемом формате.")

    return note

def delete_note(notes, index):
    if len(notes) > index + 1:
        del notes[index]

notes = []

print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')
while True:
    flag_new_note = input('Создать новую заметку (да/нет)?  ')
    if flag_new_note.strip().lower() == 'нет':
        break

    note = create_note()
    notes.append(note)

    print(f"Введено заметок - {len(notes)}.")

print("\nСписок заметок.")
for i, note in enumerate(notes, start=1):
    print(f"\nЗаметка № {i}: ")
    for key, value in note.items():
        print(key, "-", value)

# Удаление заметки
while True:
    print("\nВыберите номер заметки для удаления (или 'q' для выхода):")
    delete_index = input("\nВведите номер заметки: ")
    if delete_index.strip().lower() == 'q':
        break
    try:
        delete_note(notes, int(delete_index) - 1)
        print(f"Заметка {delete_index} успешно удалена.")
    except ValueError:
        print("Некорректный номер заметки. Повторите ввод.")

print("\nВвод заметок завершен.")

print(f"Введено заметок - {len(notes)}.")

# Вывод введенных заметок на экран
print("\nСписок заметок.")
for i in range(len(notes)):
    print(f"\nЗаметка № {i+1}: ")
    for key,value in notes[i].items():
            print(key, "-", value)
