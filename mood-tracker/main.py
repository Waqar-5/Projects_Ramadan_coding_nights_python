import streamlit as st # for creating web interface
import pandas as pd # for data manipulation
import datetime # for handling dates
import csv # for reading and writing CSV file
import os # for file operations

# Define the file name for strong mood data
MOOD_FILE = "mood_log.csv"

# function to read mood data from the CSV file
def load_mood_data():
    # check if the file exist
    if not os.path.exists(MOOD_FILE):
        # if not file, create empty dataframe with columns
        return pd.DataFrame(columns=["Date", "Mood"])
    # read and return existing mood data
    return pd.read_csv(MOOD_FILE)

# Function to add new mood entry to CSV file
def save_mood_date(data, mood):
    #  Open file in append mood
    with open(MOOD_FILE, "a") as file:
        
        # Create CSV writer
        writer = csv.writer(file)

        # Add new mood entry 
        writer.writerow([data, mood])
        
# Streamlit app title
st.title("Mood Tracker 😊")

# Get Today's date
today = datetime.date.today()

# Create subheader for mood input
st.subheader("How are you feeling today?")

# Create dropdown for mood selection
mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Neutral"])

# Create button to save mood
if st.button("Log Mood"):

# Save mood when button is clicked
    save_mood_date(today, mood)

    # Show success message
    st.success("Mood Logged Successfully!")

# Load existing mood data
data = load_mood_data()

# if there is data to display
if not data.empty:

    # Create subheader for mood trends
    st.subheader("Mood Trends Over Time")

    # Convert date strings to datatime Objects
    data["Date"] = pd.to_datetime(data["Date"])

    # count frequency of each mood
    mood_counts = data.groupby("Mood").count()["Date"]

    # Display Line chart of mood trends over time 
    st.bar_chart(mood_counts)

    # Build with love by Waqar Ali
    st.write("Built with 💖 by Waqar Ali")
    
