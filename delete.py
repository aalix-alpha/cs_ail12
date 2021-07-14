import time
import mysql.connector as sql

try:
    mydb = sql.connect(host='localhost',
                user= 'root',
                passwd= '',
                database= 'python_projectes'
    )
    mycursor = mydb.cursor()
    mycursor.execute('delete from users where 1;')
    mydb.commit()


except Exception as e:
    print('Connection failed')
    print('reconnecting...')
    time.sleep(2)
    print('''Error
        %s; %s''' % (e.__class__.__name__, e))
    exit()