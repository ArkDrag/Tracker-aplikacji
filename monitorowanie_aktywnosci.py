
'''
monitorowanie otwartych aplikacji i kart w przegladarce internetowej 
''' 
from pywinauto import Desktop
import time
from datetime import datetime


    
procesy={}
czas={}

def aktywnosc(procesy,czas):
    now = datetime.now()
        # odliczanie czasu i pobieranie otwarych okien
    current_time = now.strftime("%H:%M:%S")
    time.sleep(1)
    windows = Desktop(backend="uia").windows()# pokazuje obeznie otwarte okna 
     #usunięcie okien systemowych
    for w in windows:
        if w.window_text() !="Program Manager" and w.window_text()!="App tracker" and w.window_text()!="Spyder (Python 3.8)" and w.window_text()!="Pasek zadań" and w.window_text()!="":
     
     
            if w.window_text() not in procesy: # dodawanie procesó♠w do słownika i zliczanie czasu
                procesy[w.window_text()]=1
            else:
                procesy[w.window_text()]+=1
                 # sortowanie slownika od najdłużej trwającego procesu do najkrócej
    procesy=dict(sorted(procesy.items(), key=lambda item: item[1],reverse=True))
             # tworzenie słownika proces: moment pierwszego otwarcia
    for w in windows:
        if w.window_text() !="Program Manager" and w.window_text()!="App tracker" and w.window_text()!="Spyder (Python 3.8)" and w.window_text()!="Pasek zadań" and w.window_text()!="":
     
            if w.window_text() not in czas:
             # Skrócenie nazwy kart Google chrome( zeby było czytelne na wykresie)
                if "Google" in w.window_text():
                    w.window_text=w.window_text().split(" ")         
                    czas["Google Chrome:karta: "+w.window_text[0]+" "+w.window_text[1]]=str(current_time)
                
                else:
                    czas[w.window_text()]=str(current_time)
aktywnosc(procesy,czas)