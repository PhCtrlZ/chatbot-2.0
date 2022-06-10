from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from datetime import date
from datetime import datetime
import pyautogui
import subprocess,json,time
import requests
import ctypes   
import winshell
from colorama import Fore, Back, Style
import socket
from tkinter import messagebox
import sys

os.system("cls")
print(Fore.GREEN+"đang checking kết nối mạng")
try:
    requests.get('https://www.google.com/').status_code
    print(Fore.GREEN+"Connected to internet is successfully")
    pass
except:
    messagebox.showerror("Thông báo","vui lòng kiểm tra lại đường truyền internet")
    time.sleep(5)
    sys.exit ()

b ="sever"
r = requests.get('https://api.npoint.io/365dfdd4fe77a000f2d2')
r = json.loads(r.text)
start = "\033[1m"
end = "\033[0;0m"

try:
    with open('key.txt', 'r' ,encoding='UTF-8') as f:
            datalist = f.readlines() 
            key = datalist[1]
    if key == r[b]:
        mess=r['message']
        print(Fore.GREEN+start+mess+end)
        print(Fore.GREEN+start+"Connected to sever is successfully"+end)
        time.sleep(1)
        print("Sever sẽ đóng vào 12h->7h30 sáng để bảo trì")
        time.sleep(1)
        path = 'sent.vbs'
        if os.path.isfile(path):
            os.remove(path)
        path_w = 'sent.vbs'
        with open('user.txt', 'r' ,encoding='UTF-8') as f:
            datalist = f.readlines() 
            d = datalist[1]
        if d=="":
            messagebox.showerror("Lỗi,ko có thông tin tài khoản")
            sys.exit ()
        with open('pass.txt', 'r' ,encoding='UTF-8') as f:
            datalist = f.readlines() 
            e = datalist[1]
        if e=="":
            messagebox.showerror("Lỗi,ko có thông tin mật khẩu")
            sys.exit ()
        with open('text.txt', 'r' ,encoding='UTF-8') as f:
            datalist = f.readlines() 
            u = datalist[1]
        if u=="":
            messagebox.showerror("Lỗi,ko có thông tin tin nhắn")
            sys.exit ()
        with open('time.txt', 'r' ,encoding='UTF-8') as f:
            datalist = f.readlines() 
            c = datalist[1]
        if d=="":
            messagebox.showerror("Lỗi,ko có thông tin thời gian")
            sys.exit ()
        with open('linkfb.txt', 'r' ,encoding='UTF-8') as f:
            datalist = f.readlines() 
            n = datalist[1]
            n=n.strip("https://www.facebook.com/messages/t/")
        if d=="":
            messagebox.showerror("Lỗi,ko có thông tin link facebook")
            sys.exit ()

        LOGIN_URL = 'https://www.facebook.com/messages/t/'+n
        s="""Set WshShell = WScript.CreateObject("WScript.Shell")\nstrName = wshShell.ExpandEnvironmentStrings( "%USERNAME%" )\n"""""
        with open(path_w, mode='a') as f:
            f.write(s)
        for i in u:
            if i==" ":
                s="""WScript.sleep 200
        Wshshell.sendkeys" " \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ê":
                s="""WScript.sleep 200
        Wshshell.sendkeys"ee" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="q":
                s="""WScript.sleep 200
        Wshshell.sendkeys"q" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="a":
                s="""WScript.sleep 200
        Wshshell.sendkeys"a" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ă":
                s="""WScript.sleep 200
        Wshshell.sendkeys"aw" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="â":
                s="""WScript.sleep 200
        Wshshell.sendkeys"aa" \n"""""   
                with open(path_w, mode='a') as f:
                    f.write(s)   
            if i=="b":
                s="""WScript.sleep 200
        Wshshell.sendkeys"b" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="c":
                s="""WScript.sleep 200
        Wshshell.sendkeys"c" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="d":
                s="""WScript.sleep 200
        Wshshell.sendkeys"d" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="đ":
                s="""WScript.sleep 200
        Wshshell.sendkeys"đ" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="e":
                s="""WScript.sleep 200
        Wshshell.sendkeys"e" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="g":
                s="""WScript.sleep 200
        Wshshell.sendkeys"g" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="h":
                s="""WScript.sleep 200
        Wshshell.sendkeys"h" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="i":
                s="""WScript.sleep 200
        Wshshell.sendkeys"i" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="k":
                s="""WScript.sleep 200
        Wshshell.sendkeys"k" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="l":
                s="""WScript.sleep 200
        Wshshell.sendkeys"l" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="m":
                s="""WScript.sleep 200
        Wshshell.sendkeys"m" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="n":
                s="""WScript.sleep 200
        Wshshell.sendkeys"n" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ô":
                s="""WScript.sleep 200
        Wshshell.sendkeys"oo" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="o":
                s="""WScript.sleep 200
        Wshshell.sendkeys"o" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ơ":
                s="""WScript.sleep 200
        Wshshell.sendkeys"ow" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="p":
                s="""WScript.sleep 200
        Wshshell.sendkeys"p" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="q":
                s="""WScript.sleep 200
        Wshshell.sendkeys"q" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="r":
                s="""WScript.sleep 200
        Wshshell.sendkeys"r" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="s":
                s="""WScript.sleep 200
        Wshshell.sendkeys"s" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="t":
                s="""WScript.sleep 200
        Wshshell.sendkeys"t" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="u":
                s="""WScript.sleep 200
        Wshshell.sendkeys"u" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="v":
                s="""WScript.sleep 200
        Wshshell.sendkeys"v" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="x":
                s="""WScript.sleep 200
        Wshshell.sendkeys"x" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="y":
                s="""WScript.sleep 200
        Wshshell.sendkeys"y" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ò":
                s="""WScript.sleep 200
        Wshshell.sendkeys"of" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="á":
                s="""WScript.sleep 200
        Wshshell.sendkeys"as" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ả":
                s="""WScript.sleep 200
        Wshshell.sendkeys"ar" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ã":
                s="""WScript.sleep 200
        Wshshell.sendkeys"ax" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ạ":
                s="""WScript.sleep 200
        Wshshell.sendkeys"aj" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="è":
                s="""WScript.sleep 200
        Wshshell.sendkeys"ef" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="é":
                s="""WScript.sleep 200
        Wshshell.sendkeys"es" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ẻ":
                s="""WScript.sleep 200
        Wshshell.sendkeys"er" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ẽ":
                s="""WScript.sleep 200
        Wshshell.sendkeys"ex" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ẹ":
                s="""WScript.sleep 200
        Wshshell.sendkeys"ẹ" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ỳ":
                s="""WScript.sleep 200
        Wshshell.sendkeys"yf" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ý":
                s="""WScript.sleep 200
        Wshshell.sendkeys"ys" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ỷ":
                s="""WScript.sleep 200
        Wshshell.sendkeys"yr" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ỹ":
                s="""WScript.sleep 200
        Wshshell.sendkeys"yx" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ỵ":
                s="""WScript.sleep 200
        Wshshell.sendkeys"yj" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ổ":
                s="""WScript.sleep 200
        Wshshell.sendkeys"oor" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
        s="""WScript.sleep 200
        Wshshell.sendkeys"{enter}" """""
        with open(path_w, mode='a') as f:
            f.write(s)

        while True:
            now= datetime.now()
            a=now.strftime("%m-%d-%Y %T:%p")
            b=str(a)
            if b==c:
                print("khởi động chế độ tự động nhắn")
                print("===== Admin Login Facebook =====")
                class FacebookLogin():
                    def __init__(self, email, password, browser='Chrome'):
                        # Store credentials for login
                        self.email = email
                        self.password = password
                        if browser == 'Chrome':
                            # Use chrome
                            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
                        self.driver.get(LOGIN_URL)
                        time.sleep(1) # Wait for some time to load
                 
                 

                    def login(self):
                        email_element = self.driver.find_element_by_id('email')
                        email_element.send_keys(self.email) # Give keyboard input
                 
                        password_element = self.driver.find_element_by_id('pass')
                        password_element.send_keys(self.password) # Give password as input too
                 
                        login_button = self.driver.find_element_by_id('loginbutton')
                        login_button.click() # Send mouse click
                        print("[+] Login successfully")
                        time.sleep(15)
                        for _ in range(2):
                            pyautogui.click(542,680)

                        os.startfile('sent.vbs')
                        time.sleep(2) # Wait for 2 seconds for the page to show up
                        sys.exit()
                if __name__ == '__main__':
                    # Enter your login credentials here
                    #fb_login = FacebookLogin(email='100074258102022', password='0914220047', browser='Chrome')
                    fb_login = FacebookLogin(email=d, password=e, browser='Chrome')
                    fb_login.login()
                    


    

    elif key != r[b]:
        os.system("cls")
        messagebox.showerror("Lỗi","key sai vui lòng liên hệ với nhà phát hành")
        time.sleep(10)
        sys.exit()

except:
    os.system("cls")
    error=r['error']
    error2=r['error2']
    error3=r['error3']
    print(Fore.RED+error)
    print(Fore.RED+error2)
    print(Fore.RED+error3)
    print(Style.RESET_ALL)
    time.sleep(10)
    sys.exit()
 