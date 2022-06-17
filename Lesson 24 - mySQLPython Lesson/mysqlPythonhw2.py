import mysql.connector as mcon
from connectionInfo import infoconnection

mysqldb_info = infoconnection()
mycursor = mysqldb_info.cursor()

mycursor.execute("show databases;")
listDatabases = mycursor.fetchall()
print(listDatabases)


def showAllOrders():
    sqlSelectAll = """
        SELECT * FROM Orders_prod;
        """
    mycursor.execute(sqlSelectAll)

    # fetchall() - отображение всех результатов
    result = mycursor.fetchall()
    for i in result:
        print(i)


def showOrderByDate():
    sqlSelectDate = """
            SELECT * FROM Orders_prod
            where ord_date = '2012-10-05';
            """
    mycursor.execute(sqlSelectDate)
    # fetchall() - отображение всех результатов
    result = mycursor.fetchall()
    for i in result:
        print(i)


def insertOrder():
    cust_id = int(input('Please enter the customer id started from 30: '))
    salesman_id = int(input('Please enter salesman id started from 5004: '))
    purch_amount = float(input('Please enter purchase amount: '))
    ord_date = input('Please enter the date')
    delivery = input('Please enter Delivery cost is 30$: ')
    sqlInsert = f"""
        INSERT INTO Orders_prod (customer_id, salesman_id, purch_amount, ord_date, delivery) 
        VALUES (%s, %s, %s, %s, %s);
        """

    mycursor.execute(sqlInsert, (cust_id, salesman_id, purch_amount, ord_date, delivery))
    mysqldb_info.commit()
    print('Successfully inserted!')


def updateOrderById():
    amount = float(input('Please enter amount of purchase to update: '))
    cust_id = int(input('Please enter the customer id for updating: '))
    sqlUpdate = f"UPDATE Orders_prod " \
                f"SET purch_amount = {amount} " \
                f"where customer_id = {cust_id}"
    mycursor.execute(sqlUpdate)
    mysqldb_info.commit()
    print('Successfully updated!')


def deleteOrder():
    cust_id = int(input('Please input customer_id to delete: : '))
    sqlDelete = f"""
    DELETE FROM Orders_prod 
    where customer_id = '{cust_id}';
    """

    mycursor.execute(sqlDelete)
    mysqldb_info.commit()
    print('Successfully deleted!')


def main():
    menuText = """
        Welcome to the program!

        Menu:
        1. Show all orders
        2. Show orders by date of purchase
        3. Insert new order
        4. Update order by id
        5. Delete order by id

    """

    print(menuText)
    choiceMenu = int(input('Input menu option: '))

    if choiceMenu == 1:
        showAllOrders()
    elif choiceMenu == 2:
        showOrderByDate()
    elif choiceMenu == 3:
        insertOrder()
    elif choiceMenu == 4:
        updateOrderById()
    elif choiceMenu == 5:
        deleteOrder()



if __name__ == '__main__':
    main()
