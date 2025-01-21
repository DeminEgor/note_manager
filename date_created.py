from datetime import datetime

created_date = '10.10.2020'
issue_date =  '12.12.2020'
temp_created_date = datetime.strptime(issue_date, '%d.%m.%Y')
temp_issue_date = datetime.strptime(created_date, '%d.%m.%Y')

created_date = temp_created_date.strftime('%d.%m')
issue_date = temp_issue_date.strftime('%d.%m')

print('Сreated date:', created_date)
print('Issue date:', issue_date)
