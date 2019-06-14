import mysql.connector

class database:
    
    def usertable:
        connection = mysql.connector.connect(user='username',password='pwd',host='127.0.0.1',database='shupaypal')
        if connection.is_connected():
            cursor = connection.cursor()
            # primary key for user table is user id column. it autoincrements by 835039. Identity is a property of the column
            insert_query = "insert into user(firstname,lastname) values('Tarun','Yagmur')"
            select_query = "select * from user where user_id = 835039"
            cursor.execute(insert_query)
            connection.commit()
            cursor.execute(select_query)
            results = cursor.fetchall()
            for row in results:
                print(row)
            cursor.close()
            connection.close()

    def Banktable:
        connection = mysql.connector.connect(user='username',password='pwd',host='127.0.0.1',database='shupaypal')
        if connection.is_connected():
            cursor = connection.cursor()
            # primary key for bank table is accountnumber column. it autoincrements by  21538090. Identity is a property of the column
            insert_query = "insert into bank (Accountnumber ,userid) values('21538090 ','835039')"
            select_query = "select * from bank where user_id = 835039"
            cursor.execute(insert_query)
            connection.commit()
            cursor.execute(select_query)
            results = cursor.fetchall()
            for row in results:
                print(row)
            cursor.close()
            connection.close()


    def Transactionstable:
        connection = mysql.connector.connect(user='username',password='pwd',host='127.0.0.1',database='shupaypal')
        if connection.is_connected():
            cursor = connection.cursor()
            # primary key for Transaction table is transactionnum column. it autoincrements by  TRNS4184950158. Identity is a property of the column
            insert_query = "insert into payment(transactionnum,userid) values('TRNS4184950158',' 835039')"
            select_query = "select * from payment where user_id = 835039"
            cursor.execute(insert_query)
            connection.commit()
            cursor.execute(select_query)
            results = cursor.fetchall()
            for row in results:
                print(row)
            cursor.close()
            connection.close()
