# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 18:32:12 2021

@author: mraslan
"""

import ccxt
from crypto1 import crypto
import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
from crypto_func import BTC_drop_change,group_tweets,plot_bokeh
from datetime import datetime
quote=st.selectbox('Symbol',['USDT','BTC'])
percentage=st.number_input('Enter percantage for orderbook aggregation',0.5)


@st.cache(allow_output_mutation=True)
def OHLCV(percentage,quote,time_tuple=(2021, 3, 20, 00, 00, 00, 0, 00, 0),tf='1h'):
        a=crypto('binance',quote)  
        df_tweet=a.get_tweets()
        #time_tuple=(2021, 3, 30, 00, 00, 00, 0, 00, 0)
        into,outfrom=group_tweets(df_tweet,coin,tf)
        OHLCV=a.get_OHLCV(time_tuple,tf)
        return OHLCV,into,outfrom

time_tuple=(2021, 3, 20, 00, 00, 00, 0, 00, 0)
coin=st.text_input('Enter the coin you want to check from whale bot','BTC')

tf=st.text_input('Time frame (1m/1h/4h/1d/1w)','1h')
OHLCV,into,outfrom=OHLCV(percentage,quote,time_tuple,'1h')

start = st.text_input("start date",'2021-04-13 12:00:00')
#start = datetime.strptime(start, 'yyyy-mm-dd %H:%M:%S')
start=pd.Timestamp(start)
print(OHLCV.head())
print(start)
end = st.text_input("End date",'2021-04-13 14:00:00')
end=pd.Timestamp(end)

change_low=st.number_input('enter the change in percentage to search for ',-100)
change_high=st.number_input('enter the change in percentage to search for ',-99)

OHLCV_change=BTC_drop_change(OHLCV,start,end,change_low,change_high)
st.dataframe(OHLCV_change.set_index('Date'))
symbol=st.text_input('input the symbol to be checked','BTC/USDT')
df=OHLCV[OHLCV['symbol']==symbol]
p=plot_bokeh(into,outfrom,df)
#st.bokeh_chart(p)
#show(p)