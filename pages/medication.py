import streamlit as st
import os
import pandas as pd

st.title("---Medication Tracker---")

file_path = "medication.csv"

# Load CSV if it exists, otherwise create an empty DataFrame
if os.path.exists(file_path):
    try:
        medication = pd.read_csv(file_path)
        if medication.empty:
            st.warning("The CSV file is empty.")
    except Exception as e:
        st.error(f"Error reading file: {e}")
        medication = pd.DataFrame(columns=["Medication", "Time", "Taken", "UID"])
else:
    medication = pd.DataFrame(columns=["Medication", "Time", "Taken", "UID"])  # Empty DataFrame

# Get the current user's UID from session state
current_user_uid = str(st.session_state.get('UID', ''))  # Ensure it's a string

# Ensure the user is logged in and has a UID
if not current_user_uid:
    st.warning("Please log in to view your medication tracker.")
else:
    # Ensure the UID in the medication DataFrame is also a string
    medication['UID'] = medication['UID'].astype(str)

    # Drop rows where 'UID' is missing or empty
    medication = medication.dropna(subset=['UID'])

    # Check if current_user_uid exists in the DataFrame and filter by it
    if current_user_uid in medication['UID'].values:
        # Filter medications for the current user's UID
        medication_for_user = medication[medication['UID'] == current_user_uid]

        # Display medication list with checkboxes
        updated_status = []

        for index, row in medication_for_user.iterrows():
            checked = st.checkbox(f"{row['Medication']} ({row['Time']})", value=(row['Taken'] == "Yes"), key=index)
            updated_status.append("Yes" if checked else "No")

        # Update the DataFrame with the new values
        if st.button("Update Medication Status"):
            medication.loc[medication['UID'] == current_user_uid, "Taken"] = updated_status
            medication.to_csv(file_path, index=False)
            st.success("Medication status updated!")
    else:
        st.error("No medications found for the current user.")
