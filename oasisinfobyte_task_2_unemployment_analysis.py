# -*- coding: utf-8 -*-
"""OasisInfobyte_Task_2_Unemployment_Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jiCZR3LWmGGpqmdqF7jp1eyxtjxvrkB4

## Importing Necessary Libraries
"""

import numpy as np
import pandas as pd

"""## Reading CSV File"""

df=pd.read_csv("Unemployment_Rate_upto_11_2020.csv")

df.head()

df.tail()

df.shape  #Returns tuple of shape (Rows,Columns) of dataframe

df.info() #Prints info about dataframe

df.describe() #Prints numerical decription of the data in dataframe

x=df['Region']

x

y=df[' Estimated Unemployment Rate (%)']

y

df2=df.iloc[:,3]

df2

"""## Importing Necessary Libraries"""

import plotly.express as px
import matplotlib.pyplot as plt

"""## Analyzing Data by bar graphs"""

fg=px.bar(df,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
          title='Unemployment Rate (State-Wise) by bar Graph',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()

fg=px.bar(df,x='Region.1',y=' Estimated Unemployment Rate (%)',color='Region',
          title='Unemployment Rate (Region-Wise) by Bar Graph',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()



fg=px.box(df,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
          title='Unemployment Rate (State-Wise) by box Graph',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()

fg=px.scatter(df,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
          title='Unemployment Rate (State-Wise) by Scatter Graph',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()

fg=px.histogram(df,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
          title='Unemployment Rate (State-Wise) by Histogram',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()