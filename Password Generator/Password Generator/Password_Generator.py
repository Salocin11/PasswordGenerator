#Python 3.8 
#Future improvements: Changable length, GUI
import random 
class Password(object):
    def __init__(self, username): 
        Password.username = username
        Password.cletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        Password.sletters = "abcdefghijklmnopqrstuvwxyz"
        Password.num = "0123456789"
        Password.schar = "!@#$%^&*+=?"

    def passwordgenerate(self):
        #Requirements: minimum 2 upper, 2 lower, 2 nums and 1 special character. 15 characters long
        while True:
            pw = ""
            for i in range(15):
                x = random.randint(0,3)
                if x ==0:
                    pw += Password.cletters[random.randint(0,25)]

                elif x ==1:
                    pw += Password.sletters[random.randint(0,25)]

                elif x==2:
                    pw += Password.num[random.randint(0,9)]
                elif x==3:
                    pw += Password.schar[random.randint(0,10)]
            Password.pw = pw
            if Password.passwordcheck() == True:
                break
            else:
                pass

    def passwordcheck():
        cletter = 0
        sletter = 0
        num = 0
        schar = 0 
        for i in range(15):
            if Password.pw[i] in Password.cletters:
                cletter += 1
            elif Password.pw[i] in Password.sletters:
                sletter += 1
            elif Password.pw[i] in Password.num:
                num += 1
            elif Password.pw[i] in Password.schar:
                schar += 1
        if cletter < 2 or sletter < 2 or num < 2 or schar < 2:
            return False 
        else:
            return True

newpass = Password("John")
newpass.passwordgenerate()
print(newpass.pw)

        

    
