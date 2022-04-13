myWorkerDict = {

"Сотрудник 1":

        { "ФИО": "Адилет Эшмаматов",
          "Возраст": 28,
          "Род деятельности": "Работник цеха",
          "Заработная плата": 25000,
          "ФИО Супруга/и": "Гульзада Саратова",
          "Дети": { "Ребенок 1": "Мухаммад Эшмаматов",
                    "Ребенок 2": "Элиза Эшмаматова"

        },
          "Транспорт": "Тойота Камри 35",
          "Адрес проживания": "г. Бишкек, ул. Лев Толстой 77"

        },

"Сотрудник 2":

        { "ФИО": "Эсен Урматов",
          "Возраст": 30,
          "Род деятельности": "Работник цеха",
          "Заработная плата": 31000,
          "ФИО Супруга/и": "Тамара Тиленова",
          "Дети": { "Ребенок 1": "Усон Урматов", },
          "Транспорт": "Хонда Фит",
          "Адрес проживания": "г. Бишкек, ул. Чуй 123"
        },

"Сотрудник 3":

        {
            "ФИО": "Аселя Давлетова",
            "Возраст": 30,
            "Род деятельности": "Работник бухгалтерии",
            "Заработная плата": 42000,
            "ФИО Супруга/и": "Сергей Васильев",
            "Дети": { "Ребенок 1": "Елена Васильева",
                      "Ребенок 2": "Степан Васильев",
                      "Ребенок 3": "Марат Васильев", },
            "Транспорт": "Хонда Одиссей",
            "Адрес проживания": "г. Бишкек, ул. Токтогула 76"

        },

"Сотрудник 4":

    {
        "ФИО": "Мария Степанова",
        "Возраст": 29,
        "Род деятельности": "Работник маркетинга",
        "Заработная плата": 35000,
        "ФИО Супруга/и": "Олег Кичин",
        "Дети": { "Ребенок 1": "Василиса Кичина", },
        "Транспорт": "Пешком",
        "Адрес проживания": "г. Бишкек, мкр 7 дом 76, кв: 14"
    },
}


# print(len(myWorkerDict))
# concatWorker = 'Сотдрудник '+ str(len(myWorkerDict)+1)
# print(concatWorker)
#
# myWorkerDict[concatWorker] = {
# "ФИО": nameInput,
#
#
# }
#Task1:

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
while option!=0:
    print(menu)

    option = int(input('Ввод: '))

    if option == 1:
        nameSearch = input('Вы выбрали меню №1.\nНапишите имя для поиска: ')

        for worker, workerDict in myWorkerDict.items():
            for key, valueWorker in workerDict.items():
                    if valueWorker == nameSearch:
                        for key, valueWorker in workerDict.items():
                            print(key, valueWorker)

    elif option ==2:
        nameInput = input('Вы выбрали меню №1.'
                          '\nНапишите ФИО Сотрудника для добавления: ')
        age = int(input('Возраст: '))
        typeWork = input('Род деятельности: ')
        salary = int(input('Напишите зарплату: '))
        fioWifeHusb = input('Напишите имя супруга/и: ')
        quantChild = int(input('Кол-во детей: '))
        child = {}

        #range(3) - 0,1,2
        for i in range(quantChild):
            #Ребенок + 0 + 1 = [Ребенок 1] = 'Усон Усонов'
            # Ребенок + 1 + 1 = [Ребенок 2] = 'Урамат Усонов'
            # Ребенок + 2 + 1 = [Ребенок 3] = 'Марат Усонов'
            childKey = 'Ребенок '+ str(i+1)
            child[childKey] = input(f'Пожалуйста введите '
                                    f'имя для {i+1} ребенка: ')


        nameOfTransport = input('Название транспорта: ')
        address = input('Адрес проживания: ')

        countWorker = len(myWorkerDict)+ 1
        countWorkerKey = 'Сотрудник '+ str(countWorker)
        myWorkerDict[countWorkerKey] =      {     "ФИО": nameInput,
                                                  "Возраст": age,
                                                  "Род деятельности":typeWork,
                                                  "Заработная плата":salary,
                                                  "ФИО Супруга/и":fioWifeHusb,
                                                  "Дети":child,
                                                  "Транспорт": nameOfTransport,
                                                  "Адрес проживания":address
                                            }

        print('Новый словарь работников теперь выглядит так:')

        for worker, workerDict in myWorkerDict.items():
            print("===================")
            print(f'{worker}:\n'
                  f'===================')
            for key, values in workerDict.items():
                if key == "Дети":
                    #["Эсен", "Ураматов"]
                    workerNameList = workerDict["ФИО"].split(" ")
                    print(f'Дети {workerNameList[0]}а {workerNameList[1]}а : '
                          f'\n************************')

                    for child, childInfo in values.items():
                        print(f'{child}: {childInfo}')
                    print('************************')
                if key == "Дети":
                    continue
                print(f'{key}: {values}')

    elif option == 11:
        sumSalary = 0
        salaryList = []

        for worker, workerDict in myWorkerDict.items():
            salaryList.append(workerDict["Заработная плата"])

        print(f'Суммарная З-П всех сотрудников: {sum(salaryList)}')

    elif option == 14:
        for worker, workerDict in myWorkerDict.items():
            print("===================")
            print(f'{worker}:\n'
                  f'===================' )
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

    #0-14
    elif option not in (range(0,15)):
        print('Вы выбрали не правильную опцию! Попытайтесь заново!')





