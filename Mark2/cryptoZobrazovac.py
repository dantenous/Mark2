import urllib.request, json
from tkinter import *
import tkinter as tk
import db
import matplotlib.pyplot as plt
import datetime



database = r"/home/lukaschvostal/python/crypto.db"
conn = db.create_connection(database)
cur = conn.cursor() 

r  = Tk() 
r.geometry("500x530")
r.title('Cryptomenovy zobrazovac')
menu = Menu(r) 
r.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='Soubor', menu=filemenu) 
filemenu.add_command(label='New') 
filemenu.add_command(label='Open...') 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=r.quit) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Napoveda', menu=helpmenu) 
helpmenu.add_command(label='About')      

Lb = Listbox(r, width=490, height=30)

dog = ["1", "2", "3", "4", "5", "6"]


def graf():
    
    data = db.select_all_cryptomeny(conn)
    tst = []
    tst2 = []
    for row in data:
        tst.append(row[3])
        tst2.append(row[4])
    print(tst2)
    fig, ax = plt.subplots()
    ax.plot(tst2, tst, label="Crypto")
    ax.legend()
    plt.show()


def obnov():
    data = db.select_all_cryptomeny(conn)
    Lb.delete(0, END)
    for row in data:
        Lb.insert(END, row[1]+ " " + row[2] + " " + str(row[3]))
    Lb.pack()

def nacti(urlod1):
    with urllib.request.urlopen(urlod1) as url:
        data = json.loads(url.read().decode())
    i = 0
    x = datetime.datetime.now()
    print(x.strftime("%X"))
    # create a database connection
    while i < len(data):
        cur.execute("INSERT INTO cryptomeny(name,symbol,price_usd, datum) VALUES('"+data[i]['name']+"', '"+data[i]['symbol']+"', '"+data[i]['price_usd']+"', '"+x.strftime('%x'+' '+'%X')+"')")
        i+=1
    conn.commit()
    cur.close()

nacti("https://api.coinmarketcap.com/v1/ticker/?limit=1")


button = tk.Button(r, text='Zobraz data', width=25, command=obnov) 
button2 = tk.Button(r, text='Zobraz graf', width=25, command=graf) 
button.pack()
button2.pack()

r.mainloop() 
