import streamlit as st # we can write anything in the place of st(streamlit)
# streamlit is a Library for building web apps

# function to conert units based on predefined conversions factors or formulas
def converter_units(value, unit_from, unit_to):

    conversions = {
        "meters_kilometers": 0.001, # 1 meter = 0.001 kilometer
        "kilometers_meters": 1000, # 1 kilometer = 1000 meter
        "grams_kilograms": 0.001, # 1 gram = 0.001 kilogram
        "kilograms_grams": 1000 # 1 kilogram = 1000 gram
    }

    key = f"{unit_from}_{unit_to}" # generate a unique key for the conversation or a key based on the input and output units 

        # logic to convert unitsz
    if key in conversions:
        conversion = conversions[key]  # storing above units values in conversion variable in key
        return value * conversion
    else:
        return "Conversion not supported" # retrun a message if the conversion is not supported
    
st.title("Unit Converter") # set the title of the web app

# user input: numerical value to convert
value = st.number_input("Enter the value: ", min_value=1.0, step=1.0) 

# dropdown to select units to convert from
unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms"])

# dropdwon to select units to convert to
unit_to = st.selectbox("Convert to: ", ["meters", "kilometers", "grams", "kilograms"])

# button to trigger the conversion
if st.button("Convert"):
    result = converter_units(value, unit_from, unit_to) # call the conversion function
    st.write(f"Converted value: {result}")# display the result or show the result