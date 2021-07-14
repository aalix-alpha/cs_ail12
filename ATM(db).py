from re import DEBUG
import mysql.connector as sql
import os
import datetime
import time
from  win32com.client import  Dispatch

def Alert(alaram):  # Alaram function
    engine = Dispatch(('Sapi.SpVoice'))
    engine.speak(alaram)

try:
    mydb = sql.connect(host='localhost',
                    user='root',
                    passwd='',
                    database='python_projectes'
    )
    mycursor = mydb.cursor()
    mycursor.execute('select * from users;')
    details = []
    pins = []
    yrr = datetime.datetime.now().strftime('%Y')
    today = datetime.datetime.now().strftime('%d-%m')
    update = """
            UPDATE `users` SET `Balance`= %s
            WHERE Pin="%s"
    """
    for i in mycursor.fetchall():
        details.append(i)
        pins.append(i[0])


    tries = 0
    while (tries<4):
        tri = tries + 1
        if ((tri)==4):
            Alert('Security Breached')
            break
        else:
            ask_pin = input('Please Enter your Pin:     ')
            print(500*'\n')
            if ask_pin in pins:
                for user in range(len(details)):
                    
                    list_details = list(details[user])
                    name = list_details[1]  # Name of user
                    phone  = str(list_details[2])# Phone number of user
                    phone_no = int(phone[4:12])
                    Phone = phone_no
                    age  = list_details[3]  # Age of user
                    balance  = list_details[4]  # Balance of user
                    address  = list_details[5]  # Address of user
                    
                    if ask_pin in (details[user]):
                        while 1:
                            print("""
--------------------------------------------------------WELLCOME TO XYZ BANK------------------------------------------------


                            Press 1 to check balance.
                            Press 2 to Add money.
                            Press 3 to Withdraw money.
                            Press 4 to exit. 


                            """)
                            choice = input("What do you want to to choose:\t")
                            print(500*'\n')
                            if (choice in ['1', '2', '3', '4']):
                                if (choice=='1'):
                                    print(f"""
                            WELLCOME TO XYZ BANK
                    
        Name:                                        {name}
        Age:                                         {age}
        Mobile:                                      {Phone}
        Address:                                     {address}
-----------------------------------------------------------------------------
        TOTAL BALANCE:                               {balance}
                                        """)
                                    time.sleep(5)
    # adding money
                                elif (choice=='2'):
                                    while 1:
                                        try:
                                            add_money = float(input('Enter money to add\n'))
                                        except ValueError:
                                            pass
                                        else:
                                            break
                                    balance  = float(balance) + add_money
                                    mycursor.execute(update%(str(balance),list_details[0]))
                                    mydb.commit()
                                    print('%.2f amount is added succsessfully,\nNew balance is %s'%(add_money,balance))
                                    time.sleep(5)
                                    
    # Withdraw money
                                elif (choice=='3'):
                                    if today==list_details[6]:
                                        mycursor.execute(f'update `users` set (age = age+1, Year=\'Year + "," + "{yrr}"\') where Year not in("{yrr}")')
                                        mydb.commit()
                                    else:
                                        if (age<18):
                                            print('You are not eligible to withdraw money')
                                            time.sleep(5)
                                        else:
                                            while 1:
                                                try:
                                                    withdraw_money = float(input('Enter money to withdraw\n'))
                                                except ValueError:
                                                    pass
                                                else:
                                                    break
                                            balance  = float(balance) - withdraw_money
                                            mycursor.execute(update%(str(balance),list_details[0]))
                                            mydb.commit()
                                            time.sleep(1)
                                            print('%.2f amount is withdrawed succsessfully,\nNew balance is %s'%(withdraw_money,balance))
                                            time.sleep(5)
                                
                                else:
                                    print('card is ejecting...')
                                    time.sleep(0)
                                    print('Thanks for coming')
                                    print(5000*"\n")
                                    time.sleep(15)
                                    break
                            restart = input('Do you want to Do other operations Press either 1 or y for yes and Press either 2 or n for No: ')
                            if (restart in ('1', 'Y', 'y')):
                                print('restarting...')
                                print(100*'\n')
                            elif (restart in ('2', 'N', 'n')):
                                print('card is ejecting...')
                                time.sleep(2)
                                print('Thanks for coming')
                                time.sleep(3)
                                break
                            else:
                                print('your input is invalid')
                                time.sleep(1)
                            print('\n'*500)
                break
            
            else:
                print('You entered an invalid Pin')
                time.sleep(2)
                print('You have %d more tries left to enter a valid pin'%(2-tries))
                tries += 1


except Exception as e:
    print('Somthing went wrong\n trying to reconnect')
    time.sleep(5)
    print(100*'\n')
    print('Connection failed')
    time.sleep(5)
    print(52*'\n')
    print('Error')
    print('%s: %s'%(e.__class__.__name__, e))
    time.sleep(5)
    exit()