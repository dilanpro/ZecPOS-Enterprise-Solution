import streamlit as st
from pywebio import *
from pywebio.input import *
from pywebio.output import *

# Define Pywebio widget for selecting a date range
def select_date_range():
    start_date = input("Start Date", type=DATE)
    end_date = input("End Date", type=DATE)
    return (start_date, end_date)

# Streamlit app
def app():
    # Use Streamlit to build main UI
    st.title("My Streamlit + Pywebio App")
    name = st.text_input("What's your name?")
    st.write("Hello,", name)

    # Use Pywebio to build custom widget
    start_date, end_date = select_date_range()
    st.write("Selected date range:", start_date, "to", end_date)

# Start Streamlit app
if __name__ == '__main__':
    app()
