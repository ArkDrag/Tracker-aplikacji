'''
wykresy przedstawiajace graficznie czas dzialania programów

timeline: pokazuje moment pierwszego włączenia danego programu
plot: sumuje czas kiedy dany program był włączony

'''
import matplotlib.pyplot as plt
from datetime import datetime 
import numpy as np


 

def timeline(my_time): 
    '''
    my_time=monitorowanie_aktywnosci.czas 
    '''
    for i in my_time:
        my_time[i]=datetime.strptime(my_time[i],"%H:%M:%S").strftime("%H:%M:%S") # konwertowanie str na date
    
    names =[i for i in my_time]
    
    dates=[my_time[j] for j in my_time]
    dates = [datetime.strptime(d, "%H:%M:%S").strftime("%H:%M:%S") for d in dates]
    #randowome y, zeby bylo lepiej widać wykres ;)
    levels = np.tile([-5, 5, -3, 3, -1, 1],
                     int(np.ceil(len(dates)/6)))[:len(dates)]
    fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)
    ax.plot(dates, np.zeros_like(dates), "-o",
            color="k", markerfacecolor="w") 
    plt.xticks(rotation=90)
    ax.vlines(dates, 0, levels) 
    for d, l, r in zip(dates, levels, names):
        ax.annotate(r, xy=(d, l),
                    xytext=(-3, np.sign(l)*3), textcoords="offset points",
                    horizontalalignment="right",
                    verticalalignment="bottom" if l > 0 else "top")
    ax.yaxis.set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    ax.spines['left'].set_visible(False)
    ax.margins(y=0.1)
    ax.set_title("Czas włączenia programów")
    #plt.savefig('Timeline.png')
    return fig
    
def plot(myDictionary):
    '''
    myDictionary=monitorowanie_aktywnosci.wynik
    '''
    dict2 = dict()
    karta=1
    # zamiana nazw kart Google Chrom na krótsze
    for key in myDictionary:
        if "Google" in key:
            dict2["Google karta nr"+str(karta)] = myDictionary[key]
            karta+=1
        else:
            dict2[key] = myDictionary[key]
    myDictionary=dict2    
    fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)
    plt.bar(myDictionary.keys(), myDictionary.values(), color='g')
    plt.title("Czas otwarcia aplikacji/stron internetowych")
    plt.xticks(rotation=90)
    plt.ylabel("Czas spędzony na danej aplikacji/stronie internetowej [s]")
    plt.xlabel("Nazwa aplikacji")
    #plt.savefig('Bar_plot.png')
    return fig