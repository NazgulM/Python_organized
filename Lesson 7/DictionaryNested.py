# defining nested dictionary in python
myDict = {'student1': {'name': 'Bashir', 'age': 22},
     'student2': {'name': 'Kane', 'age': 12},
     'student3':{'name':'Nat', 'age': 13}}
# for loop to iterate through nested dictionary
for i, y in myDict.items():
    # printing keys of outer dictionary
    print("the info about ",i)
    # nested for loop
    for nested_value in y:
        # printing nested keys and values
        print(nested_value)
        print(y[nested_value])

Liverpool = {
    'Keepers':{'Loris Karius':1,'Simon Mignolet':2,'Alex Manninger':3},
    'Defenders':{'Nathaniel Clyne':3,'Dejan Lovren':4,'Joel Matip':5,'Alberto Moreno':6,'Ragnar Klavan':7,'Joe Gomez':8,'Mamadou Sakho':9}
}

for k,v in Liverpool.items():
    if k =='Defenders':
       print(v)