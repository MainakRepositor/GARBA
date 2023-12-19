"""This is the main module to run the app"""

# Importing the necessary Python modules.
import streamlit as st

# Import necessary functions from web_functions
from web_functions import load_data

# Import pages
from Tabs import home, data, predict, visualise

# Configure the app
st.set_page_config(
    page_title = 'Gamma Ray Burst Anticipator',
    page_icon = '🌟',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

# Dictionary for pages
Tabs = {
    "Home": home,
    "Prediction": predict,
    "Visualisation": visualise
    
}

# Create a sidebar
# Add title to sidear
st.sidebar.title("Navigation")

st.sidebar.image("./images/home.png")

# Create radio option to select the page
page = st.sidebar.radio("Pages", list(Tabs.keys()))

# Loading the dataset.
df, X, y = load_data()

# Call the app funciton of selected page to run
if page in ["Prediction", "Visualisation"]:
    Tabs[page].app(df, X, y)
else:
    Tabs[page].app()
