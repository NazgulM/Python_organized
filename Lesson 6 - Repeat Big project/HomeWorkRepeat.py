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

# print(myWorkerDict)

# for key, value in myWorkerDict.items():
#     print(key, value)
choice = ''
while choice != 0:
    choice = int(input('Your choice please: '))
    if choice == 1:
        print('You choose:  Поиск сотрудника')
        name = (input('Please input the name of employee for searching: '))
        print(myWorkerDict['Employee 1'])
    if choice == 2:
        print('You choose option: "Adding new Employee" ')
        print('For adding info about new employee, please add following information: ')
        myWorkerDict['Employee 6'] = {}
        fullName = input('Please input full name of new employee: ')
        myWorkerDict['Employee 6']['Full name'] = fullName
        age = int(input('Please input age: '))
        myWorkerDict['Employee 6']['Age'] = age
        occupation = input('Please enter the occupation: ')
        myWorkerDict['Employee 6']['Occupation'] = occupation
        salary = int(input('Please input the salary: '))
        myWorkerDict['Employee 6']['Salary'] = salary
        spouseName = input('Please enter the full name of spouse: ')
        myWorkerDict['Employee 6']['Full name of spouse'] = spouseName
        children = int(input('Please enter the number of children: '))
        myWorkerDict['Employee 6']['Children'] = children
        kid = input('Please enter name of a kid: ')
        myWorkerDict['Employee 6']['Children'] = {'Kid 1': kid}
        transport = input('Please enter the type and model of your transport:  ')
        myWorkerDict['Employee 6']['Transport'] = transport
        address = input('Please enter the address: ')
        myWorkerDict['Employee 6']['Living address'] = address
        print(myWorkerDict['Employee 6'])
    if choice == 3:
        print('You choose option: "Delete of employee"')
        print(input('Please enter employee name for deletion the collection >>> '))
        print('Employee with name Adilet Eshmamatov was deleted')
        del myWorkerDict['Employee 1']
        print('Now collection with employees looks like that: ', myWorkerDict)
    if choice == 4:
        print('You choose: "Create a list to reward employees"')
        n = int(input('How many person will be rewarded?: >>> '))
        list1 = []
        for i in range(n):
            element = input('Please enter name of employee No.1 to reward: >>> ')
            list1.append(element)
            element2 = input('Please enter name of employee No.2 to reward: >>> ')
            list1.append(element2)
            element3 = input('Please enter name of employee No.3 to reward: >>> ')
            list1.append(element3)
            if element and element2 and element3 not in myWorkerDict.values():
                print('This employee does not exist')
            print('Here is the list of employees to reward: ', list1)
            break
    if choice == 5:
        print('You choose: "Create a list of employees to reward (set)"')
        s = int(input('How many person will be rewarded?: >>> '))
        set1 = set()
        for j in range(s):
            person1 = input('Please enter name of employee No.1 to reward: >>> ')
            set1.add(person1)
            person2 = input('Please enter name of employee No.2 to reward: >>> ')
            set1.add(person2)
            person3 = input('Please enter name of employee No.3 to reward: >>> ')
            set1.add(person3)
            if person1 or person2 or person3 not in myWorkerDict.values():
                print('This employee does not exist in the system.')
            print('Here is the list of employees to reward: ', set1)
            break
    if choice == 6:
        print('You choose: Increasing salary for employee')
        empIncr = input('Please enter name of employee, to whom you are going to increase salary: ')
        print('The employee ', empIncr, 'has a salary of ', myWorkerDict['Employee 5']['Salary'])
        salIncr = int(input('How much do you want to raise salary?: '))
        myWorkerDict['Employee 5']['Salary'] += salIncr
        print('Updated salary of ', empIncr, 'is: ', myWorkerDict['Employee 5']['Salary'])
        print('Updated collection of the employees now looks like: ', myWorkerDict)
    if choice == 7:
        print('You choose decreasing the salary for employee')
        empDec = input('Please enter name of employee, to whom you are going to decrease salary: ')
        salDecr = int(input('How much do you want to raise salary?: '))
        myWorkerDict['Employee 2']['Salary'] -= salDecr
        print('Updated salary of', empDec, 'is: ', myWorkerDict['Employee 2']['Salary'])
        print('Updated collection of the employees now looks like: ', myWorkerDict)
    if choice == 8:
        print('You choose: "Display employee name, receiving the maximum of salary"')
        list1 = [myWorkerDict['Employee 1']['Salary'], myWorkerDict['Employee 2']['Salary'],
                 myWorkerDict['Employee 3']['Salary'], myWorkerDict['Employee 4']['Salary'],
                 myWorkerDict['Employee 5']['Salary']]
        # list1 = list(map(int, str(list1)))
        print('The name of the employee, that receives max salary: ', myWorkerDict['Employee 5']['Full name'],
              'and his salary is: ', max(list1), ' RUB')
    if choice == 9:
        print('You choose: "Display employee name, receiving the minimum of salary"')
        list2 = [myWorkerDict['Employee 1']['Salary'], myWorkerDict['Employee 2']['Salary'],
                 myWorkerDict['Employee 3']['Salary'], myWorkerDict['Employee 4']['Salary'],
                 myWorkerDict['Employee 5']['Salary']]
        print('The name of the employee, that receives min salary: ', myWorkerDict['Employee 1']['Full name'],
              'and his salary is: ', min(list2), ' RUB')
    if choice == 10:
        print('You choose: "Calculate of the average monthly salary of employees"')
        list3 = [myWorkerDict['Employee 1']['Salary'], myWorkerDict['Employee 2']['Salary'],
                 myWorkerDict['Employee 3']['Salary'], myWorkerDict['Employee 4']['Salary'],
                 myWorkerDict['Employee 5']['Salary']]
        average_salary = sum(list3)/len(list3)
        print('Average sum of employees salary: ', average_salary)
    if choice == 11:
        print('You choose: Total salary of all employees')
        list4 = [myWorkerDict['Employee 1']['Salary'], myWorkerDict['Employee 2']['Salary'],
                 myWorkerDict['Employee 3']['Salary'], myWorkerDict['Employee 4']['Salary'],
                 myWorkerDict['Employee 5']['Salary']]
        sumSalary = sum(list4)
        print('Total sum  of all employees salary: ', sumSalary)
    if choice == 12:
        print('You choose: "Type of transport of all employees"')
        list5 = [myWorkerDict['Employee 1']['Transport'], myWorkerDict['Employee 2']['Transport'],
                 myWorkerDict['Employee 3']['Transport'], myWorkerDict['Employee 4']['Transport'],
                 myWorkerDict['Employee 5']['Transport']]
        for index, car in enumerate(list5, 1):
            if 'Walking' not in car:
                print(f'{index} transport is: {car}')
    if choice == 13:
        print('You choose: "Display the names and number of children of all employees"')
        list6 = [myWorkerDict['Employee 1']['Children']['Kid 1'],
                 myWorkerDict['Employee 1']['Children']['Kid 2'],
                 myWorkerDict['Employee 2']['Children']['Kid 1'],
                 myWorkerDict['Employee 3']['Children']['Kid 1'],
                 myWorkerDict['Employee 3']['Children']['Kid 2'],
                 myWorkerDict['Employee 3']['Children']['Kid 3'],
                 myWorkerDict['Employee 4']['Children']['Kid 1'],
                 myWorkerDict['Employee 5']['Children']['Kid 1'],
                 myWorkerDict['Employee 5']['Children']['Kid 2'],
                 myWorkerDict['Employee 5']['Children']['Kid 3'],
                 myWorkerDict['Employee 5']['Children']['Kid 4']]
        print(list6)
        print('Total number of children of the employees: ', len(list6), ' kids')
        for index, kid in enumerate(list6, 1):
            print(f'{index} kid : {kid}')
    if choice == 0:
        print('You have completed the program. See you soon!')

