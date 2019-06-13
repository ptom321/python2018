#!/usr/bin/env python
# coding: utf-8

# In[18]:


path=r'C:\Users\priyanka\Desktop\python2\pythonprogram\BSE-BOM500209.csv'
file=open(path,'r')
dic={}
i=0
from datetime import datetime
for line in file:
     
     
    if line.startswith('Date'):
        continue
    
    line=line.strip()
    column=line.split(',')
    
    close = float(column[4])
    
    date=datetime.strptime(column[0], "%Y-%m-%d")
    month=date.month
  #   month=date.strftime('%B')
    year=date.year
    
    if year in dic:
        if month in dic[year]:
            dic[year][month].append(close)
        else:
            dic[year][month] = list()
            dic[year][month].append(close)
    else:
        dic[year]={month:[]}
        dic[year][month].append(close)
        
    

#Get average of each month of each year
for yr in dic:
    for mn in dic[yr]:
        dic[yr][mn]=sum(dic[yr][mn])/len(dic[yr][mn])

#Gen % change for each month in each year
for yr in dic:
    prev=0
    for mnth in sorted(dic[yr]):
        if prev:
            prcntg=((dic[yr][mnth]-prev)/prev)*100
            prev=dic[yr][mnth]
            dic[yr][mnth]=prcntg           
        else:
            prev = dic[yr][mnth]
            dic[yr][mnth]='init'
            
#Print year wise report            
for yr in dic:
    print(f'Report for year {yr}')
    for mnth in sorted(dic[yr]):
        month = datetime(1900,mnth, 1).strftime('%B')
        print(f'{month} : {dic[yr][mnth]}')
    print('\n')

