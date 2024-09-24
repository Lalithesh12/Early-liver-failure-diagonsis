# -*- coding: utf-8 -*-
"""Module1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12QDZcq8YVhOQFE-mV0SqOixZ3xzw2d0Z

#  Module 1: Data validation and pre-processing technique
"""


#import library packages
import pandas as pd

import numpy as np

# warning
import warnings
warnings.filterwarnings('ignore')

#load given dataset
data = pd.read_csv("C:\\Users\\User\\Desktop\\fproject\\dataset\\liver_patient.csv")

data.head()

#shape
data.shape

#size
data.size

#Checking datatype and information about dataset
data.info()

#To describe the dataframe
data.describe()

#duplicate data
data.duplicated()

# sum of duplicated 
data.duplicated().sum()

data = data.drop_duplicates()

data.shape

data.duplicated().sum()

data.size

data.shape

# null values
data.isnull()

#sum of null values
data.isnull().sum()

# before drop null values
data.shape

#drop null values
df=data.dropna()

#drop after drop null values
df.shape

data.size

df.isnull().sum()

#changing feature name
df = df.rename({'Dataset': 'Result'}, axis=1)

df.head(10)

df.columns

df.Gender.unique()

df['Result'].describe()

df.Age.unique()

df['Total_Bilirubin'].unique()

df[ 'Direct_Bilirubin'].unique()

df['Alkaline_Phosphotase'].unique()

df['Alamine_Aminotransferase'].unique()

df['Alamine_Aminotransferase'].unique()

df['Total_Protiens'].unique()

df['Albumin'].unique()

df['Albumin'].unique()

df['Albumin_and_Globulin_Ratio'].unique()

df["Result"].unique()

df.columns

pd.Categorical(df['Age']).describe()

pd.Categorical(df['Gender']).describe()

pd.Categorical(df['Result']).describe()

df["Alkaline_Phosphotase"].min()

df["Alkaline_Phosphotase"].max()

df["Alkaline_Phosphotase"].mean()

df["Age"].sort_values().unique()

df.columns

from sklearn.preprocessing import LabelEncoder

var_mod = {'Gender'}
le=LabelEncoder()
for i in var_mod:
    df[i] = le.fit_transform(df[i]).astype(int)

df.head()

df.corr()

df.head()
