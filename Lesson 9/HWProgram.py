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
# print(len(myWorkerDict))
# concatWorker = 'Employee ' + str(len(myWorkerDict) + 1)
# print(concatWorker)
menu = """
1 - Поиск сотрудника 
2 - Добавление нового сотрудника 
3 - Удаление сотрудника 
4 - Составить список для награждения сотрудников 
5 - Составить список сотрудников на отпуск 
6 - Повышение З-П 
7 - Понижение З-П 
8 - Отобразить имя сотрудника, получающий максимальную З-П 
9 - Отобразить имя сотрудника, получающий минимальную З-П 
10 - Подсчет среднемесячной Заработной платы 
11 - Вывод суммарной З-П всех сотрудников 
12 - Виды транспорта всех сотрудников 
13 - Отобразить имена и кол-во детей всех сотрудников 
14 - Отобразить всех сотрудников 
0 - Выход из Программы
"""
option = None
while option != 0:
    print(menu)

    option = int(input('Ввод: '))

    if option == 1:
        nameSearch = input('Вы выбрали меню №1.\nНапишите имя для поиска: ')

        for worker, workerDict in myWorkerDict.items():
            for key, valueWorker in workerDict.items():
                    if valueWorker == nameSearch:
                        for key, valueWorker in workerDict.items():
                            print(key, valueWorker)
    elif option == 2:
        nameInput = input('Вы выбрали меню №2.'
                          '\nНапишите ФИО Сотрудника для добавления: ')
        age = int(input('Возраст: '))
        typeWork = input('Род деятельности: ')
        salary = int(input('Напишите зарплату: '))
        fioWifeHusb = input('Напишите имя супруга/и: ')
        quantChild = int(input('Кол-во детей: '))
        child = {}

        # range(3) - 0,1,2
        for i in range(quantChild):
            # Ребенок + 0 + 1 = [Ребенок 1] = 'Усон Усонов'
            # Ребенок + 1 + 1 = [Ребенок 2] = 'Урамат Усонов'
            # Ребенок + 2 + 1 = [Ребенок 3] = 'Марат Усонов'
            childKey = 'Ребенок ' + str(i + 1)
            child[childKey] = input(f'Пожалуйста введите '
                                    f'имя для {i + 1} ребенка: ')

        nameOfTransport = input('Название транспорта: ')
        address = input('Адрес проживания: ')

        countWorker = len(myWorkerDict) + 1
        countWorkerKey = 'Сотрудник ' + str(countWorker)
        myWorkerDict[countWorkerKey] = {"ФИО": nameInput,
                                        "Возраст": age,
                                        "Род деятельности": typeWork,
                                        "Заработная плата": salary,
                                        "ФИО Супруга/и": fioWifeHusb,
                                        "Дети": child,
                                        "Транспорт": nameOfTransport,
                                        "Адрес проживания": address
                                        }

        print('Новый словарь работников теперь выглядит так:')

        for worker, workerDict in myWorkerDict.items():
            print("===================")
            print(f'{worker}:\n'
                  f'===================')
            for key, values in workerDict.items():
                if key == "Дети":
                    # ["Эсен", "Ураматов"]
                    workerNameList = workerDict["ФИО"].split(" ")
                    print(f'Дети {workerNameList[0]}а {workerNameList[1]}а : '
                          f'\n************************')

                    for child, childInfo in values.items():
                        print(f'{child}: {childInfo}')
                    print('************************')
                if key == "Дети":
                    continue
                print(f'{key}: {values}')
    elif option == 14:
        for worker, workerDict in myWorkerDict.items():
            print("===================")
            print(f'{worker}:\n'
                  f'===================')
            for key, values in workerDict.items():
                if key == "Дети":
                    workerNameList = workerDict["ФИО"].split(" ")
                    print(f'Дети {workerNameList[0]}а {workerNameList[1]}а : '
                          f'\n************************')

                    for child, childInfo in values.items():
                        print(f'{child}: {childInfo}')
                    print('************************')
                if key == "Дети":
                    continue
                print(f'{key}: {values}')
    if option == 0:
        print('Программа Завершена! Всего Вам хорошего!')
        break

        # 0-14
    elif option not in (range(0, 15)):
        print('Вы выбрали не правильную опцию! Попытайтесь заново!')









