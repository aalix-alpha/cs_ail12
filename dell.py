import mysql.connector as sql
import time
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

try:
    mydb = sql.connect(host='localhost',
                    user='root',
                    passwd='',
                    database='python_projectes'
    )
    
    mycursor = mydb.cursor()
    ask_name = input('Plese Enter your name:  ')
    ask_pin = input('Please enter your pin:  ')
    mycursor.execute(f'DELETE FROM users WHERE Pin="{ask_pin}"')
    mydb.commit()
    orgin, data, bals = [], [], []
    
    mycursor.execute('select * from `users` where 1;')
    
    for i in mycursor.fetchall():
        bals.append(i[4])
    
    with open('users.txt') as f:
        orgin.append(f.readlines()[0:2])
        lines = f.readlines()[2:]
        for det in lines:
            det = det.split('; ')
            det.pop()
            if ask_pin not in det:
                data.append(det)

        for i in range(len(data)):
            data[i][4] = bal[i][4]
            for val in range(len(data[i])):
                dat = ''
                dat += data[i][val]

    with  open('users.txt', 'w') as f:
        for i in orgin:
            f.write(i)
    time.sleep(3)
    print(500*'\n')
    print(f'{ask_name} your account successfully deleted')
    time.sleep(3)


except Exception as e:
    print('Somthing went wrong\n trying to reconnect')
    time.sleep(5)
    print(100*'\n')
    print('Connection failed')
    time.sleep(5)
    print(52*'\n')
    print('Error')
    print('%s: %s'%(e.__class__.__name__, e))
