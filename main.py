#library
import numpy as np
import pandas as pd
import streamlit as st

from fbprophet import Prophet
from fbprophet.diagnostics import performance_metrics
from fbprophet.diagnostics import cross_validation
from fbprophet.plot import plot_cross_validation_metric

from datetime import datetime as dt

import base64

#side python files
import CEMIScount
import RCCcount

add_selectbox = st.sidebar.selectbox("Menu",
    ("CEMIS repair count","RCC repair count")
)

if add_selectbox == "CEMIS repair count":
    CEMIScount.CEMIS()
if add_selectbox == "RCC repair count":
    RCCcount.RCC()
