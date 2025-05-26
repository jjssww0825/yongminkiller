import streamlit as st
st.title('나의 첫 Streamlit 앱')
st.write('안녕하세요!')
import pandas as pd
import streamlit as st
import plotly.express as px

# Google Drive CSV 링크
CSV_URL = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

# 데이터 불러오기
@st.cache_data
def load_data():
    return pd.read_csv(CSV_URL)

df = load_data()

# 앱 UI
st.title("📊 Plotly 시각화 웹앱 (Google Drive CSV)")
st.markdown("Google Drive에서 데이터를 불러와 Plotly로 시각화합니다.")

# 데이터 미리보기
st.subheader("🔍 데이터 미리보기")
st.dataframe(df)

# 컬럼 선택
columns = df.columns.tolist()
x_axis = st.selectbox("X축 변수 선택", options=columns)
y_axis = st.selectbox("Y축 변수 선택", options=columns)
color_by = st.selectbox("색상 그룹 변수 선택 (선택)", options=[None] + columns)

# 그래프 종류 선택
chart_type = st.radio("그래프 종류", ["Scatter", "Line", "Bar"])

# 그래프 출력
st.subheader("📈 시각화 결과")
if chart_type == "Scatter":
    fig = px.scatter(df, x=x_axis, y=y_axis, color=color_by)
elif chart_type == "Line":
    fig = px.line(df, x=x_axis, y=y_axis, color=color_by)
elif chart_type == "Bar":
    fig = px.bar(df, x=x_axis, y=y_axis, color=color_by)

st.plotly_chart(fig, use_container_width=True)
