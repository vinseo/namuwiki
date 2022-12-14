#import settings
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
from bokeh.plotting import figure

#data loading
# st.cache를 이용하여 데이터 로딩을 하는 함수
@st.cache #데이터를 불러와서 메모리에 가지고 있는 것 (매번 불러오기 번거롭기 때문)
def load_data(filename):
    data = pd.read_csv(filename)
    return data

#df0 = load_data("")
#df = df0.copy()

st.subheader("2022-2 데이터 저널리즘 과제전")
st.title("나무위키 활용 학습의 가능성과 한계")
st.write("10조: 서정빈, 신부경, 정민제")

#문제의식 서술
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("### 문제의식")

#데이터 소개
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("### 데이터 소개")

#데이터 분석
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("### 데이터 분석 결과")
