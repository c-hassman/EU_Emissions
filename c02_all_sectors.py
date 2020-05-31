#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 10:07:52 2020

@author: Colburn Hassman and Ingrid Nilsson
"""

import pandas as pd
import matplotlib.pyplot as plt

#%%
data = pd.read_excel('air_emmis.xls', skiprows = 10, na_values = ":") # Read in excel, skip header rows, : = na 
data = pd.melt(data, id_vars = ["GEO/TIME"], var_name = 'year') # Melt data to make narrow/long
data = data.set_index(["GEO/TIME", "year"]) #Set Index to a multi index of country and year
#%%
plt.plot(data.loc['Germany'], label = "Germany")
plt.plot(data.loc['France'], label = "France")
plt.title("Total Co2 Emmissions per Year")
plt.ylabel("Tonnes Co2")
plt.legend()
#%%
