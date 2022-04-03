

# Explanation 0
#
# There are 5 students in this class whose names and grades are assembled to build the
# following list:
#
# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41],
# ['Harsh', 39]]
#
# The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21
# belongs to both Harry and Berry, so we order their names alphabetically and
# print each name on a new line.
#
# Solution in Python3
# Beginner friendly solution with comments


#take value of n
no_of_students = int(input())
#create empty list
records = []
#append record of each student name,score in a for loop
for i in range(no_of_students):
    name = input()
    score = float(input())
    records.append([name, score])

#convert list of records to a python dictionary
# [['Harry', 37.21], ['Berry', 37.21]] becomes
# {'Harry': 37.21, 'Berry': 37.21}
records = dict(records)
#get only values from our dictionary and use set function to rmeove duplicate score then sort it in ascending order
scores = sorted(set(records.values()))
#index 1 has the 2nd lowest score
second_lowest_score = scores[1]
#create a list of names of students who has 2nd lowest score using list comprehension
second_lowest_students = [name for name,score in records if score==second_lowest_score]
#sort names in alphabetical order
second_lowest_students.sort()
#loop through each name and print
for name in second_lowest_students:
    print(name)

students = [[input(),float(input())] for i in range(int(input()))]
second_highest = sorted(set(j for i,j in students))[1]
print("\n".join(sorted(i for i,j in students if j==second_highest)))