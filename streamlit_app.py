import streamlit as st
import os
import pandas as pd

#Page Name
st.set_page_config(
    page_title="Alzheimer's Disease Awareness",  # Set the title in the browser tab
    page_icon="🧠",  
    layout="wide")

st.sidebar.header("Alzheimer Help") #Sets sidebar name to "Alzheimer Help"
st.sidebar.page_link("streamlit_app.py", label="Home", icon="🏠")
if st.sidebar.button("🏠 ome"):
    st.load_page("medication.py")
st.sidebar.page_link("medication.py", label="Medication", icon="💊")
st.sidebar.page_link("schedule.py", label="Schedule", icon="📅")
st.sidebar.page_link("settings.py", label="Settings", icon="⚙️")

#Functions
def main_menu_UI():
    st.title("--- Alzheimer help ---")
    st.divider()

def main():
    main_menu_UI()


#Call main
main()





#Todo: 
#Rewrite validation for daily routine, HHMM format, etc.
#Refine input validation for account creation, email validation, etc.
#Set up streamlit UI
#GPS tracking 
#Daily routine
#Reminders
#Move main menu UI in main() to user_interface()
#Admin account that can delete accounts?
#Allow user to go back to main menu in the sub-menus.
#Add file close() everywhere it is missing.
#Optimise the code, make it neater.
#Add a way to go back to the main menu in all sub-menus.
#Fix delete event
#Add edit event function
#Add view events function