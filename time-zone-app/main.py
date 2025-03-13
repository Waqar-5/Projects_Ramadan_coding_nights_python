# Required libraries
import streamlit as st #Streamlit is used for creating web applications 
from datetime import datetime # Used for handling date and time functionalities
from zoneinfo import ZoneInfo # Provides timezone information for different locations

# Define a list of different time zones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
    "Asia/Riyadh"
]

# Application title
st.title(" 🌏 Time Zone App")
# A multi-select widget to allow users to select multiple time zones
selected_timezone = st.multiselect(
    "Select Timezones", # Label for the dropdow
     TIME_ZONES,  # List of available time zones
     default=["UTC", "Asia/Karachi"]) # Default selected time zones 

# Display the selected Timezones
st.subheader("Selected Timezones")

# Loop through each selected time zone and display the current time
for tz in selected_timezone:

    # Get and format current time for each time between timezones with AM/PM
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")
    # display the current time for each selected timezones
    st.write(f"**{tz}**: {current_time}")

# A subheader for converting time between timezones
st.subheader("Convert Time Between Timezones")

# Create a time input widget for the current time
current_time = st.time_input(
    "Current Time", # Label for the input field
     value=datetime.now().time()) # Default value: current local time

# create a selectbox for selecting the timezone to convert **from**
from_tz = st.selectbox(
    "From Timezone",  # Label for the select box
     TIME_ZONES,   # List of available time zones
     index=0) # Default selection (UTC)

# # create a selectbox for selecting the timezone to convert **to**
to_tz = st.selectbox(
    "To Timezone",  # Label for the select box
     TIME_ZONES,   # List of available time zones
      index=1) # Default selection (Asia/Karachi)

# Create a button to trigger the time conversation
if st.button("Convert Time"):

    # Combine the selected date with the time and assign it the selected "from" timezone
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))

     # Convert the time to the target "to" timezone
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")

    # Display the converted time in the selected target timezone
    st.success(f"Converted Time in {to_tz}: {converted_time}")