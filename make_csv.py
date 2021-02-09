import numpy as np
import pandas as pd

print("importing excel files...")

df = pd.read_excel('Repair data 2018 Jan_Apr.xlsx')
df = df.append(pd.read_excel('Repair data 2018 May_Aug.xlsx'))
df = df.append(pd.read_excel('Repair data 2018 Sep_Dec.xlsx'))
df2 = pd.read_excel('Repair data 2019 Jan_Apr.xlsx')
df2 = df2.append(pd.read_excel('Repair data 2019 May_Aug.xlsx'))
df2 = df2.append(pd.read_excel('Repair data 2019 Sep_Dec.xlsx'))
df3 = pd.read_excel('Repair data 2020 Jan_Jun.xlsx')
df3 = df3.append(pd.read_excel('Repair data 2020 Jul_Dec.xlsx'))
print(df.info()) #データフレームの情報表示



print("importing excel files... done!")

#ソート
df = df.sort_values(by='Invoice Date') #Month yearを指定してデータフレームをソート
df2 = df2.sort_values(by='Invoice Date') #Month yearを指定してデータフレームをソート
df3 = df3.sort_values(by='Invoice Date') #Month yearを指定してデータフレームをソート

#全体も作っておく
df_all = pd.concat([df,df2,df3])


#ピボットテーブルのデータフレーム
CEMIScount = df_all.pivot_table(index='Invoice Date', columns='CEMIS', values='Model', aggfunc = 'count')
RCCASFcount = df_all.pivot_table(index='Invoice Date', columns='TRQ_WSHP', values='CEMIS', aggfunc='count')
RCCcount = df_all.pivot_table(index='Invoice Date', columns='RCC CODE', values='CEMIS', aggfunc='count')
TRQTYPEcount = df_all.pivot_table(index='Invoice Date', columns='TRQ_TYPE', values='CEMIS', aggfunc = 'count')
Modelcount = df_all.pivot_table(index='Invoice Date', columns='Model', values='CEMIS', aggfunc = 'count')

#結合
#out = pd.concat([CEMIScount,RCCcount, RCCASFcount, TRQTYPEcount], axis=1, keys=['CEMIS', 'RCC_CODE', 'TRQ_WSHP', 'TRQ_TYPE']).fillna(0)
#print(out.info())

#csv出力
df_all.to_csv("Repair data 2020 all.csv")
df.to_csv("Repair data 2018.csv")
df2.to_csv("Repair data 2019.csv")
df3.to_csv("Repair data 2020.csv")
CEMIScount.to_csv("CEMIScount.csv")
RCCASFcount.to_csv("RCCASFcount.csv")
RCCcount.to_csv("RCCcount.csv")
TRQTYPEcount.to_csv("TRQTYPEcount.csv")
Modelcount.to_csv("Modelcount.csv")

print("output to csv is succeeded.")