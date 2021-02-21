
import datetime as dt
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def RSI(price,symbol,window=14):
    prices = price.copy()
    prices["Diff"] = prices["Close"].diff()
    prices["Gain"] = prices["Diff"][prices["Diff"]>0]
    prices["Loss"] = (-1)*prices["Diff"][prices["Diff"]<0]
    prices = prices.fillna(0)
    prices["AvgGain"] = prices["Gain"].rolling(window=window).mean()
    prices["AvgLoss"] = prices["Loss"].rolling(window=window).mean()
    prices["RSI"] = 100 - (100/(1+ prices["AvgGain"]/prices["AvgLoss"]))
    # print(prices)
    # return prices[["RSI"]]
    return prices

def BB(price,symbol,window=20):
    prices = price.copy()
    prices["SMA"] = prices["Close"].rolling(window=window).mean()
    prices["STD"] = prices["Close"].rolling(window=window).std()
    prices["UBB"] = prices["SMA"] + 2*prices["STD"]
    prices["LBB"] = prices["SMA"] - 2*prices["STD"]
    prices["BBP"] = (prices["Close"] - prices["SMA"]) / (2 * prices["STD"])
    # print(prices)
    # return prices[[symbol,"SMA","UBB","LBB","BBP"]]
    return prices
    # return prices[["BBP"]]

def MACD(price,symbol):
    prices = price.copy()
    prices["EM12"] = pd.Series.ewm(prices["Close"], span=12).mean()
    prices["EM26"] = pd.Series.ewm(prices["Close"], span=26).mean()
    prices["MACD"] = prices["EM12"]-prices["EM26"]
    prices["MACD_EM9"] = pd.Series.ewm(prices["MACD"], span=9).mean()
    prices["MACD_HIST"] = prices["MACD"] - prices["MACD_EM9"]
    prices["MACD_T"] = np.sign(prices["MACD_HIST"]).diff()
    prices.iloc[0:2,-1] = 0
    # del prices["SPY"]
    # print(prices)
    return prices
    # return prices[[symbol,"MACD_T"]]

def Master(price,symbol):
    #MACD
    prices = price.copy()
    prices["EM12"] = pd.Series.ewm(prices["Close"], span=12).mean()
    prices["EM26"] = pd.Series.ewm(prices["Close"], span=26).mean()
    prices["MACD"] = prices["EM12"]-prices["EM26"]
    prices["MACD_EM9"] = pd.Series.ewm(prices["MACD"], span=9).mean()
    prices["MACD_HIST"] = prices["MACD"] - prices["MACD_EM9"]
    prices["MACD_T"] = np.sign(prices["MACD_HIST"]).diff()
    prices.iloc[0:2,-1] = 0

    #RSI-Non Window
    prices["Diff"] = prices["Close"].diff()
    prices["Gain"] = prices["Diff"][prices["Diff"]>0]
    prices["Loss"] = (-1)*prices["Diff"][prices["Diff"]<0]
    for window in range(5,21):
        #BB
        strwindow = str(window)
        prices["SMA"+strwindow] = prices["Close"].rolling(window=window).mean()
        prices["STD"+strwindow] = prices["Close"].rolling(window=window).std()
        prices["UBB"+strwindow] = prices["SMA"+strwindow] + 2*prices["STD"+strwindow]
        prices["LBB"+strwindow] = prices["SMA"+strwindow] - 2*prices["STD"+strwindow]
        prices["BBP"+strwindow] = (prices["Close"] - prices["SMA"+strwindow]) / (2 * prices["STD"+strwindow])
        #RSI
        prices = prices.fillna(0)
        prices["AvgGain"+strwindow] = prices["Gain"].rolling(window=window).mean()
        prices["AvgLoss"+strwindow] = prices["Loss"].rolling(window=window).mean()
        prices["RSI"+strwindow] = 100 - (100/(1+ prices["AvgGain"+strwindow]/prices["AvgLoss"+strwindow]))

    return prices
