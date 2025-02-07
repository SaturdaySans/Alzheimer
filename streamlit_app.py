import streamlit as st
import os
import pandas as pd

#Variables
assert os.path.exists("daily_routine.csv"), "File not found!"
login_account = None
accounts = pd.read_csv("accounts.txt")
routine = pd.read_csv("daily_routine.csv")

#Functions
def main_menu_UI():
    st.title("--- Alzheimer help ---")
    st.divider()
    st.page_link("pages/settings.py", label="Settings")
    st.page_link("pages/schedule.py", label="Schedule")

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