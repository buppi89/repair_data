import numpy as np
import pandas as pd
import streamlit as st
import datetime

import matplotlib.pyplot as plt

from fbprophet import Prophet
from fbprophet.diagnostics import performance_metrics
from fbprophet.diagnostics import cross_validation
from fbprophet.plot import plot_cross_validation_metric

def CEMIS():

    st.title('CEMIS count 2018 Jan - 2020 December')

    data_load_state = 'Loading data...'
    st.text(data_load_state)
    data_load_state = 'Done!'
    st.text(data_load_state)

    #データフレーム読み込み
    df = pd.read_csv('CEMIScount.csv')

    #Inovice DateをDatetime型に変更
    df['Invoice Date'] = pd.to_datetime(df['Invoice Date'])
    print(df.info())

    df['day of week'] = df['Invoice Date'].dt.day_name()

    df['year'] = df['Invoice Date'].dt.year
    df['month'] = df['Invoice Date'].dt.month

    df2 = df.set_index("Invoice Date")
    print(df.head())
    #df = df.fillna(0)
    #indexの日付を月でリサンプリングしたデータフレームdf_month
    df_month = df2.resample('M').sum()

    #ここまでデータ整形

    #ここからUI表示を含む処理
    
    #日付選択
    #today = datetime.date.today()
    #start_date = st.date_input('date from', df['Invoice Date'].min())
    #end_date = st.date_input('date until', today)
    #df2 = df[df['Invoice Date'].between(pd.to_datetime(start_date), pd.to_datetime(end_date))]
    

    #multiselect, listを返す
    options = st.multiselect(
        'Select CEMIS code',
        ['AC', 'AD', 'AJ', 'AO','BM','BO','BQ','CD','CQ','PJ','VC'],
        ['AC', 'AD', 'AJ', 'AO','BM','BO','BQ','CD','CQ','PJ','VC']
    )
    #options.insert(0,'day of week')
    #streamlitにデータフレームとグラフを出力
    st.header('Count of repair')
    st.dataframe(df2[options])
    st.text('simple analysis')
    st.dataframe(df2[options].describe())

    #st.line_chart
    st.header('Repair counts by month')
    chart_data = df_month[options]
    st.area_chart(chart_data)

    month = st.slider(
        'value of SMA window',
        1, 12)
    st.header('Single Moving Average (SMA)')
    chart_data2 = df_month[options].rolling(month).mean()
    st.line_chart(chart_data2)

    #prophetでの時系列予測を出す。一つのSeriesしかできないので一つ選ばせる
    st.header('Prediction of the number')
    prophet_option = st.selectbox(
        'Select CEMIS code',
        ('AC', 'AD', 'AJ', 'AO','BM','BO','BQ','CD','CQ','PJ','VC')
    )

    if st.button("Predict button"):
        data = df[['Invoice Date', prophet_option]]
        #st.dataframe(df[['Invoice Date', prophet_option]])
        data.columns = ['ds', 'y'] #prophetのためにds, yにカラム名を変更
        #st.write(data.y.mean()/8)
        data = data[data.y > (data.y.mean()/4)]
        #st.dataframe(data)
        
        #約２年間のデータを訓練用に使用
        data_train = data[:730]

        m = Prophet(weekly_seasonality=True, daily_seasonality=True)
        m.fit(data_train)
        
        st.header("Prophet prodiction info")
        future = m.make_future_dataframe(periods=len(data_train), freq='D')
        predict = m.predict(future)
        st.dataframe(predict)

        fig1 = m.plot(predict)
        fig2 = m.plot_components(predict)
        st.pyplot(fig1)
        st.pyplot(fig2)


