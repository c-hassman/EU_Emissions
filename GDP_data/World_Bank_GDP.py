#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 09:34:52 2020

@author: colburnhassman
"""


import pandas as pd
import world_bank_data as wb
import matplotlib.pyplot as plt

#%%

gdp = wb.get_series('NY.GDP.MKTP.PP.CD', simplify_index = True)

#%%
# Create a new GDP dataframe from only the countries in question, 
# which merges along the index of years
GDP = pd.DataFrame({'Germany'     : gdp['Germany'],
                    'France'      : gdp['France'], 
                    'Italy'       : gdp['Italy'],
                    'Spain'       : gdp['Spain'],
                    'Netherlands' : gdp['Netherlands'],
                    'Switzerland' : gdp['Switzerland'],
                    'Poland'      : gdp['Poland'],                    
                    'Sweden'      : gdp['Sweden'],
                    'Belgium'     : gdp['Belgium']})

GDP.index = pd.to_datetime(GDP.index) # Convert the index to DateTime object
#%%
plt.plot(GDP['Germany'])                   
plt.ylim(0, 5000000000000) 
plt.title("German GDP")

#%%
GDP = GDP[GDP.index > "2008"]
print(GDP.head())