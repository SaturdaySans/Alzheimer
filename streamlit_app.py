import streamlit as st
import os
import pandas as pd

#Page Name
st.set_page_config(
    page_title="Alzheimer's Disease Awareness",  # Set the title in the browser tab
    page_icon="🧠",  
    layout="wide")


#Functions
def main_menu_UI():
    st.title("--- Alzheimer help ---")
    st.divider()
    st.page_link("pages/settings.py", label="Settings")
    st.page_link("pages/schedule.py", label="Schedule")
    st.page_link("pages/medication.py", label="Medication")

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