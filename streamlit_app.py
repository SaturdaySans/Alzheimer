import streamlit as st
import os
import pandas as pd

#Page Name
st.set_page_config(
    page_title="Alzheimer's Disease Awareness",  # Set the title in the browser tab
    page_icon="🧠",  
    layout="wide",
    initial_sidebar_state="auto")

pg=st.navigation([
    st.Page("streamlit_app.py", title="Main Menu", icon="🏠"),
    st.Page("pages/medication.py", title="Medication", icon="💊"),
    st.Page("pages/events.py", title="Events", icon="📆"),
    st.Page("pages/routine.py", title="Routine", icon="🗓️"),
    st.Page("pages/settings.py", title="Settings", icon="⚙️"),
])


#def side_bar_UI():
    #st.sidebar.header("Alzheimer Help")  # Sets sidebar name to "Alzheimer Help"
    #st.sidebar.page_link("streamlit_app.py", label="Home", icon="🏠")
    #st.sidebar.page_link("pages/medication.py", label="Medication", icon="💊")
    #st.sidebar.page_link("pages/routine.py", label="Routine", icon="🗓️")  
    #st.sidebar.page_link("pages/events.py", label="Events", icon="📆")  
    #st.sidebar.page_link("pages/settings.py", label="Settings", icon="⚙️")



#Functions
def main_menu_UI():
    #st.image("resources/banner.png", use_container_width=True)
    st.title("--- Alzheimer help ---")
    st.divider()
    st.page_link("pages/settings.py", label="Settings", icon="⚙️")
    st.page_link("pages/routine.py", label="Routine", icon="🗓️")
    st.page_link("pages/events.py", label="Events", icon="📆")  
    st.page_link("pages/medication.py", label="Medication", icon="💊")

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
