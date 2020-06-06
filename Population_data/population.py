#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 14:35:56 2020

@author: colburnhassman
"""

# The purpose of this file is to create a csv file of population timeseries
# Which can be read into the main data analysis. 
# The data is collected from wikipedia 

import requests
from bs4 import BeautifulSoup
import pandas as pd

#%%
#---------------------Germany ------------------------------#
url1 = "https://en.wikipedia.org/wiki/Demographics_of_Germany"
s = requests.Session()
response = s.get(url1, timeout = 10) # go to the URL to pull data
src = response.content # assign content of the response to source
soup = BeautifulSoup(src, 'lxml') # feed source into BeautifulSoup
r_table = soup.find('table', {'class': 'wikitable collapsible'}) #Find table type from page to identify the proper table

# rows have <tr> tags, made up of data with <td> tags.
# Create 11 lists to hold each column of the tables
A = []
B = []
C = []
D = []
E = []
F = []
G = []
H = []
I = []
J = []
K = []

# Loop through table and append the text to the list
for row in r_table.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) == 11:
        A.append(cells[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))
        F.append(cells[5].find(text=True))
        G.append(cells[6].find(text=True))
        H.append(cells[7].find(text=True))
        I.append(cells[8].find(text=True))
        J.append(cells[9].find(text=True))
        K.append(cells[10].find(text=True))
     
DE = pd.DataFrame(A, columns = ['Year'])
DE['Population'] = B # append only the Population column
DE = DE.replace('\n', '', regex = True) #remove all \n
DE = DE.replace(" ", '', regex = True) #remove all empty spaces
print(DE)

#%%
#--------------------Sweden--------------------------#
url1 = "https://en.wikipedia.org/wiki/Demographics_of_Sweden"

s = requests.Session()
response = s.get(url1, timeout = 10) # go to the URL to pull data
src = response.content # assign content of the response to source
soup = BeautifulSoup(src, 'lxml') # feed source into BeautifulSoup

#We will need to adjust the strategy used for this, as the table we want it not 
# unique in it's class. We will have to choose all tables then select it 
r_table = soup.find_all('table', {'class': 'wikitable'})[16] 

# Create 9 lists to hold each column of the tables
A = []
B = []
C = []
D = []
E = []
F = []
G = []
H = []
I = []

for row in r_table.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) == 9:
        A.append(cells[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))
        F.append(cells[5].find(text=True))
        G.append(cells[6].find(text=True))
        H.append(cells[7].find(text=True))
        I.append(cells[8].find(text=True))
        

        
SE = pd.DataFrame(A, columns = ['Year'])
SE['Population'] = B
SE = SE.replace('\n', '', regex = True) #remove all \n
SE = SE.replace(" ", '', regex = True) #remove all empty spaces
print(SE)

#%%
#--------------France-----------------------
url1 = "https://en.wikipedia.org/wiki/Demographics_of_France"

s = requests.Session()
response = s.get(url1, timeout = 10) # go to the URL to pull data
src = response.content # assign content of the response to source
soup = BeautifulSoup(src, 'lxml') # feed source into BeautifulSoup

# We will approach this just as we did with Sweden
r_table = soup.find_all('table', {'class': 'wikitable'})[19] 

# Create 12 lists to hold each column of the tables
A = []
B = []
C = []
D = []
E = []
F = []
G = []
H = []
I = []
J = []
K = []
L = []

# Loop through table and append the text to the list
for row in r_table.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) == 12:
        A.append(cells[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))
        F.append(cells[5].find(text=True))
        G.append(cells[6].find(text=True))
        H.append(cells[7].find(text=True))
        I.append(cells[8].find(text=True))
        J.append(cells[9].find(text=True))
        K.append(cells[10].find(text=True))
        L.append(cells[11].find(text=True))

FR = pd.DataFrame(A, columns = ['Year'])
FR['Population'] = B
FR = FR.replace('\n', '', regex = True) #remove all \n
FR = FR.replace(" ", '', regex = True) #remove all empty spaces
print(FR)

#%%
url1 = "https://en.wikipedia.org/wiki/Demographics_of_Denmark"

s = requests.Session()
response = s.get(url1, timeout = 10) # go to the URL to pull data
src = response.content # assign content of the response to source
soup = BeautifulSoup(src, 'lxml') # feed source into BeautifulSoup

# We will approach this just as we did with Sweden
r_table = soup.find_all('table', {'class': 'wikitable'})[6] 

# Create 12 lists to hold each column of the tables
A = []
B = []
C = []
D = []
E = []
F = []
G = []
H = []
I = []

# Loop through table and append the text to the list
for row in r_table.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) == 9:
        A.append(cells[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))
        F.append(cells[5].find(text=True))
        G.append(cells[6].find(text=True))
        H.append(cells[7].find(text=True))
        I.append(cells[8].find(text=True))
       
DN = pd.DataFrame(A, columns = ['Year'])
DN['Population'] = B
DN = DN.replace('\n', '', regex = True) #remove all \n
DN = DN.replace(" ", '', regex = True) #remove all empty spaces
print(DN)

#%%
#------------------------Italy-------------------
url1 = "https://en.wikipedia.org/wiki/Demographics_of_Italy"

s = requests.Session()
response = s.get(url1, timeout = 10) # go to the URL to pull data
src = response.content # assign content of the response to source
soup = BeautifulSoup(src, 'lxml') # feed source into BeautifulSoup

# For this one, the table is sortable, so we can look directly for it
r_table = soup.find('table', {'class': 'wikitable sortable'})

# Create lists to hold each column of the tables
A = []
B = []
C = []
D = []
E = []
F = []
G = []
H = []
I = []

# Loop through table and append the text to the list
for row in r_table.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) == 9:
        A.append(cells[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))
        F.append(cells[5].find(text=True))
        G.append(cells[6].find(text=True))
        H.append(cells[7].find(text=True))
        I.append(cells[8].find(text=True))
IT = pd.DataFrame(A, columns = ['Year'])
IT['Population'] = B
IT = IT.replace('\n', '', regex = True)
IT = IT.replace(' ', '', regex = True)
print(IT)

#%%
#----------------Poland-----------------------#
url1 = "https://en.wikipedia.org/wiki/Demographics_of_Poland"

s = requests.Session()
response = s.get(url1, timeout = 10) # go to the URL to pull data
src = response.content # assign content of the response to source
soup = BeautifulSoup(src, 'lxml') # feed source into BeautifulSoup

r_table = soup.find_all('table', {'class': 'wikitable collapsible'})[1]


# Create 12 lists to hold each column of the tables
A = []
B = []
C = []
D = []
E = []
F = []
G = []
H = []
I = []
J = []
K = []
L = []
M = []
N = []
O = []

# Loop through table and append the text to the list
for row in r_table.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) == 15:
        A.append(cells[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))
        F.append(cells[5].find(text=True))
        G.append(cells[6].find(text=True))
        H.append(cells[7].find(text=True))
        I.append(cells[8].find(text=True))
        J.append(cells[9].find(text=True))
        K.append(cells[10].find(text=True))
        L.append(cells[11].find(text=True))
        M.append(cells[12].find(text=True))
        N.append(cells[13].find(text=True))
        O.append(cells[14].find(text=True))
PO = pd.DataFrame(A, columns = ['Year'])
PO['Population'] = B
PO = PO.replace('\n', '', regex = True)
PO = PO.replace(' ', '', regex = True)
print(PO)

#%%
#-----------------------Spain----------------------#
url1 = "https://en.wikipedia.org/wiki/Demographics_of_Spain"

s = requests.Session()
response = s.get(url1, timeout = 10) # go to the URL to pull data
src = response.content # assign content of the response to source
soup = BeautifulSoup(src, 'lxml') # feed source into BeautifulSoup

# We will approach this just as we did with Sweden
r_table = soup.find_all('table', {'class': 'wikitable'})[10] 

# Create lists to hold each column of the tables
A = []
B = []
C = []
D = []
E = []
F = []
G = []
H = []
I = []

# Loop through table and append the text to the list
for row in r_table.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) == 9:
        A.append(cells[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))
        F.append(cells[5].find(text=True))
        G.append(cells[6].find(text=True))
        H.append(cells[7].find(text=True))
        I.append(cells[8].find(text=True))
       
SP = pd.DataFrame(A, columns = ['Year'])
SP['Population'] = B
SP = SP.replace('\n', '', regex = True)
SP = SP.replace(' ', '', regex = True)
SP = SP['Year'].replace('(p)', '', regex = True) # Need to figure it out. Need to get rid of () for 2018
print(SP)

#%%
#-------------Switzerland--------------------#
url1 = "https://en.wikipedia.org/wiki/Demographics_of_Switzerland"

s = requests.Session()
response = s.get(url1, timeout = 10) # go to the URL to pull data
src = response.content # assign content of the response to source
soup = BeautifulSoup(src, 'lxml') # feed source into BeautifulSoup

# We will approach this just as we did with Sweden
r_table = soup.find_all('table', {'class': 'wikitable'})[6] 

# Create lists to hold each column of the tables
A = []
B = []
C = []
D = []
E = []
F = []
G = []
H = []
I = []

# Loop through table and append the text to the list
for row in r_table.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) == 9:
        A.append(cells[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))
        F.append(cells[5].find(text=True))
        G.append(cells[6].find(text=True))
        H.append(cells[7].find(text=True))
        I.append(cells[8].find(text=True))
       
SW = pd.DataFrame(A, columns = ['Year'])
SW['Population'] = B
SW = SW.replace('\n', '', regex = True)
SW = SW.replace(' ', '', regex = True)
print(SW)