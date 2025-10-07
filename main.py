import streamlit as st
from utils import generate_xiaohongshu

import os

st.header("AI 職缺寫手 ✏️")
# with st.sidebar:
#     openai_api_key = st.text_input("請輸入OpenAI API密鑰: ", type="password")
#     st.markdown("[獲取OpenAI API密鑰](https://platform.openai.com/api-keys)")

theme = st.text_area("主題").strip()
submit = st.button("開始寫作")

openai_api_key = os.getenv("OPENAI_API_KEY")

if submit and not openai_api_key:
    st.info("請輸入你的OpenAI API密鑰")
    st.stop()
if submit and not theme:
    st.info("請輸入生成內容的主題")
    st.stop()
if submit:
    with st.spinner("AI正在努力創作中，請稍等..."):
        theme = theme + "以上，請設計求職文宣。"
        result = generate_xiaohongshu(theme, openai_api_key)
    st.divider()
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("##### 標題1")
        st.write(result.titles[0])
        st.markdown("##### 標題2")
        st.write(result.titles[1])
        st.markdown("##### 標題3")
        st.write(result.titles[2])
        st.markdown("##### 標題4")
        st.write(result.titles[3])
        st.markdown("##### 標題5")
        st.write(result.titles[4])
    with right_column:
        st.markdown("##### 正文")
        st.write(result.content)