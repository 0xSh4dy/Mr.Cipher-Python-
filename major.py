# The ultimate python project to decode and encode various ciphers

# Input the mode
from nums import * 
class InputData:
    def __init__(self):
        self.num = nums()

    def getMode(self):
        self.modes = ['cipher','base64','hexadecimal','octal','binary','decimal','hash']
        print("Select the mode(must be the corresponding number)..")
        print("1. Cipher  2. base64   3. hexadecimal  4. octal  5. binary  6. decimal  7. Hash ")
        try:
            self.mode=int(input())
        except(Exception):
            print("The input value must be a number from 1 to 7")
            exit()
        print("Starting "+self.modes[self.mode-1]+ " mode")    

    def startSelectedMode(self):
        a = self.mode
        if a==1:
            pass
        elif a==2:
            pass
        elif a==3:
            pass
        elif a==4:
            pass
        elif a==5:
            pass
        elif a==6:
            myNum = self.num
            print("Enter a number from the following choices")
            try:
                mode = int(input("1. decimal to binary  2. decimal to octal  3. decimal to hexadecimal\n"))
                if mode<1 or mode >3:
                    print("Invalid input, try once again")
                    mode = int(input("1. decimal to binary  2. decimal to octal  3. decimal to hexadecimal\n"))
                    if mode<1 or mode>3:
                        print("Invalid input")
                        exit()
            except(Exception):
                print("Invalid input")
                exit()
            if mode==1:
                inp = int(input("Enter a decimal number to convert into binary\n"))
                try:
                    myNum.decToBin(inp)
                except(Exception):
                    print(Exception)
            elif mode==2:
                inp = int(input("Enter a decimal number to convert into octal\n"))
                try:
                    myNum.decToOct(inp)
                except(Exception):
                    print(Exception)
            elif mode==3:
                inp = int(input("Enter a decimal number to convert into binary\n"))
                try:
                    myNum.decToHex(inp)
                except(Exception):
                    print(Exception)
        elif a==7:
            pass


m = InputData()
m.getMode()
m.startSelectedMode()