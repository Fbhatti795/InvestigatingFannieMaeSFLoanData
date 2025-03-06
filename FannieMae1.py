# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 13:38:33 2023

@author: Fthulu
"""
#import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
#import numpy as np
import os
#import glob
#import sklearn

import GitPython

#Eventually will write in code to automatically push this .py file to GitHub public repo for this project.

#Will try to use containerization with Docker to make an environment that contains all the necessary packages for this script to run properly.
#Will try to use Flask to create a dynamic webapp that allows for a UI that lets a user choose which quarter of data from Fannie Mae to choose for analysis from a dropdown.
#Will try to use FannieMae API or AWS w/ import boto3. Not sure yet how to.

#New development as of March 6th 2025. Figured out how to use Microsoft Graph to download files from OneDrive. Will clean the data from Fannie Mae for it to be only the 20 columns that are needed, and then upload them to OneDrive. When the script is run, the files can be downloaded locally on a temp directory that is chosen by the user when prompted. Those files are deleted at the end of the script. 


#import onedrivesdk_fork as onedrivesdkposer

# =============================================================================
# import onedrivesdk
# 
# from onedrivesdk.helpers import GetAuthCodeServer
# =============================================================================

cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))
os.chdir("C:/Users/Faisal Bhatti/OneDrive/Documents/Downloads/FannieMaePROJECT/")
cwd = os.getcwd()
print("New working directory: {0}".format(cwd))

#from onedrivesdkposer.helpers import GetAuthCodeServer

importfilelist = ["2020Q1", "2020Q2", "2020Q3", "2020Q4", "2021Q1", "2021Q2", "2021Q3", "2021Q4", "2022Q1", "2022Q2","2022Q3", "2022Q4", "2023Q1", "2023Q2", "2023Q3","2023Q4", "2024Q1", "2024Q2", "2024Q3"]

#The dictionary for the what each of the 108 columns are can be found at https://capitalmarkets.fanniemae.com/media/6931/display. 
#There is not enough memory to load all the columns at the same time or to load all the quarters."
#Take the 'Field Position' and subtract 1 to figure out the column names because indexing starts at 0."

#Importing datasets. You can comment in/out whichever sets you would like to include in your analysis.

colnames = [1,8,9,11,13,16,17,20,21,22,23,25,30,31,32,34,35,36,39,40]
headings = ["loanid","currint","origUPB","curractUPB","OrigDate","MTLM","MTM","CLTV","Numborr","DTI", "BorrCRS","FTHBI", "State", "MSA", "ZipShort", "ARMorFIX", "PPI", "IntONLY", "CurrDelinq", "PayHist"] 
#fanniemae = importfilelist
fanniemae_2020Q1 = pd.read_csv('2020Q1.csv',sep='|', usecols=colnames, names=headings)
#fanniemae_2020Q2 = pd.read_csv('2020Q2.csv',sep='|', usecols=colnames, names=headings)

# =============================================================================
# fanniemae_2020Q3 = pd.read_csv('2020Q3.csv',sep='|', usecols=colnames, names=headings)
# fanniemae_2020Q4 = pd.read_csv('2020Q4.csv',sep='|', usecols=colnames, names=headings)
# fanniemae_2021Q1 = pd.read_csv('2021Q1.csv',sep='|', usecols=colnames, names=headings)
# fanniemae_2021Q2 = pd.read_csv('2021Q2.csv',sep='|', usecols=colnames, names=headings)
# fanniemae_2021Q3 = pd.read_csv('2021Q3.csv',sep='|', usecols=colnames, names=headings)
# fanniemae_2021Q4 = pd.read_csv('2021Q4.csv',sep='|', usecols=colnames, names=headings)
# fanniemae_2022Q1 = pd.read_csv('2022Q1.csv',sep='|', usecols=colnames, names=headings)
# fanniemae_2022Q2 = pd.read_csv('2022Q2.csv',sep='|', usecols=colnames, names=headings)
# fanniemae_2022Q3 = pd.read_csv('2022Q3.csv',sep='|', usecols=colnames, names=headings)
# fanniemae_2022Q4 = pd.read_csv('2022Q4.csv',sep='|', usecols=colnames, names=headings)
# fanniemae_2023Q1 = pd.read_csv('2023Q1.csv',sep='|', usecols=colnames, names=headings)
# fanniemae_2023Q2 = pd.read_csv('2023Q2.csv',sep='|', usecols=colnames, names=headings)
# fanniemae_2023Q3 = pd.read_csv('2023Q3.csv',sep='|', usecols=colnames, names=headings)
# fanniemae_2023Q4 = pd.read_csv('2023Q4.csv',sep='|', usecols=colnames, names=headings)
# fanniemae_2024Q1 = pd.read_csv('2024Q1.csv',sep='|', usecols=colnames, names=headings)
# fanniemae_2024Q2 = pd.read_csv('2024Q2.csv',sep='|', usecols=colnames, names=headings)
# fanniemae_2024Q3 = pd.read_csv('2024Q3.csv',sep='|', usecols=colnames, names=headings)
# 
# =============================================================================

#Load each variable one at a time because each one takes time to load.
#SpotCheck Variable Explorer in Spyder that vars are correctly loaded. 

#Try the analysis with the first two datasets first. 

#fanniemae_2024Q3 = pd.read_csv('2024Q3.csv',sep='|', usecols=colnames, names=headings)

#Rudimentary EDA
fanniemae_2020Q1.apply(lambda x: x.isnull().sum(), axis=0) #Counts the nulls in each column. 
fanniemae_2020Q1.groupby(['FTHBI','State'])[['currint','BorrCRS','DTI']].mean()

fanniemae_2020Q1_FTHBI_Y_only = fanniemae_2020Q1[fanniemae_2020Q1['FTHBI']=='Y']
fanniemae_2020Q1_FTHBI_Y_only.columns = headings
fanniemae_2020Q1_FTHBI_Y_only.shape
fanniemae_2020Q1_FTHBI_Y_only.head(5)

fanniemae_2020Q1.groupby(['FTHBI','State'])[['loanid']].count()
#fanniemae_2020Q2.groupby(['FTHBI','State'])[['loanid']].count()

fanniemae_2020Q1_FTHBI_Y_only.groupby(['State'])[['loanid']].count()

#Setting the color "vector" to standardize it.
colorvect = fanniemae_2020Q1_FTHBI_Y_only.groupby(['State'])[['loanid']].count()
#print(colorvect)

from sklearn.preprocessing import StandardScaler
#colorvect['loanid']
colorvect.iloc[:,0:1] = StandardScaler().fit_transform(colorvect.iloc[:, 0:1])

#Making a note of warning from running line 93
# =============================================================================
# FutureWarning: Setting an item of incompatible dtype is deprecated and will raise in a future error of pandas. Value '[-0.82605751 -0.40239234 -0.62686548  0.34882964  3.05284639  0.24458932
#  -0.20125289 -0.7443365  -0.71095882  3.18214358  0.8467212  -0.87336223
#  -0.68943093 -0.27078185 -0.63601248  1.02695829  0.04785222 -0.57882901
#  -0.50891057 -0.38783977 -0.11066814  0.16725886 -0.77626246  0.58890579
#   0.37883178 -0.16546749 -0.6773805  -0.68783758  0.77683816 -0.78696739
#  -0.44922495 -0.695285    0.57364506 -0.55056185 -0.15787843  1.6521406
#   0.64507423 -0.56789983 -0.11587307  0.99787675 -0.78662512 -0.71383865
#  -0.13373037 -0.72267877 -0.08164561  3.7312701  -0.28675073  0.22787687
#  -0.86990407 -0.8131573   0.52563219  0.15125457 -0.76145023 -0.79842769]' has dtype incompatible with int64, please explicitly cast to a compatible dtype first.
# =============================================================================

# =============================================================================
# The standardized z-scores are accurate with the first 5 values from the colorvect dataframe. 
# 
#        loanid
# State        
# AK       4063
# AL      39959
# AR      20940
# AZ     103608
# CA     332712 
# =============================================================================

#Simply with z-scores, one can see which states have the most mortgages and the fewest. Possible to understand the nature of a distribution.
#Time to apply a color gradient. 

#https://stackoverflow.com/questions/25668828/how-to-create-colour-gradient-in-python#29736037

from colour import Color
red = Color("red")
colors = list(red.range_to(Color("green"),54))

#Colors is now a list of length 54 with 54 hexadecimal color codes representing steps between "red" and "green".
#colors

#Now to apply each color to each corrresponding state based on whether it has more or fewer mortgages.

len(colorvect)
# =54

#Transform colorvect into ascending order to append to colors list to it to make the USA choropleth from it.

asc_ordered_colorvect = colorvect.sort_values(['loanid'], ascending=[True])

#Dataframe for USA_mortgage_dist_choro
Red2GreenCol = pd.DataFrame({'col':colors})
print(Red2GreenCol)
len(Red2GreenCol)

#Makes the indices of the two dataframes the same before concat'ing.
Red2GreenCol.index = asc_ordered_colorvect.index
DF_USA_mortgage_dist_choro = pd.concat([asc_ordered_colorvect, Red2GreenCol], axis=1)
#The above command concats vertically even though it should concat horizontsally. Only way to make it concat correctly is to make the indices the same. Have to create a new DataFrame to hold the data.

#test = pd.merge(asc_ordered_colorvect, Red2GreenCol, left_index=True, right_index=True, how='outer')
#The function append has been deprecated in the package pandas, and 
#asc_ordered_colorvect.append(Red2GreenCol, ignore_index=True)

DF_USA_mortgage_dist_choro.head()

#There are a total of 889 regions by 3 digit zip-codes.
len(fanniemae_2020Q1['ZipShort'].unique())

#Testing out using plotly.io https://plotly.com/python/choropleth-maps/
# =============================================================================
# import plotly.io as pio
# pio.renderers.default='browser'
# from urllib.request import urlopen
# import json
# import requests
# 
#with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
#     counties = json.load(response)
#      
#counties["features"][0]
# =============================================================================

#import plotly
import plotly.express as pxexp

#Testing with 3 states.
#choro_rel_oftotloans_by3state = pxexp.choropleth(locations=["AK", "AL", "AR"], locationmode="USA-states", color=['red', 'green', 'blue'], scope="usa")
#choro_rel_oftotloans_by3state.show(renderer='browser')  

#There are 57 "states". The color "vector" will be a standardized z-score of the count of loans/total by state. 
    #choro_perc_oftotloans_bystate = pxexp.choropleth(locations=["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "GU", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VI", "VT", "WA", "WI", "WV", "WY"], locationmode="USA-states", color=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], scope="usa")
    #choro_perc_oftotloans_bystate.show(renderer='browser')
    

#finalchoro_rel_oftotloans_bystate = pxexp.choropleth(locations=["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "GU", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VI", "VT", "WA", "WI", "WV", "WY"], locationmode="USA-states", color_discrete_sequence = [DF_USA_mortgage_dist_choro['col']], scope="usa")
#This does not work properly with the colorvect created. I will try to use the ipyleaflet package instead.

#This works correctly, but does not use the gradient color scale that I wanted.
#finalchoro_rel_oftotloans_bystate = pxexp.choropleth(locations=["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "GU", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VI", "VT", "WA", "WI", "WV", "WY"], locationmode="USA-states", color = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], scope="usa")
#finalchoro_rel_oftotloans_bystate.show(renderer='browser')  

#ipyleaflet package is not interactive like plotly. Bummer.
#https://coderzcolumn.com/tutorials/data-science/choropleth-maps-using-ipyleaflet

#Found the answer https://stackoverflow.com/questions/73704214/set-specific-color-for-a-value-in-plotly-choropleth-maps#73710914
#colorscale = ["rgb(255, 51, 51)", "rgb(210, 231, 154)", "rgb(94, 179, 39)", "rgb(67, 136, 33)", "rgb(33, 74, 12)"]
#finalchoro_rel_oftotloans_bystate = pxexp.choropleth(asc_ordered_colorvect, locations=['GU', 'VI', 'AK', 'VT', 'WY', 'ND', 'PR', 'ME', 'WV', 'DC', 'SD', 'RI', 'DE', 'NH', 'HI', 'MT', 'MS', 'ID', 'AR', 'KS', 'OK', 'NM', 'KY', 'NE', 'AL', 'LA', 'UT', 'IA', 'CT', 'MO', 'NV', 'SC', 'OR', 'MA', 'TN', 'IN', 'WI', 'MD', 'VA', 'CO', 'AZ', 'MN', 'WA', 'NJ', 'MI', 'OH', 'NC', 'GA', 'PA', 'IL', 'NY', 'CA', 'FL', 'TX'], color = 'loanid', locationmode="USA-states", title = "Scaled representation of Number of Mortgages for 2020 Q1 by State", color_continuous_scale = colorscale, color_continuous_midpoint=0, range_color=(-5,18.5), scope="usa", labels={'loanid':'Z-score of Number of Mortgages'})
#finalchoro_rel_oftotloans_bystate.show(renderer='browser')  

colorscale = ["rgb(255, 51, 51)", "rgb(210, 231, 154)", "rgb(94, 179, 39)", "rgb(67, 136, 33)", "rgb(33, 74, 12)"]
finalchoro_rel_oftotloans_bystate = pxexp.choropleth(asc_ordered_colorvect, locations=['GU', 'VI', 'AK', 'VT', 'WY', 'ND', 'PR', 'ME', 'WV', 'DC', 'SD', 'RI', 'DE', 'NH', 'HI', 'MT', 'MS', 'ID', 'AR', 'KS', 'OK', 'NM', 'KY', 'NE', 'AL', 'LA', 'UT', 'IA', 'CT', 'MO', 'NV', 'SC', 'OR', 'MA', 'TN', 'IN', 'WI', 'MD', 'VA', 'CO', 'AZ', 'MN', 'WA', 'NJ', 'MI', 'OH', 'NC', 'GA', 'PA', 'IL', 'NY', 'CA', 'FL', 'TX'], color = 'loanid', locationmode="USA-states", title = "Scaled Representation of Number of Mortgages for 2020 Q1 by State",subtitle="Source: Single-Family Loan Performance Data | Fannie Mae", color_continuous_scale = colorscale, color_continuous_midpoint=0, range_color=(-1,4), scope="usa", labels={'loanid':'Z-score of Number of Mortgages'})
finalchoro_rel_oftotloans_bystate.show(renderer='browser') 

#Making second visualization that is a choropleth of 889 zip shorts that shows 0 to 100 % FTHBI.
#fanniemae_2020Q1.groupby(['FTHBI','State'])[['loanid']].count()
(fanniemae_2020Q1['ZipShort'].unique())
DF_choro_FTHBI_TOT = fanniemae_2020Q1.groupby(['ZipShort'])[['FTHBI']].count()
DF_choro_FTHBI_numb_y_only = fanniemae_2020Q1_FTHBI_Y_only.groupby(['ZipShort'])[['FTHBI']].count()


fanniemae_2020Q1_FTHBI_N_only = fanniemae_2020Q1[fanniemae_2020Q1['FTHBI']=='N']
fanniemae_2020Q1_FTHBI_N_only.columns = headings
DF_choro_FTHBI_numb_n_only = fanniemae_2020Q1_FTHBI_N_only.groupby(['ZipShort'])[['FTHBI']].count()
#Verily, 1394 = 7296 = 8690.

DF_choro_FTHBI_TOT["Percentage (Y)"] = ( DF_choro_FTHBI_numb_y_only['FTHBI'] /  DF_choro_FTHBI_TOT['FTHBI'] ) * 100
DF_choro_FTHBI_TOT.head(5)

#To understand 3-digit Zip Codes. 
#https://conheroineivaj.blogspot.com/2016/11/3-digit-zip-code-map-united-states.html

#Need to generate my own .json file for the boundaries of the 3-digit zip code regions. 
#https://gis.stackexchange.com/questions/116308/where-can-i-get-a-topojson-with-3-digit-zip-codes-zip3-shapes
#https://github.com/gweissman86/three_digit_zips?tab=readme-ov-file
#https://www.statsilk.com/maps/convert-esri-shapefile-map-geojson-format

#Going to upload the .json file to the Github repo for this project and then call for the .json file within this script to generate the choropleth.

import plotly.io as pio
pio.renderers.default='browser'
from urllib.request import urlopen
import json
import requests

with urlopen('https://raw.githubusercontent.com/Fbhatti795/InvestigatingFannieMaeSFLoanData/b00794b12912277ea418a5c36bd994ff4efd09ef/three_dig_zips.json') as response:
    ThreeDigitZips = json.load(response)     

ThreeDigitZips["features"][0]

colorscale = ["rgb(255, 51, 51)", "rgb(210, 231, 154)", "rgb(94, 179, 39)", "rgb(67, 136, 33)", "rgb(33, 74, 12)"]
#finalchoro_perc_FTHBI_byZipShort = pxexp.choropleth(DF_choro_FTHBI_TOT, locations=['GU', 'VI', 'AK', 'VT', 'WY', 'ND', 'PR', 'ME', 'WV', 'DC', 'SD', 'RI', 'DE', 'NH', 'HI', 'MT', 'MS', 'ID', 'AR', 'KS', 'OK', 'NM', 'KY', 'NE', 'AL', 'LA', 'UT', 'IA', 'CT', 'MO', 'NV', 'SC', 'OR', 'MA', 'TN', 'IN', 'WI', 'MD', 'VA', 'CO', 'AZ', 'MN', 'WA', 'NJ', 'MI', 'OH', 'NC', 'GA', 'PA', 'IL', 'NY', 'CA', 'FL', 'TX'], color = 'Percentage (Y)', locationmode="USA-states", title = "Percentage of FTHBI Per 889 3-Digit Zip Codes for 2020 Q1",subtitle="Source: Single-Family Loan Performance Data | Fannie Mae", color_continuous_scale = colorscale, color_continuous_midpoint=0, range_color=(0,100), scope="usa", labels={'Percentage (Y)':'% of FTHBI'})

#ValueError: All arguments should have the same length. The length of column argument `df[color]` is 888, whereas the length of previously-processed arguments ['locations'] is 54
#Need to make a list of all 888 3 Digit Zip Codes. 

arraythreezips = (fanniemae_2020Q1['ZipShort'].unique())
listthreezips = arraythreezips.tolist()
print(listthreezips)
#When the list is printed, then you can see that the 3rd to last value is listed as nan. That zip code is most probably the 3 digit zip code 000. That's why there was a discrepancy  of 888 total items in one list, and 889 in another. Let's set listthreezips[886] = 000. 

listthreezips[886] = 000
#Done. Well, still shows up as 'nan'. Both the number of color(s) and the unique number of 3 digit Zip codes are the same quantity of 888. or 889 if you count that 'nan' value. 

DF_choro_FTHBI_TOT = DF_choro_FTHBI_TOT.reset_index()
#Without the above command, there is an error because the 3 digit zip codes are the index of the dataframe.
finalchoro_perc_FTHBI_byZipShort = pxexp.choropleth(DF_choro_FTHBI_TOT, geojson= ThreeDigitZips, locations='ZipShort', color = 'Percentage (Y)', title = "Percentage of FTHB's Per 889 3-Digit Zip Codes for 2020 Q1",subtitle="Source: Single-Family Loan Performance Data | Fannie Mae", color_continuous_scale = colorscale, color_continuous_midpoint=0, range_color=(0,100), scope="usa", labels={'Percentage (Y)':'% of FTHBs'})

finalchoro_perc_FTHBI_byZipShort.show(renderer='browser') 

#fanniemae_2020Q1['FTHBI'].head()

# =============================================================================
# dict(
#             text="Life Expectancy",
#             subtitle=dict(
#                 text="Life expectancy by European country in 1952 and in 2002",
#                 font=dict(color="gray", size=13),
#             )
# =============================================================================
# =============================================================================
# import pandas as pd
# df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
#                    dtype={"fips": str})
# 
# import plotly.express as px
# 
# fig = px.choropleth(df, geojson=counties, locations='fips', color='unemp',
#                            color_continuous_scale="Viridis",
#                            range_color=(0, 12),
#                            scope="usa",
#                            labels={'unemp':'unemployment rate'}
#                           )
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.show()
# 
# =============================================================================
df1 = fanniemae_2023Q1.groupby(['State'])['currint','BorrCRS','DTI'].mean()
df1.index.name = 'State'
df1.reset_index(inplace=True)

fig, ax = plt.subplots()
ax.bar(df1['State'].tolist(), df1['currint'].tolist(), align='center', width=0.8)
ax.figure(figsize = (20, 5))
ax.set_ylabel('Mean Current Interest Rate')
ax.set_xlabel('States')              
ax.set_title('Mean Current Interst Rate per State')
plt.show

pd.unique(fanniemae_2023Q1['OrigDate'])
len(pd.unique(fanniemae_2023Q1['OrigDate']))

pd.set_option('display.max_columns', 8)
mins = fanniemae_2023Q1.loc[fanniemae_2023Q1['CLTV'].idxmin()]
maxs = fanniemae_2023Q1.loc[fanniemae_2023Q1['CLTV'].idxmax()]
minsnmaxs = pd.concat([mins, maxs], axis=1).reset_index()

# =============================================================================
# import matplotlib.pyplot as plt
# 
# fig, ax = plt.subplots()
# 
# fruits = ['apple', 'blueberry', 'cherry', 'orange']
# counts = [40, 100, 30, 55]
# bar_labels = ['red', 'blue', '_red', 'orange']
# bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
# 
# ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
# 
# ax.set_ylabel('fruit supply')
# ax.set_title('Fruit supply by kind and color')
# ax.legend(title='Fruit color')
# 
# plt.show()
# 
# =============================================================================
with urlopen('https://gist.githubusercontent.com/mshafrir/2646763/raw/8b0dbb93521f5d6889502305335104218454c2bf/states_titlecase.json') as response:
    states = json.load(response)

import plotly.express as px

df2 = fanniemae_2023Q1.groupby(['State'])['loanid'].count()
df2 = pd.DataFrame(df2)
df2.index.name = 'State'
df2.reset_index(inplace=True)

# =============================================================================
# fig = px.choropleth(df2, locations='State', locationmode='USA-states' color='loanid',
#                     
#                            color_continuous_scale="Viridis",
#                            range_color=(0, 1500000),
#                            scope="usa",
#                            labels={'unemp':'unemployment rate'}
#                           )
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.show()
# 
# =============================================================================
# =============================================================================
# for i in importfilelist:
#     print("fanniemae_" + (i))
#     fanniemae[i] =  "fanniemae_" + (i)
#     print(fanniemae)
#     ("fanniemae_" + (i)) = pd.read_csv(((i)+".csv"),sep='|')
#     
# =============================================================================


# =============================================================================
# importfilelist = ("2022Q1.csv", "2022Q2.csv", "2022Q3.csv", "2022Q4.csv", "2023Q1.csv")
# folder_name = 'FannieMaeMortData'
# file_type = 'csv'
# seperator ='|'
# dataframe = pd.concat([pd.read_csv(f, sep=seperator) for f in glob.glob(folder_name + "/*."+file_type)],ignore_index=True)
#     
# =============================================================================
