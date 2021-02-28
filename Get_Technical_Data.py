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
from GenerateSymbols import getSymbols
from datetime import date

today = date.today()

symbols = getSymbols()
for symbol in symbols:
	print("Currently working on {0}".format(symbol))
	filePath_Master ="AnalysisOn/MasterFile" + str(symbol)+" " + str(today)+".csv" 
	filePath_Corr ="AnalysisOn/CorrFile" + str(symbol)+" " + str(today)+".csv" 
	hist = getHistoricPricing(symbol, "10y")
	master = Master(hist,symbol)
	#print(master)
	print(master.shape)
	master = master.dropna()

	# Add ta features filling NaN values
	hist_master = add_all_ta_features(hist, open="Open", high="High", low="Low", close="Close", volume="Volume", fillna=True)
	#print(hist_master)
	Master_All = pd.merge(left=master, right=hist_master, left_on=['Date', 'Open','High','Low','Close','Adj Close','Volume','Dividends','Stock Splits'], right_on=['Date', 'Open','High','Low','Close','Adj Close','Volume','Dividends','Stock Splits'] , how="inner")
	#print(Master_All.columns)

	#print(Master_All)
	Master_All['Next_Open'] = Master_All['Open'].shift(periods=-1)
	Master_All['Next_High'] = Master_All['High'].shift(periods=-1)
	#del Master_All['Open']
	#del Master_All['High']
	#print(Master_All)

	Master_Open = Master_All.copy()
	Master_High = Master_All.copy()
	
	del Master_Open['Next_High']
	del Master_High['Next_Open']

	Master_Open.to_csv("AnalysisOn/Open/TechnicalsOpen"+str(symbol)+".csv")
	Master_High.to_csv("AnalysisOn/High/TechnicalsHigh"+str(symbol)+".csv")
	#Master_All.corr().to_csv("AnalysisOn/MasterJoin_Corr"+str(symbol)+".csv")
	print("Completed :- {0}".format(symbol))
	#input("Check")

print("Mained")