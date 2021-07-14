import time
import datetime
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

encrypting_values = {'a':'42=?X', 'b':'54f#@', 'c':'89*D%', 'e':'x^l89', 'f':'94/*@!', 'g':'89$gX',
                'h':'Qw2@j', 'i':'Lk9*1', 'j':'+09Po', 'k':'kl89*', 'l':'oi&89', 'm':'rg6&7',
            'n':'pi&u2', 'o':'Ja@$4', 'p':'Op*6k', 'q':'.- P6', 'r':'Mi+t2', 's':'Mak2@', 
        't':'Abs2#', 'u':'Bg@23', 'v':'34$Ty', 'w':'Rst%5', 'x':'a. st', 'y':'A @13',
    'z':'Stu=5', 'Z':'Tus+5', ' ':'8S8h&', '  ':'4+sCf', '   ':'k<j0*', '    ':'Q2/\n',
    '\n':'Hj)\n', '\t':'Aw4$1', '\'':'1oiU&*', '\"':'jJ22@', '\r':'Bc2@1', '@':'wh8@2',
        '#':'LjK8&', '!':'DfD#4', '`':'JuK&5', '~':r'VX5%c', '$':'reT5%', '%':'r+4\n',
            '^':'xzV$4', '*':'Aw2@2', '&':'>x3#G', '+':'09*Hh', '-':'/.Hh6', '_':'0*lKJ',
                '=':'Z@x34', '/':'rS4$J', '?':'T0+yz', '<':'aS7&P', '>':'Vv@31', ',':'cx+09',
                    '.':'Aas!1', ':':'Ssd@2', ';':'T3#t5', '0':'B7b&n', '1':'Nm8*8', '2':'M*yu6',
                    'd':'Zzx@2', '3':'Xxc#3', '4':'Ccv$4', '5':'Vvb&7', '6':'Bbn*8', '7':'Nnm(9',
                '8':'Ssd%5', '9':'Nn5#1', '10':'Rrs&2', '11':'Jjt^5', '100':'Aas)1', '101':'Zzx$2',
            'A':'t@7', 'B':'89D&J', 'C':'J*K8x', 'D':'852!D', 'E':'82d#!', 'F':'k8)45',
        'G':'As#$q', 'H':'!t7%9', 'I':'8/#sA', 'J':'59-+@', 'K':'23&lM', 'L':'E5&s9',
    'M':'A3$$q', 'N':'!t6^9', 'O':'//#sA', 'P':'59l+@', 'Q':'89&lM', 'R':'So&s9',
        'S':'Sd&89', 'T':'F9*r5', 'U':'85$lD', 'V':'4S#59', 'W':r'8%56aA',
            'X':'89!zW', 'Y':r'*94%sX','(':'85@45', ')':'85^kz', "\\":'Qwe4@', '|':'@fg28',
                1:'h65$$', 2:r'L82%$', 3:'**gFk', 4:r'vb@s9', 5:'a-_-s', 6:r'|abc|', 7:r'<\s/>', 8:'op(a)', 9:'/+Sx$', 0:'l>>8X'
}
# asking details
Year = datetime.datetime.now().strftime('%Y')
Name = input('Enter your name:  ')
time.sleep(1)
Mobile = input('Enter your mobile phone number(+91):  ')
time.sleep(1)
age = input('Enter your age: ')
DoB = input('Enter your date of birth:  ')
time.sleep(1)
Address = input('Enter your address\n=> ')
time.sleep(1)
bal = input('Enter Amount to add to create an account\n=> ')
# converting values
encrypt_name = encrypting_values[Name[0]]
encrypt_mob = encrypting_values[Mobile[0]]
encrypt_dob = encrypting_values[DoB[0]]
encrypt_add = encrypting_values[Address[0]]
# gaining values to generate a pin 
gen_pin_name = encrypt_name[1]
gen_pin_mob = encrypt_mob[1]
gen_pin_bday = encrypt_dob[1]
gen_pin_add =  encrypt_add[1]
pin = f'{gen_pin_add}{gen_pin_bday}{gen_pin_mob}{gen_pin_name}'  # pin is created
# (`Pin`,`Fullname`,`Phone_No`,`Age`,`Balance`,`Addres`,`DOB`,`Year`)
print('Loading...')
time.sleep(5)
print(500*'\n')
with open('users.txt', 'a') as f:
    f.write(f'{pin}; {Name}; {Mobile}; {age}; {str(float(bal) - float(bal)*0.083)}; {Address}; {DoB[0:5]}; \n')
print(f"Your pin in {pin}")
