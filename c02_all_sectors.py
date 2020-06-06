#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 10:07:52 2020

@author: Colburn Hassman and Ingrid Nilsson
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

#%%
data = pd.read_excel('air_emmis.xls', skiprows = 10, na_values = ":") # Read in excel, skip header rows, : = na 
data = pd.melt(data, id_vars = ["GEO/TIME"], var_name = 'year') # Melt data to make narrow/long
data['year'] = pd.to_datetime(data['year'])# Convert year column to a datetime
data = data[(data['year'] > '2007') & (data['year'] < '2019')] #subset the data to only include relevant years                                        
data = data.set_index(["GEO/TIME", "year"]) #Set Index to a multi index of country and year
data.index.names=['Country', 'year'] # rename the index values to something more descriptive
#%%
# Plot the selected countries
plt.plot(data.loc['Germany'], label = "Germany")
plt.plot(data.loc['France'], label = "France")
plt.plot(data.loc['Italy'], label = "Italy")
plt.plot(data.loc['Spain'], label = "Spain")
plt.plot(data.loc['Netherlands'], label = "Netherlands")
plt.plot(data.loc['Poland'], label = "Poland")
plt.plot(data.loc['Belgium'], label = "Belgium")
plt.plot(data.loc['Switzerland'], label = "Switzerland")
plt.plot(data.loc['Sweden'], label = "Sweden")
plt.title("Total Co2 Emmissions per Year")
plt.ylabel("Tonnes Co2")
plt.legend()
#%%
data_pct =data.groupby(level ="Country")['value'].pct_change() * 100 #group data by country and taking the percentage change from the year before
plt.plot(data_pct.loc['Sweden'], label = "Sweden")
plt.plot(data_pct.loc['Germany'], label = "Germany")
plt.plot(data_pct.loc['France'], label = "France")
plt.plot(data_pct.loc['Italy'], label = "Italy")
plt.plot(data_pct.loc['Spain'], label = "Spain")
plt.plot(data_pct.loc['Netherlands'], label = "Netherlands")
plt.plot(data_pct.loc['Poland'], label = "Poland")
plt.plot(data_pct.loc['Belgium'], label = "Belgium")
plt.plot(data_pct.loc['Switzerland'], label = "Switzerland")
plt.title("Percentage change of Co2 Emissions per year")
plt.ylabel("Percentage change")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5)) #placing the label outside of the graph

#%%


