#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 16:25:15 2017

@author: boo
"""

import pandas as pd
df = pd.read_csv("/Users/sangeetha/Downloads/DAT210x-master/Module2/Datasets/tutorial.csv")
#print(df)
#print(df.describe())
#print(df.loc[2:4, 'col3'])
#print(df)

new_df = pd.read_csv("/Users/sangeetha/Downloads/DAT210x-master/Module2/Datasets/servo.data",header=None)
#print(new_df)
print(new_df[new_df.loc[:,3]== 5].count())
#print(new_df)

print(new_df[(new_df.loc[:,0] == 'E') & (new_df.loc[:,1] == 'E')].count())
print(new_df[new_df.loc[:,2]== 4].loc[:,3].mean())
#print(new_df[[new_df.loc[:,3]]>5])

web = pd.read_excel("/Users/sangeetha/Desktop/from web.xlsx")
print(web)
web=web.dropna(axis=0,thresh=4)
print(web)
web=web.drop(labels=['RK'],axis=1)
print(web)
print(web.dtypes)
print(web['PCT'].value_counts())


lab5= pd.read_csv("/Users/sangeetha/Downloads/DAT210x-master/Module2/Datasets/census.data",header=None,names=['education', 'age', 'capital-gain', 'race', 'capital-loss', 'hours-per-week', 'sex', 'classification'])
print(lab5)
print(lab5.dtypes)
lab5['capital-gain'] = lab5['capital-gain'].apply(pd.to_numeric,errors='coerce')
lab5['capital-gain']=lab5['capital-gain'].fillna(0.0)
print(lab5.dtypes)
print(lab5)
education_ordered = [
        '7th-8th',
        '9th',
        '10th',
        '11th',
        '12th',
        'HS-grad',
        'Some-college',
        'Bachelors',
        'Masters',
        'Doctorate']

lab5.education = lab5.education.astype("category",
                                       ordered=True,
                                       categories=education_ordered).cat.codes

                                       
print(lab5.classification.unique())
class_ordered= [
        '<=50K',
        '>50K'
        ]

lab5.classification=lab5.classification.astype("category",
                                               ordered=True,
                                               categories=class_ordered).cat.codes
lab5 = pd.get_dummies(lab5,columns=['sex'])
lab5 = pd.get_dummies(lab5,columns=['race'])


print lab5

#lab5=lab5['capital gain'].replace()