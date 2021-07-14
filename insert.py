import time
import os
import mysql.connector as sql

try:
    mydb = sql.connect(host='localhost',
                user= 'root',
                passwd= '',
                database= 'python_projectes'
        )
    mycursor = mydb.cursor()

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # succssfully connected to database and localhost.
    time.sleep(3)
    # creating values to insert into the table.
    syntax = '''
        INSERT INTO `users`(`Pin`, `Fullname`, `Phone_No`, `Age`, `Balance`, `Address`, `DOB`)
        VALUES ("%s", "%s", "%s", %d, "%s", "%s", "%s");
        '''
    values = []  # list to give data to placeholders
    with  open('users.txt') as f:
        for val in f:
            val = val.split('; ')
            if '\n' in val[-1] and (len(val)>1):
                val.pop(-1)
                val[3] = int(val[3])
                val[2] = '+91 '+ val[2]
                values.append(tuple(val))
    # Inserting values
        for value in range(len(values)):
            mycursor.execute(syntax%values[value])
            mydb.commit()

# Confirmation of submission
except Exception as e:
    print('Somthing went wrong\n trying to reconnect')
    time.sleep(5)
    print(100*'\n')
    print('Connection failed')
    time.sleep(5)
    print(52*'\n')
    print('Error')
    print('%s: %s'%(e.__class__.__name__, e))