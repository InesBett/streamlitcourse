import streamlit as st
import random
###################################### PAGE SETUP ############################################

# Set up the page
st.set_page_config(
    page_title="Superhero Name",
    layout="wide", # or wide
    page_icon="🦸", # choose your favorite icon
    initial_sidebar_state="collapsed" # or expanded
)

#################################### APPLICATION ################################################
#Predefined list of superhero catchpharses

catchphrases= [
    "Saving the world, one step at a time",
    "With great power comes great responsability",
    "Justice is my middle name",
    "Evil doesn't stand a chance!",
    "I'm not just ahero, I'm a legend!"
]

#################################### USER INPUTS ################################################

st.title("What's your Superhero Name?🦸🦸")

#inputs for superhero name
favorite_color= st.text_input("", placeholder="What's your favorite color?")
favorite_animal= st.text_input("", placeholder="What's your favorite animal?")
lucky_number= st.number_input("Enter your lucky number:", min_value=1, step=1, value=7)

#dropdown for superpower
superpower= st.selectbox("Choose your superpower:",
                        ["Flying", "Invisibility", "Super Strengh", "Mind Control", "Time Travel"])

#Generate superhero name on button click
if st.button("Generate My Superhero Name")== True:
    superhero_name= f"{favorite_color}{favorite_animal} of {lucky_number}"
    st.header(f"🦸 Your Superhero Name: {superhero_name}")
    st.write(f"🌟Superpower: {superpower}")

    #Display a motto
    st.subheader("Your Superhero Motto:")
    st.write(f'"Whith great power comes great {superpower.lower()}!"')
             
# Generate Random catchphrases

if st.button("Generate Random Superhero Catchphrase"):
    st.write(f"Catchphrase: *{random.choice(catchphrases)}*")