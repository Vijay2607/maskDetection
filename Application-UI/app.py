import streamlit as st

# Custom imports 
from multipage import MultiPage
from pages import qr_code_generator, feedback, mask_detection, social_distancing

# Create an instance of the app 
app = MultiPage()

# Title of the main page
# st.markdown("Prevention of covid-19")
# Add all your applications (pages) here

app.add_page("Registration Form", qr_code_generator.app)
app.add_page("Feedback", feedback.app)
app.add_page("Mask Detection", mask_detection.app)
app.add_page("Social Distancing", social_distancing.app)


# The main app
app.run()