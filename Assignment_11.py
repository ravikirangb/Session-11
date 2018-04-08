# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 18:16:11 2018

@author: Ravikiran
"""
import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url= 'https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'
titanic = pd.read_csv(url)

# Create a pie chart presenting the male/female proportion

df = titanic.assign(SrNo = [1 + i for i in range(len(titanic))])[['SrNo'] + titanic.columns.tolist()]
print (df)

table = pd.pivot_table(data=df, values='SrNo', index='sex', columns='survived', aggfunc='count')
pie_female = table.loc['female']
pie_male = table.loc['male']

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8,4))

pie_1 = axes[0].pie(pie_female, labels=['Not survived','Survived'],autopct='%1.1f%%', colors=['gold', 'lightskyblue'])

axes[0].set_title('Female')
axes[0].axis('equal')

pie_2 = axes[1].pie(pie_male, labels=['Not survived','Survived'], autopct='%1.1f%%', startangle=90, colors=['gold', 'lightskyblue'])
axes[1].set_title('Male')
plt.axis('equal')

plt.subplots_adjust(wspace=1)
plt.show()


# Create a scatterplot with the Fare paid and the Age, differ the plot color by gender

print ("Below plot is a scatter plot \n\n")
x = df['fare']
y = df['age']
z = df['sex']

colors = np.where(df['sex']=='female','r','g')

scatter_plot = plt.scatter(x, y, alpha=0.5, c=colors)

plt.xlabel('Fare')
plt.ylabel('Age')
plt.show()


