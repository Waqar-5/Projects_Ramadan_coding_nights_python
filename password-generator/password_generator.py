import streamlit as st # importing the streamlit ibrary for creating the web app
import random # importing the random number library for generating random vharacters
import string # provide special letters / importing the string library for using string characters

# Function to generate a password based on the user's perference
def generator_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Includes all letters (a-z, A-Z, )

    if use_digits:
        characters += string.digits # add numbers (0-9) if selected

    if use_special:
        characters += string.punctuation # add special characters (!,@,#,$,%,^,&,*) if selected

# generate random password of the specified length the characters defined above
    return ''.join(random.choice(characters) for _ in range(length))

# title of web app
st.title("Password Generator")

length = st.slider("Select Password Length", min_value=6, max_value=32, value=12)

use_digits = st.checkbox("Include Digits")

use_special = st.checkbox("Include special Characters")

if st.button("Generator Password"):
    password = generator_password(length, use_digits, use_special)
    st.write(f"Generated Password: `{password}`")

st.write("----------------------------------")

st.write("Build with ❤️ by [Waqar Ali](https://hithub.com/Waqar-5)")