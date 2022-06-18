import mysql.connector as mcon
from connectionInfo import infoconnection

myssqldb_info = infoconnection()
mycursor = myssqldb_info.cursor()


def createView(viewName):
    country = input('Please enter the country: ')
    sqlCreateView = f"""
        CREATE VIEW {viewName}
        AS SELECT * FROM Djangolessons
        WHERE country = '{country}';
    """

    mycursor.execute(sqlCreateView)
    print('View created!')


def showInfoFromView(viewName):
    showDataSql = f"""
    SELECT * FROM {viewName};
    """

    mycursor.execute(showDataSql)
    result = mycursor.fetchall()
    for i in result:
        print(f'Student id: {i[0]}')
        print(f'Student name: {i[1]}')
        print(f'Student age: {i[2]}')
        print(f'Student country: {i[3]}')
        print('*'*20)


def main():
    viewName = input('Enter view name: ')

    # createView(viewName)
    showInfoFromView(viewName)


if __name__ == '__main__':
    main()
