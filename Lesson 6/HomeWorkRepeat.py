# Task 1
myWorkerDict = {
    'Employee 1':
        {
            'Full name': 'Adilet Eshmamatov',
            'Age': 28,
            'Occupation': 'Worker of the shop',
            'Salary': 25000,
            'Full name of spouse': 'Gulzada Saratova',
            'Children': {
                'Kid 1': 'Muhammad Eshmamatov',
                'Kid 2': 'Eliza Eshmamatova'
            },
            'Transport': 'Toyota Camry 35',
            'Living address': 'Bishkek city, L.Tolstoy street 77'
        },
    'Employee 2':
        {
            'Full name': 'Esen Urmatov',
            'Age': 30,
            'Occupation': 'Worker of the shop',
            'Salary': 31000,
            'Full name of spouse': 'Tamara Tilenova',
            'Children': {
                'Kid 1': 'Uson Urmatov',
            },
            'Transport': 'Honda Fit',
            'Living address': 'Bishkek city, Chui street 123'
        },
    'Employee 3':
        {
            'Full name': 'Asel Davletova',
            'Age': 30,
            'Occupation': 'Accounting staff member',
            'Salary': 42000,
            'Full name of husband': 'Sergey Vasiliev',
            'Children': {
                'Kid 1': 'Elena Vasilieva',
                'Kid 2': 'Stepan Vasiliev',
                'Kid 3': 'Marat Vasiliev',
            },
            'Transport': 'Honda Odyssey',
            'Living address': 'Bishkek city, Toktogul street 76'
        },
    'Employee 4':
        {
            'Full name': 'Maria Stepanova',
            'Age': 29,
            'Occupation': 'Marketing officer',
            'Salary': 35000,
            'Full name of husband': 'Oleg Kichin',
            'Children': {
                'Kid 1': 'Vasilisa Kichina',
            },
            'Transport': 'Walking',
            'Living address': 'Bishkek city, 7 micro-district, b. 76, app. 14 '
        },
    'Employee 5':
        {
            'Full name': 'Oleg Ivanov',
            'Age': 45,
            'Occupation': 'General director',
            'Salary': 70000,
            'Full name of spouse': 'Svetlana Valerieva',
            'Children': {
                'Kid 1': 'Grigory Ivanov',
                'Kid 2': 'Natalya Ivanova',
                'Kid 3': 'Vasilii Ivanov',
                'Kid 4': 'Filip Ivanov',
            },
            'Transport': 'BMW X7',
            'Living address': 'Bishkek city, 5 micro-district, b. 16, app. 102 '
        },
}
print('1 - Поиск сотрудника')
print('2 - Добавление нового сотрудника')
print('3 - Удаление сотрудника')
print('4 - Составить список для награждения сотрудников')
print('5 - Составить список сотрудников на отпуск')
print('6 - Повышение З-П')
print('7 - Понижение З-П')
print('8 - Отобразить имя сотрудника, получающий максимальную З-П')
print('9 - Отобразить имя сотрудника, получающий минимальную З-П')
print('10 - Подсчет среднемесячной Заработной платы')
print('11 - Вывод суммарной З-П всех сотрудников')
print('12 - Виды транспорта всех сотрудников')
print('13 - Отобразить имена и кол-во детей всех сотрудников')
print('0 - Выход из Программы')
print('Good day, dear User')
print('Please enter the number from this menu, to get access to the functionality you need!')

print()
# choice = ''
# while choice != 0:
choice = int(input('Your choice please: '))
for key in myWorkerDict:
    if choice == 1:
        print('You choose:  Поиск сотрудника')
        name = (input('Please input the name of employee for searching: '))
        print(myWorkerDict.get(name))

