from nsetools import Nse
from pprint import pprint
from csv import writer
import pandas as pd
from datetime import date

def getGainValue():
	today = date.today()
	nse= Nse()

	top_gainers = pd.DataFrame(nse.get_top_gainers())
	#print(top_gainers)
	filenames= {}
	filenames['TG'] = 'Files/TopGainers'+str(today)+'.csv'
	top_gainers.to_csv(filenames['TG'])
	print(filenames)
	return top_gainers



def getLostValue():
	today = date.today()
	nse= Nse()
	top_losers = pd.DataFrame(nse.get_top_losers())
	#print(top_losers)
	filenames= {}
	filenames['TL'] = 'Files/TopLosers'+str(today)+'.csv'
	top_losers.to_csv(filenames['TL'])
	print(filenames)
	return top_losers



print("Main-ed")
#getLostValue()
#getGainValue()