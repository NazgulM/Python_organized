import mysql.connector as mcon
from connectionInfo import infoconnection

mysqldb_info = infoconnection()
mycursor = mysqldb_info.cursor()

mycursor.execute("show databases;")
listDatabases = mycursor.fetchall()
print(listDatabases)

sqlCreateTable = """
    CREATE TABLE IF NOT EXISTS programmers2(
    id int,
    full_name varchar(100),
    age int,
    progLanguage varchar(50),
    salary double
    );
"""
mycursor.execute(sqlCreateTable)

# sqlInsert = """
#       INSERT INTO programmers(full_name, age, progLanguage, salary)
#       VALUES('Alicia Keys', 25,'Java', 14299.99),('Ashley Stanley', 28, 'C++', 15750.50);
# """
# mycursor.execute(sqlInsert)
# mysqldb_info.commit()
# print('Successfully inserted!')
# idNo = int(input('Please enter the id: '))
# full_name = input('Please enter the name to insert: ')
# age = int(input('Please enter the age: '))
# progLanguage = input('Please enter the programming language: ')
# salary = float(input('Please enter the salary: '))
# sqlInsert = """
#         INSERT INTO programmers2(id, full_name, age, progLanguage, salary)
#         VALUES(%s, %s, %s, %s, %s);
#         """
#
# mycursor.execute(sqlInsert,(idNo, full_name, age, progLanguage, salary))
# mysqldb_info.commit()
# print('Successfully inserted!')

# sqlUpdate = f"UPDATE programmers " \
#                 f"SET progLanguage = 'Typescript' " \
#                 f"where full_name = 'Alicia Keys'"
#
# mycursor.execute(sqlUpdate)
# mysqldb_info.commit()
# print('Successfully updated!')

sqlScript = f"""
    SELECT * FROM programmers
    WHERE progLanguage = 'Java';
    """

mycursor.execute(sqlScript)
result = mycursor.fetchall()

print('Result: ', result)
print('*'*20)
