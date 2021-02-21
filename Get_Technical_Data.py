import datetime as dt
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
from YahoBuilt import getHistoricPricing
from indicators import Master
from ta import add_all_ta_features
from ta.utils import dropna


symbol = "RELIANCE"

hist = getHistoricPricing(symbol, "10y")
'''
hist['Next_Open'] = hist['Open'].shift(periods=1)
hist['Next_High'] = hist['High'].shift(periods=1)
'''
master = Master(hist,symbol)
print(master)
print(master.shape)
master.corr()


master = master.dropna()

master.to_csv('master.csv')
x=master.corr()
x.to_csv('corr.csv')

print(master)

# Add ta features filling NaN values
his_master = add_all_ta_features(hist, open="Open", high="High", low="Low", close="Close", volume="Volume", fillna=True)
print(his_master)
Master_All = pd.merge(left=master, right=his_master, left_on='Date', right_on='Date')
print(Master_All)

Master_All.to_csv("MasterJoin.csv")

Master_All.corr().to_csv("MasterJoin_Corr.csv")

