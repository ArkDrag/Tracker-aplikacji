'''
tworzenie ramki danych 
'''

import monitorowanie_aktywnosci
import pandas as pd
import numpy as np
procesy=monitorowanie_aktywnosci.procesy
czas=monitorowanie_aktywnosci.czas
def data_frame(procesy, czas):    
    indeks=[i for i in czas.keys()]
    czas_wlaczenia=[j for j in czas.values()]
    liczba_sekund=[z for z in procesy.values()]
    
    
    czas_wlaczenia=np.array(czas_wlaczenia)
    liczba_sekund=np.array(liczba_sekund)
    df=pd.DataFrame(czas_wlaczenia,index=indeks, columns=["godzina włączenia"])
    df["czas działania [s]"]=liczba_sekund.tolist()
    return df