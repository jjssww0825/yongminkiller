import streamlit as st
st.title('나의 첫 Streamlit 앱')
st.write('안녕하세요!')
import pandas as pd
import plotly.express as px
import streamlit as st

# Google Drive CSV 불러오기
url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
df = pd.read_csv(url)

st.title("📊 Google Drive CSV Plotly 시각화 웹앱")
st.write("데이터를 선택하여 시각화할 수 있는 웹앱입니다.")

# 데이터 확인
st.subheader("🔍 데이터 미리보기")
st.dataframe(df.head())

# 사용자 선택
cols = df.columns.tolist()
x = st.selectbox("X축 변수", options=cols)
y = st.selectbox("Y축 변수", options=cols)
color = st.selectbox("색상 구분 (선택)", options=[None] + cols)

# 그래프 시각화
st.subheader("📈 Plotly 그래프")
fig = px.scatter(df, x=x, y=y, color=color)
st.plotly_chart(fig)
