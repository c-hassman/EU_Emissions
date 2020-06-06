#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This code ia part of a larger analysis of EU Emmissions data. 
The purpose of this program is to pull GDP data from the World Bank, 
clean and subset the data, and export the data as a csv to be uses in 
the main analysis program
@author: Colburn Hassman
"""

# Import required packages
import pandas as pd
import world_bank_data as wb
import matplotlib.pyplot as plt

# Pull the data from the world bank
gdp = wb.get_series('NY.GDP.MKTP.PP.CD', simplify_index = True)

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
GDP = GDP[(GDP.index > "2007") & (GDP.index < '2019')] 
#subset the data to only be the relevant years
GDP.to_csv('gdp_data.csv') #export the data to a csv file

