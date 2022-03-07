hospital1 = set()
command = ''
while command != 'no':
    hospital1.add(input('Name of the doctor?: '))

    command = input('Continue?: ')
    if command =='no':
        print(hospital1)

hospital2 = set()
command = ''
while command != 'no':
    hospital2.add(input('Name of the doctor?: '))

    command = input('Continue?: ')
    if command == 'no':
        print(hospital2)

# function intersection()  - & -  peresechenie dannyh
sameDoctor = hospital1.intersection(hospital2)
print(f'same doctor: {sameDoctor}')

# union()
hospitalsJoins = hospital1.union(hospital2)
print(f'Two hospitals together: {hospitalsJoins}')

# difference() - ' - '
differenceHospitals1 = hospital1.difference(hospital2)
print(differenceHospitals1)
differenceHospitals2 = hospital2.difference(hospital1)

differenceHospitals3  = hospital1 - hospital2
print(differenceHospitals3)
differenceHospitals4 = hospital2 - hospital1

sumListNums  = list(range(15, 21))
print(sumListNums)