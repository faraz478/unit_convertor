import streamlit as st

st.title("🌍 Unit Convertor App")
st.markdown("## Converts Length, Weight, Time, Temprature instantly")
st.write(" Welcome! Select a Category, enter a value and get the converted value instant.")

category = st.selectbox("Choose a Category", ["📏Length", "⚖Weight", "🕤Time", "🌡️Temperature"])

def convert_units(category, value, unit):
    if category=="📏Length":
        if unit== "Kilometers to miles":
            return value *0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        
    elif category=="⚖Weight":
        if unit =="Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "🕤Time":
        if unit=="Seconds to minutes":
            return value /60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24

    elif category == "🌡️Temeprature":
        if unit == "Celcius to Fahrheneite":
            return value* 9/5 + 32
        elif unit == "Fahrheneite to celcius":
            return (value-32)* 5/9
        

if category=="📏Length":
 unit=st.selectbox("Select Conversion",["Kilometers to miles", "Miles to Kilograms"])

elif category=="⚖Weight":
 unit=st.selectbox("Select Conversion",["Kilograms to Pounds", "Pounds to Kilograms"])

elif category =="🕤Time":
 unit=st.selectbox("Select conversion",["Seconds to minutes","Minutes to seconds","Minutes to hours","Hours to minutes","Hours to days","Days to hours"])

elif category =="🌡️Temprature":
 unit=st.selectbox("Select conersion",["Celsius to Fahrheneite","Fahrheneite to celsius"])


value = st.number_input("Enter the value to convert")

if st.button("Convert"):
   result=convert_units(category,value,unit)
   st.success(f"The result is {result:2f}")
        

                  