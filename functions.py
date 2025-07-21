# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 22:50:03 2025

@author: JdeDios4
"""

import plotly.express as px
import matplotlib.pyplot as plt
#%%
# Data
data = {'Category': ['A', 'B', 'C', 'D'], 'Value': [40, 25, 20, 15]}

#%%
# Pie chart
fig = px.pie(data, names='Category', values='Value', title='Pie Chart')
fig.show(renderer="browser")
fig.show()

#%%Bar Chart
fig = px.bar(data, x='Category', y='Value', title='Bar Chart')
fig.show(renderer="browser")

#%%Line Chart
fig = px.line(data, x='Category', y='Value', title='Line Chart', markers=True)
fig.show(renderer="browser")

#%% Scatter Plot
fig = px.scatter(data, x='Category', y='Value', title='Scatter Plot', size='Value')
fig.show(renderer="browser")

#%% Box Plot
fig = px.box(data, x='Category', y='Value', title='Box Plot')
fig.show(renderer="browser")

#%% Histogram
fig = px.histogram(data, x='Value', title='Histogram')
fig.show(renderer="browser")

#%% Area Chart
fig = px.area(data, x='Category', y='Value', title='Area Chart')
fig.show(renderer="browser")

#%% Treemap
fig = px.treemap(data, path=['Category'], values='Value', title='Treemap')
fig.show(renderer="browser")

#%% Sunburst Chart
fig = px.sunburst(data, path=['Category'], values='Value', title='Sunburst Chart')
fig.show(renderer="browser")