import streamlit as st

st.title("📋 Notice Board")

uploaded_file = st.file_uploader("Upload a notice image", type=["jpg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Notice")
    st.success("Notice uploaded!")
