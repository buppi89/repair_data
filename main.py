import numpy as np
import pandas as pd
import streamlit as st
from datetime import datetime as dt
import CEMIScount
import RCCcount

add_selectbox = st.sidebar.selectbox("Menu",
    ("CEMIS repair count","RCC repair count")
)

if add_selectbox == "CEMIS repair count":
    CEMIScount.CEMIS()
if add_selectbox == "RCC repair count":
    RCCcount.RCC()
