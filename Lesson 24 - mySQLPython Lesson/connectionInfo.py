import mysql.connector as mcon


def infoconnection():
    mysqldb_info = mcon.connect(
        host="localhost",
        user="mysqlPython",
        password="nurbakar2022",
        database="mySQLLesson"
    )
    return mysqldb_info


if __name__ == '__main__':
    pass
