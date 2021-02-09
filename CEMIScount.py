import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
from datetime import datetime as dt

def CEMIS():

    st.title('CEMIS count 2018 Jan - 2020 December')

    data_load_state = st.text('Loading data...')

    #データフレーム読み込み
    df = pd.read_csv('CEMIScount.csv')

    #Inovice DateをDatetime型に変更
    df['Invoice Date'] = pd.to_datetime(df['Invoice Date'])
    print(df.info())

    df['day of　week'] = df['Invoice Date'].dt.day_name()

    df['year'] = df['Invoice Date'].dt.year
    df['month'] = df['Invoice Date'].dt.month

    df = df.set_index("Invoice Date")
    #df = df.fillna(0)
    #indexの日付を月でリサンプリングしたデータフレームdf_month
    df_month = df.resample('M').sum()

    #multiselect, listを返す
    options = st.multiselect(
        'Select CEMIS code',
        ['AC', 'AD', 'AJ', 'AO','BM','BO','BQ','CD','CQ','PJ','VC'],
        ['AC', 'AD', 'AJ', 'AO','BM','BO','BQ','CD','CQ','PJ','VC']
    )

    #streamlitにデータフレームとグラフを出力
    st.header('Count of repair')
    st.dataframe(df[options])
    #st.line_chart
    st.header('Repair counts by month')
    chart_data = df_month[options]
    st.area_chart(chart_data)

    month = st.slider(
        'value of SMA window',
        3, 12)
    st.header('Single Moving Average (SMA)')
    chart_data2 = df_month[options].rolling(month).mean()
    st.line_chart(chart_data2)




