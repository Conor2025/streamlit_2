import streamlit as st
st.title("Hello World")

user_input = st.text_input("Enter your name")
st.write("This is ", user_input)


