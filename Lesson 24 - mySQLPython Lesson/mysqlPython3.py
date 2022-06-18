import mysql.connector as mcon
from connectionInfo import infoconnection

myssqldb_info = infoconnection()
mycursor = myssqldb_info.cursor()


def createView(viewName):
    sqlCreateView = f"""
        CREATE VIEW {viewName}
        AS SELECT customer_id, salesman_id, ord_date, purch_amount as 'Max order' 
        FROM Orders_prod
        WHERE purch_amount = (
        SELECT MAX(purch_amount) FROM Orders_prod
        );
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
        print(f'Salesman id: {i[0]}')
        print(f'Customer id: {i[1]}')
        print(f'Max order: {i[3]}')



def main():
    viewName = input('Enter view name: ')

    # createView(viewName)
    showInfoFromView(viewName)


if __name__ == '__main__':
    main()