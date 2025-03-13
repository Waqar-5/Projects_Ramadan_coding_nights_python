import streamlit as st # for ui purposes
import random # used for generate random number
import time # used time related working or functionlities
import requests # used for calling api to get sort of data from internet or fromany specific api

st.title("Money Making Machine 📠")

def generate_money():
    # randint method in random module is used to generate specific integer between specific set of values
    return random.randint(1, 1000)
# used to provide subheading
st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("Counting your money...")
    # sleep method is used for delaying 
    time.sleep(1) # 1 = 1 second
    amount = generate_money()
    # Show success message on screen
    st.success(f"You made ${amount}!")

# api calling
def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustle"]
        else:
            return("Freelancing")

    except:
        return ("Something went wrong!")

st.subheader("Side Hustle Ideas")
if st.button("Genrate Hustle"):
    idea =fetch_side_hustle()
    st.success(idea)

def fetch_money_quotes():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:
            quotes = response.json()
            return quotes["money_quote"]
        else:
            return ["Money is the root of all evil!"]
    except:
        return("Something went wrong!")

st.subheader("Money-Making Motivation")
if st.button("Get Inspired"):
    quote = fetch_money_quotes()
    st.info(quote)
    # st.warning(quote)