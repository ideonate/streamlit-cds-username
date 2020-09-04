import streamlit as st
import cds_username from cds_username

st.subheader("Username test")

# Create an instance of our component with a constant `name` arg, and
# print its output value.
username = cds_username()
st.markdown("Username is %s!" % username)
