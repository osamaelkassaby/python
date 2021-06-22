import pyautogui
import time
import keyboard
import random
import string
import pyperclip
import os


try:
    os.mkdir("passwrds")
except :
    print("HI user i'm found folder contains passwords")


#  def generate password 

def get_random_string(length):
    # With combination of lower and upper case
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    # print random string
    result =   result_str + str(random.randint(length,50))
    print(result) 
    f = open("passwrds/password_low.txt","a")
    f.write("password : " + result + " |  <|=|>  Time : " + time.ctime()+"\n")
    pyperclip.copy(result)
    f.close()


# def 2 

def get_random_string_mid(length):
    # With combination of lower and upper case
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    # print random string
    result = result_str +"@#*" +str(random.randint(200,300))
    print(result) 
    f = open("passwrds/password_mid","a")
    f.write("password : " + result + " |  <|=|> Time : " + time.ctime()+"\n")
    pyperclip.copy(result)
    f.close()


# def 3 
def get_random_string_hight(length):
    # With combination of lower and upper case
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    # print random string
    result = str(random.randint(100,200)) +result_str+"@#*" +str(random.randint(200,300))
    print(result) 
    f = open("passwrds/password_hight","a")
    f.write("password : " + result + " | <|=|> Time : " + time.ctime()+"\n")
    pyperclip.copy(result + "\n")
    f.close()

    # End def 


print("==================================================================")
print("(1) generate password low")
print("____________________________\n")
print("(2) generate password mid")
print("__________________________ \n")
print("(3) generate password hight")
print("__________________________ \n")
print("(4) insert password low")
print("__________________________ \n")
print("(5) insert password mid")
print("__________________________ \n")
print("(6) insert password hight")
print("==================================================================")

inp = input("SELECT number :   ")

if inp == "1":
    get_random_string(6)

elif inp == "2":
    get_random_string_mid(8)

elif inp == "3":
    get_random_string_hight(10)
elif inp == "4" :
    print("WAITE 5 second")
    time.sleep(5)
    pyautogui.typewrite("write your password")
elif inp == "5" :
    print("WAITE 5 second")
    time.sleep(5)
    pyautogui.typewrite("write your password")
elif inp == "6" :
    print("WAITE 5 second")
    time.sleep(5)
    pyautogui.typewrite("write your password")
# print(random.randint(0,30))

while True:
    if keyboard.is_pressed('f2'):
        pyautogui.typewrite("write your password")
        break
    elif keyboard.is_pressed('esc'):
        pyautogui.typewrite("write your password")
        break
    elif keyboard.is_pressed('ins'):
        pyautogui.typewrite("write your password")

