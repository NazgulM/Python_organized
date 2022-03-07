hospital1 = {'Yuliya', 'Timur', 'Alexey', 'Murat'}
hospital2 = {'Bolot', 'Adilet', 'Murat', 'Askar'}

mainHospital1 = {'Yuliya', 'Timur', 'Alexey', 'Murat', 'Aslan', 'Adilet', 'Aisuluu'}
mainHospital12 = {'Kadyr', 'Guldana', 'Alena', 'Bolot', 'Adilet', 'Murat', 'Askar'}

print(hospital1.issubset(mainHospital1)) #True
print(mainHospital1.issuperset(hospital1))

print(hospital1.issuperset(mainHospital1))
print(mainHospital1.issuperset(hospital1))

# Frozenset
cannotChangeSet = frozenset(hospital1)
print(cannotChangeSet)

sumListNums  = list(range(15, 21))
print(sumListNums)

setNums = {15, 43, 20, 4}
setNums.update(sumListNums)
print(setNums)