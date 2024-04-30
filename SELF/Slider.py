import streamlit as st

st.title(":rainbow[Hello World]")
st.header('welcome to streamlit')

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
