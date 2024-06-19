import streamlit as st
import Langchain_helper
st.title("Restaurant Name Generator and Main Menu") 
cuisine = st.sidebar.selectbox("Pick a Cusine",("Indian","Italian","Arabic","American","Mexican","Chinese","Korean"))


if cuisine:
    response = Langchain_helper.J_I(cuisine)
    st.header(response['restaurant_name'].strip(""))
    menu_items=response['menu_items'].strip("").split(",")
    st.write("***Menu Items***")
    for item in menu_items:
        st.write("-",item)
