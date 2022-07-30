from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from tkinter import ttk, filedialog ,messagebox
from os import walk
import requests
import json
from tkinter import *
from tkinter.ttk import *

def login(method,target):
    options = Options()
    options.binary_location = r'C:\Users\Pc\AppData\Local\Mozilla Firefox\firefox.exe'
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.instagram.com/")
    time.sleep(1)
    driver.maximize_window()
    time.sleep(3)
    cookies = open("ckis.json", "r")
    e = json.load(cookies)
    for cookie in e:
            if cookie["domain"] == ".instagram.com":
                driver.add_cookie(cookie)
                print(cookie)
    driver.get(target)
    if method=="likes":
        driver.find_element(By.XPATH,("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button")).click()
    else:
        driver.find_element(By.XPATH, ("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button"))
    input()


def convert(fl):
    netscape = open(fl, "r")
    lines = netscape.read()
    url = "https://www.cookieconverter.com/"
    data = {'cookieNetscape': lines}
    r = requests.post(url, data=data)
    txt = r.text
    txt = txt[txt.find('[{"domain'):]
    txt = txt[:txt.find('</textarea>')]
    t = "ckis.json"
    jso = open("ckis.json", "w")
    jso.write(txt)
    jso.close()


def directory():
    filepath=filedialog.askdirectory(initialdir=r"F:\python\pythonProject",title="Dialog box")
    l['text'] = filepath


def sel():
    global method
    if var.get()=="1":
        method="likes"
    else:
        method="followers"

def main():
    if method=="":
        messagebox.showerror(title=None, message="Select likes or followers")
    elif l.cget("text")=="":
        messagebox.showerror(title=None, message="Select directory")
    elif target.index("end") == 0:
        messagebox.showerror(title=None, message="Please select target")
    else:
        res = []
        for (dir_path, dir_names, file_names) in walk(l.cget("text")):
            try:
                file_names.index('Cookies.txt')
                convert(dir_path + "\\" + 'Cookies.txt')
                login(method,target.cget("text"))
            except:
                continue






method=""
root = Tk()

root.iconbitmap('icon.ico')
root.geometry('700x400')
root.title("INSTAXEL")
var = IntVar()
R1 = Radiobutton(root, text="likes", variable=var, value=1,command=sel)
R2 = Radiobutton(root, text="followers", variable=var, value=2,command=sel)
l = Label(text="", borderwidth=1, relief="solid", width="50")
l2= Label(text="", borderwidth=1, relief="solid")
l3= Label(text="Target post or profile")
target=Entry(width="80")
dialog_btn = Button(text='select cookies directory', command=directory)
start_btn= Button(text="start",command=main)
dialog_btn.grid(row = 0, column = 0, sticky = W, pady = 1)
l.grid(row = 0, column = 1, pady = 2)
R1.grid(row = 1, column = 0, sticky = W, pady = 1)
R2.grid(row = 1, column = 1, pady = 2)
start_btn.grid(row = 3, column = 1, pady = 1)
l2.grid(row = 4, column = 1, pady = 1)
l3.grid(row = 2, column = 0, pady = 1)
target.grid(row = 2, column = 1, pady = 1)
root.mainloop()


