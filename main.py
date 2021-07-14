import subprocess
import os
import time
import webbrowser


class callpy():
    def __init__(self, path, File, dir):
        self.File = File
        self.dir = dir
        self.path = path
    def call(self):
        os.chdir(self.path)
        if '.py' in (self.File):
            subprocess.call(f'python {self.File}')
    def localhost(self):
        webbrowser.open(f'http://localhost/dashboard/{self.dir}')

Base_dir = os.path.dirname(os.path.abspath(__file__))
# creating objects
signin = callpy(Base_dir, 'create_acct.py', '')
update_db_pt1 = callpy(Base_dir, 'delete.py', '')
update_db_pt2 = callpy(Base_dir,'insert.py', '')
login = callpy(Base_dir, 'ATM(db).py', '')
delete = callpy(Base_dir, 'dell.py', '')
while 1:
    try:
        print(490*'\n')
        print('''
---------------------------------------------------------WELLCOME TO XYZ BANK-------------------------------------------
            Do you have an existing account,
            Do you want to create one account,
            or you want to delete an account?
            
            
            '''
        )
        ask_yes_or_no = input('''
        Press ("1","s", "y") to sign in
        Press ("2","l","n") to log in
        Press ("3", "d") to delete an account\n=> ''')
        if ask_yes_or_no in ('1', 'S', 's', 'y', 'Y'):
            login.call()
            time.sleep(1)
            print(5000*'\n')
        elif ask_yes_or_no in ('2', 'l', 'L', 'n', "N"):
            signin.call()
            print('Updating database')
            update_db_pt1.call()
            time.sleep(0.5)
            update_db_pt2.call()
            time.sleep(0.5)
            print(500*'\n')
            print('Opening official website')
            time.sleep(3)
            signin.localhost()
            time.sleep(2)
            print(500*'\n')
            print('Loading...')
            time.sleep(3)
            login.call()
        elif ask_yes_or_no in ('3', 'd', 'D'):
            delete.call()
        else:
            print(500*'\n')
            time.sleep(3.8)
            print('You entered an invalid command')

    except Exception as e:
        print('Somthing went wrong\n trying to reconnect')
        time.sleep(5)
        print(100*'\n')
        print('Connection failed')
        time.sleep(5)
        print(52*'\n')
        print('Error')
        print('%s: %s'%(e.__class__.__name__, e))
        time.sleep(3)
    print(500*'\n')
