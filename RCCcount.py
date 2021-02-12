import numpy as np
import pandas as pd
import streamlit as st
from datetime import datetime as dt

def RCC():
        
    st.title('RCC repair count 2018 Jan - 2020 December')

    data_load_state = st.text('Loading data...')

    #Indexを月ごとにしたい場合 resampleでIndexを月ベースに変更可能 M...月、Q...クォーター、W...週
    #out_month = out.resample('W').sum()

    #データフレーム読み込み
    df = pd.read_csv('RCCcount.csv')

    #Inovice DateをDatetime型に変更
    df['Invoice Date'] = pd.to_datetime(df['Invoice Date'])

    df['day of week'] = df['Invoice Date'].dt.day_name()

    df['year'] = df['Invoice Date'].dt.year
    df['month'] = df['Invoice Date'].dt.month

    df = df.set_index("Invoice Date")
    #indexの日付を月でリサンプリングしたデータフレームdf_month
    #df_month = df.resample('M').sum()
    df_month = df.resample('M').sum()

    #multiselect
    options = st.multiselect(
        'Select RCC',
        ['100', '203', '204', '205','206','207'],
        ['100', '203', '204', '205', '206', '207']
    )
    #options.insert(0,'day of week')
    #streamlitにデータフレームとグラフを出力
    st.header('Count of repair by day')
    st.dataframe(df[options])
    st.text('simple analysis')
    st.dataframe(df[options].describe())
    #st.line_chart
    chart_data = df_month[options]
    st.area_chart(chart_data)

    month = st.slider(
        'value of SMA window',
        1, 12)
    st.header('Sngle Moving Average (SMA)')
    chart_data2 = df_month[options].rolling(month).mean()
    st.line_chart(chart_data2)



