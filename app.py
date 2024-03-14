import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from predict_stock import show_predict_stock_page



page = st.sidebar.selectbox("Explore Salary or Predict Salary or Predict Stock Price", ("Predict Salary", "Explore Salary", "Predict Stock Price"))

if page == "Predict Salary":
    show_predict_page()
elif page == "Explore Salary":
    show_explore_page()
else:
    show_predict_stock_page()
