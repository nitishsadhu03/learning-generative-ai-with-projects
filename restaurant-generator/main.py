import streamlit as st
import langchain_helper

st.title("Restaurant Name And Menu Generator 😋")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Chinese", "Arabic", "American", "Thai", "Greek", "French", "Turkish", "Korean"))


if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)

    st.header(response['restaurant_name'].strip())

    st.divider()

    st.subheader("Menu Items")
    st.write(response['menu_items'].strip())
