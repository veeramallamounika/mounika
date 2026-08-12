import streamlit as st
import requests

st.title("🍔 Food Delivery App")

response = requests.get("http://127.0.0.1:8000/foods")

foods = response.json()

st.subheader("Available Food")

for food in foods:
    st.write(f"### {food['name']}")
    st.write(f"Price: ₹{food['price']}")
    st.button("Add to Cart", key=food["id"])