from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from nsetools import Nse
from NSEDownload import stocks
from nsepython import *
import PYTopLosersTopGainersEquity as ab

def getSymbols():
    today = date.today()
    currentDay = datetime.datetime.now().day
    currentMonth = datetime.datetime.now().month
    currentYear = datetime.datetime.now().year
    start = datetime.datetime(2018,4,20)
    end = datetime.datetime(currentYear,currentMonth,currentDay-1)


    nse= Nse()
    OptionLot = (nse.get_fno_lot_sizes())
    print(OptionLot)


    listOptions = OptionLot.keys()
    TG = ab.getGainValue()
    TL = ab.getLostValue()
    data =pd.DataFrame(nse_events())

    data['HasOption'] = -1
    TL['HasOption'] = -1
    TG['HasOption'] = -1

    for i, row in data.iterrows():
        if data.at[i,'symbol'] in listOptions:
            data.at[i,'HasOption'] = 1
        else:
            data.at[i,'HasOption'] = 0

    for i, row in TL.iterrows():
        if TL.at[i,'symbol'] in listOptions:
            TL.at[i,'HasOption'] = 1
        else:
            TL.at[i,'HasOption'] = 0

    for i, row in TG.iterrows():
        if TG.at[i,'symbol'] in listOptions:
            TG.at[i,'HasOption'] = 1
        else:
            TG.at[i,'HasOption'] = 0

    symbols = []
    symbols = TL.symbol.tolist()
    symbols+= TG.symbol.tolist()
    symbols+= data.symbol.tolist()
    print("List Of Stocks to Analyse Today :- ")
    print(symbols)
    return(symbols)

print("Mained")