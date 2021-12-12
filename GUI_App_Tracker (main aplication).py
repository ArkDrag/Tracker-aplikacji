import monitorowanie_aktywnosci
import wykresy
import data_frame
from tkinter import *
from tkinter import ttk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
from tkinter import filedialog
from pandastable import Table, TableModel
import tkinter
# tworzenie okna tkinter i ustalanie wielosci
win = tkinter.Tk()

win.geometry("700x680")
win.title("App tracker")
running = True # potrzebne do petli monitorowania czasu

czas={}
procesy={}
# funkcja monitorowania aktywnosci w petli
def print_text():
    if running:
        global procesy
        monitorowanie_aktywnosci.aktywnosc(procesy, czas)
        
    win.after(1000, print_text)

# funkcje wykresów
def timeline(): 
    global bar
    wykres=wykresy.timeline(czas)
    bar = FigureCanvasTkAgg(wykres, win)
    bar.get_tk_widget().pack(fill=X, side=BOTTOM)
def plot():
    global bar1
    wykres2=wykresy.plot(procesy)
    bar1 = FigureCanvasTkAgg(wykres2, win)
    bar1.get_tk_widget().pack(fill=X, side=BOTTOM)
# dane do tabeli i eksport do excela
def data_frame_2():# pokazuje dataframe w oknie konsoli 
    print(data_frame.data_frame(procesy, czas))
 
def to_excel(): #eksport dataframe do pandas tabel, mozliwosc dalszego eksportu do excela
    frame = tkinter.Frame(win)
    frame.pack(fill='both', expand=True)
    df=data_frame.data_frame(procesy, czas)
        
    pt = Table(frame, dataframe=df, showtoolbar=True, showstatusbar=True)
    pt.show()
    

#usuwanie widgetow
def usun_timeline():
    global bar
    for item in bar.get_tk_widget().find_all():
       bar.get_tk_widget().forget()
    
def usun_plot():
    global bar1
    for item in bar1.get_tk_widget().find_all():
       bar1.get_tk_widget().forget()
    
canvas = Canvas(win, bg="skyblue3", width=700, height=60)
canvas.create_text(350, 30, text="Program został włączony", font=('', 13))
canvas.pack()
# dodawanie przycisków
timeline =        ttk.Button(win,width=12, text="Timeline",       command=timeline).place(x=0,y=61)
plot1 =           ttk.Button(win,width=12, text="Plot",           command=plot).place(x=100,y=61)
df =              ttk.Button(win,width=12, text="Data_frame",     command=data_frame_2).place(x=200,y=61)
df_to_excel =     ttk.Button(win,width=12, text="Pokaż tabelę",    command=to_excel).place(x=300,y=61)
clear_timeline =  ttk.Button(win,width=12, text="Usuń timeline",  command=usun_timeline).place(x=400,y=61)
clear_plot =      ttk.Button(win,width=12, text="Usuń plot",      command=usun_plot).place(x=500,y=61)
zamknij =         ttk.Button(win,width=12, text="Zamknij",        command=win.destroy).place(x=600,y=61)

#uruchamianie funkcji print_text
win.after(1, print_text)

win.mainloop()