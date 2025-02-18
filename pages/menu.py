import streamlit as st
import os
import pandas as pd


st.title("--- Alzheimer help ---")
st.divider()
st.page_link("pages/settings.py", label="Settings", icon="⚙️")
st.page_link("pages/routine.py", label="Routine", icon="🗓️")
st.page_link("pages/events.py", label="Events", icon="📆")  
st.page_link("pages/medication.py", label="Medication", icon="💊")
