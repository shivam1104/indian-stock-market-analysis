#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # linear algebra
import pandas as pd # pandas for dataframe based data processing and CSV file I/O


# In[2]:


import requests # for http requests
from bs4 import BeautifulSoup # for html parsing and scraping
from fastnumbers import isfloat 
from fastnumbers import fast_float
from multiprocessing.dummy import Pool as ThreadPool 
import bs4

import matplotlib.pyplot as plt
import seaborn as sns
import json
from tidylib import tidy_document # for tidying incorrect html
'''
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
'''

# In[3]:



def ffloat(string):
    if string is None:
        return np.nan
    if type(string)==float or type(string)==np.float64:
        return string
    if type(string)==int or type(string)==np.int64:
        return string
    return fast_float(string.split(" ")[0].replace(',','').replace('%',''),
                      default=np.nan)

def ffloat_list(string_list):
    return list(map(ffloat,string_list))

def remove_multiple_spaces(string):
    if type(string)==str:
        return ' '.join(string.split())
    return string


# In[4]:


url1="https://www.bseindia.com/corporates/Forth_Results.aspx"
url="https://www.nseindia.com/companies-listing/corporate-filings-event-calendar"
url2= "https://economictimes.indiatimes.com/markets/stocks/mcalendar.cms"


headers = {
    'authority': 'beta.nseindia.com',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'sec-fetch-user': '?1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
}


# In[5]:


response = requests.get(url, timeout=240, headers=headers)
response.status_code
response.content


# In[6]:


soup = BeautifulSoup(response.content,"html.parser")


# In[7]:


select_object=soup.find('select',{'id':'eventCalender_equities_fourthComing'})
print(select_object)


# In[8]:


#new_tag = BeautifulSoup('<option value="15D" data-date="forward">Next 15 Days</option>').option
#<option value="">All Forthcoming</option>

for item in select_object:
    if str(item) == '<option value="">All Forthcoming</option>':
        del item['selected']
    if str(item) == '<option value="15D" data-date="forward">Next 15 Days</option>':
        item['selected'] = 'selected'

submit_data = str(select_object).replace("forthComingSelect","forthComingSelect active")       
#<select class="forthComingSelect active" id="eventCalender_equities_fourthComing">
                                                        
print(submit_data)


# In[9]:


'''
action = soup.find('div', 'custom_select').get('action')
post_url = get_post_url(url, action)

# parse the html and prepare the form
form = {'limit': '0', ...}

# send post request the form data
response = requests.post(post_url, data=form)

'''


# In[10]:


'''
request=requests.post(url,params=str(select _object), headers=headers)
soup=BeautifulSoup(request.content)
'''


# In[ ]:


# parsing data
response = requests.post(url, data=submit_data,timeout=240, headers=headers)

soup = BeautifulSoup(response.content)

print(soup)

'''
for row in soup.select('table.tData01 tr'):
    print [td.text for td in row.find_all('td')]
'''


# In[ ]:




