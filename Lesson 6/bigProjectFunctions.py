def searchWorker(nameSearch):
    for worker, workerDict in myWorkerDict.items():
        for key, valueWorker in workerDict.items():
            if valueWorker == nameSearch:
                for key, valueWorker in workerDict.items():
                    print(key, valueWorker)


def addingWorker(nameInput, age, typeWork, salary, fioWifeHusb, child, nameOfTransport, address, countWorkerKey):
    myWorkerDict[countWorkerKey] = {"ФИО": nameInput,
                                    "Возраст": age,
                                    "Род деятельности": typeWork,
                                    "Заработная плата": salary,
                                    "ФИО Супруга/и": fioWifeHusb,
                                    "Дети": child,
                                    "Транспорт": nameOfTransport,
                                    "Адрес проживания": address
                                    }


def showWorkers():
    workerNameList = list()

    if len(myWorkerDict) != 0:
        for worker, workerDict in myWorkerDict.items():
            print("===================")
            print(f'{worker}:\n'
                  f'===================')
            for key, values in workerDict.items():
                if key == "Дети":
                    workerNameList = workerDict["ФИО"].split(" ")
                    print(f'Дети {workerNameList[0]}а {workerNameList[0]}а : '
                          f'\n************************')

                    for child, childInfo in values.items():
                        print(f'{child}: {childInfo}')
                    print('************************')
                if key == "Дети":
                    continue
                print(f'{key}: {values}')
    else:
        print('База сотрудников пуста!')


def delWorker(nameWorker):
    valDelete = None
    for worker, workerDict in myWorkerDict.items():
        for k, v in workerDict.items():
            if nameWorker in workerDict.values():
                valDelete = worker

    del myWorkerDict[valDelete]

    print(delWorker(nameWorker))


myWorkerDict = {
    "Сотрудник 1":

        {"ФИО": "Адилет Эшмаматов",
         "Возраст": 28,
         "Род деятельности": "Работник цеха",
         "Заработная плата": 25000,
         "ФИО Супруга/и": "Гульзада Саратова",
         "Дети": {"Ребенок 1": "Мухаммад Эшмаматов",
                  "Ребенок 2": "Элиза Эшмаматова"

                  },
         "Транспорт": "Тойота Камри 35",
         "Адрес проживания": "г. Бишкек, ул. Лев Толстой 77"

         },

    "Сотрудник 2":

        {"ФИО": "Эсен Урматов",
         "Возраст": 30,
         "Род деятельности": "Работник цеха",
         "Заработная плата": 31000,
         "ФИО Супруга/и": "Тамара Тиленова",
         "Дети": {"Ребенок 1": "Усон Урматов", },
         "Транспорт": "Хонда Фит",
         "Адрес проживания": "г. Бишкек, ул. Чуй 123"

         },

    "Сотрудник 3":

        {
            "ФИО": "Аселя Давлетова",
            "Возраст": 30,
            "Род деятельности": "Работник бухгалтерии",
            "Заработная плата": 42000, "ФИО Супруга/и":
            "Сергей Васильев",
            "Дети": {"Ребенок 1": "Елена Васильева",
                     "Ребенок 2": "Степан Васильев",
                     "Ребенок 3": "Марат Васильев", },
            "Транспорт": "БМВ X7",
            "Адрес проживания": "г. Бишкек, ул. Токтогула 76"
        },

    "Сотрудник 4":

        {
            "ФИО": "Мария Степанова",
            "Возраст": 29,
            "Род деятельности": "Работник маркетинга",
            "Заработная плата": 35000,
            "ФИО Супруга/и":
                "Олег Кичин", "Дети": {"Ребенок 1": "Василиса Кичина", },
            "Транспорт": "Пешком",
            "Адрес проживания": "г. Бишкек, мкр 7 дом 76, кв: 14"
        },

    "Сотрудник 5":
        {
            "ФИО": "Олег Иванов",
            "Возраст": 45,
            "Род деятельности": "Генеральный Директор",
            "Заработная плата": 70000,
            "ФИО Супруга/и": "Светлана Валерьева",
            "Дети": {"Ребенок 1": "Григорий Иванов",
                     "Ребенок 2": "Наталья Иванова",
                     "Ребенок 3": "Василий Иванов",
                     "Ребенок 4": "Филип Иванов", },
            "Транспорт": "БМВ X7",
            "Адрес проживания": "г. Бишкек, мкр 5 дом 16, кв: 102"
        },
}

# Task 1:

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
        searchWorker(nameSearch)
    elif option == 2:
        nameInput = input('Вы выбрали меню №2.'
                          '\nНапишите ФИО Сотрудника для добавления: ')
        age = int(input('Возраст: '))
        typeWork = input('Род деятельности: ')
        salary = int(input('Напишите зарплату: '))
        fioWifeHusb = input('Напишите имя супруга/и: ')
        quantChild = int(input('Кол-во детей: '))
        child = {}
        # 3 - range(3) - 0,1,2
        for i in range(quantChild):
            childKey = 'Ребенок ' + str(i + 1)
            child[childKey] = input(f'Пожалуйста введите '
                                    f'имя для {i + 1} ребенка: ')

        nameOfTransport = input('Название транспорта: ')
        address = input('Адрес проживания: ')

        countWorker = len(myWorkerDict) + 1
        countWorkerKey = 'Сотрудник ' + str(countWorker)
        addingWorker(nameInput, age, typeWork, salary, fioWifeHusb, child, nameOfTransport, address, countWorkerKey)

        print('Новый словарь работников теперь выглядит так:')

        showWorkers()

    elif option == 3:
        nameWorker = input('Вы выбрали меню "Удаление сотрудника"\n'
                           'Напишите имя сотрудника для удаления: ')

        print('\nНовый словарь работников теперь выглядит так:')


    elif option == 4:
        listWorkerAwarded = []
        cannotFindAwarded = []
        numberAwarded = int(input('Сколько сотрудников вы планируете наградить? '))

        for i in range(numberAwarded):
            nameAward = input('Напишите имя сотрудника для награждения: ')
            for worker, workerDic in myWorkerDict.items():
                if nameAward == workerDic["ФИО"]:
                    listWorkerAwarded.append(nameAward)
                # else:
                #     print('Не смогли найти')
                #     continue

            print('Сотрудники для награждения: ')
            counter = 1

            for worker in listWorkerAwarded:
                print(f'Имя {counter} - го сотрудника для награды: {worker}')
                counter += 1

            print('Мы не смогли найти следующих сотрудников: ')
            counter += 1

            for i in cannotFindAwarded:
                print(f'Имя {counter} - го сотрудника который  не был найден: {i}')
    elif option == 5:
        listWorkerRest = []
        cannotFindRest = []
        numberRest = int(input('Сколько сотрудников собираются в отпуск? '))

        for i in range(numberRest):
            nameRest = input('Напишите имя сотрудника для отпуска: ')
            for worker, workerDict in myWorkerDict.items():
                if nameRest == workerDict["ФИО"]:
                    listWorkerRest.append(nameRest)

        print('Сотрудники которые выходят в отпуск: ')
        counter = 1
        for worker in listWorkerRest:
            print(f'Имя {counter} - го сотрудника в отпуск: {worker}')
            counter += 1

        print('Мы не смогли найти следующих сотрудников: ')

        for i in cannotFindRest:
            print(f'Имя {counter} - го сотрудника который  не был найден: {i}')

    elif option == 6:
        nameIncreaseSalary = input('Вы выбрали меню "Повышение ЗП сотрудника"\n'
                                   'Напишите имя сотрудника для повышения ЗП: ')
        increaseSalary = int(input('Напишите сумму, на которую хотите повысить ЗП: '))
        valIncrease = None
        for worker, workerDict in myWorkerDict.items():
            for k, v in workerDict.items():
                if nameIncreaseSalary in workerDict.values():
                    valIncrease = worker

        myWorkerDict[valIncrease]["Заработная плата"] = myWorkerDict[valIncrease]["Заработная плата"] + increaseSalary

        print(
            f'Новая ЗП Сотрудника: {myWorkerDict[valIncrease]["ФИО"]}: {myWorkerDict[valIncrease]["Заработная плата"]}')
    elif option == 7:
        nameDecreaseSalary = input('Вы выбрали меню "Понижение ЗП сотрудника"\n'
                                   'Напишите имя сотрудника для понижения ЗП: ')
        decreaseSalary = int(input('Напишите сумму, на которую хотите понизить ЗП: '))
        valDecrease = None
        for worker, workerDict in myWorkerDict.items():
            for k, v in workerDict.items():
                if nameDecreaseSalary in workerDict.values():
                    valDecrease = worker

        myWorkerDict[valDecrease]["Заработная плата"] = myWorkerDict[valDecrease]["Заработная плата"] - decreaseSalary

        print(
            f'Новая ЗП Сотрудника: {myWorkerDict[valDecrease]["ФИО"]}: {myWorkerDict[valDecrease]["Заработная плата"]}')
    elif option == 8:
        salaryList = []
        for worker, workerDict in myWorkerDict.items():
            salaryList.append(workerDict["Заработная плата"])

        maxSalary = max(salaryList)
        nameWorkerMaxSalary = " "

        for worker, workerDict in myWorkerDict.items():
            if workerDict["Заработная плата"] == maxSalary:
                nameWorkerMaxSalary = workerDict["ФИО"]

        print(f'Имя сотрудника с Максимальной ЗП: {nameWorkerMaxSalary}')
    elif option == 9:
        salaryList = []
        for worker, workerDict in myWorkerDict.items():
            salaryList.append(workerDict["Заработная плата"])

        minSalary = min(salaryList)
        nameWorkerMinSalary = " "

        for worker, workerDict in myWorkerDict.items():
            if workerDict["Заработная плата"] == minSalary:
                nameWorkerMinSalary = workerDict["ФИО"]

        print(f'Имя сотрудника с Минимальной ЗП: {nameWorkerMinSalary}')
    elif option == 10:
        sumSalary = 0
        salaryList = []
        for worker, workerDict in myWorkerDict.items():
            salaryList.append(workerDict["Заработная плата"])

        print(f'Среднемесячная З-П всех сотрудников: {sum(salaryList) / len(salaryList)}')

    elif option == 11:
        sumSalary = 0
        salaryList = []
        for worker, workerDict in myWorkerDict.items():
            salaryList.append(workerDict["Заработная плата"])

        print(f'Суммарная З-П всех сотрудников: {sum(salaryList)}')
    elif option == 12:
        transportTypeList = []
        for worker, workerDict in myWorkerDict.items():
            if workerDict["Транспорт"] == "Пешком":
                continue

            transportTypeList.append(workerDict["Транспорт"])

        transportTypeList = list(set(transportTypeList))

        print('Уникальные транспорты всех сотрудников: ')
        counter = 1
        for transport in transportTypeList:
            print(f'Транспорт {counter}: {transport}')
            counter += 1

    elif option == 13:
        print('Вы выбрали меню №13 - Отображение кол-ва и имен всех детей сотрудников')
        listOfChild = []
        for worker, workerDict in myWorkerDict.items():
            if workerDict['Дети']:
                for k, v in workerDict['Дети'].items():
                    listOfChild.append(v)

        print(f'Общее кол-во детей сотрудников: {len(listOfChild)}')
        print('Дети: ')

        counter = 1
        for child in listOfChild:
            print(f'Ребенок {counter}: {child}')
            counter += 1

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

    elif option not in (range(0, 15)):
        print('Вы выбрали не правильную опцию! Попытайтесь заново!')
