import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import pyqrcode
import png
import smtplib
import imghdr
from email.message import EmailMessage
from PIL import Image

import csv

def app():
    st.title("Feedback Request")
    st.subheader("Your opinion matters")
    st.markdown("Help us to improve our product? Give us your valuable feedback")
    rating = st.radio(
    "Your Rating",
    ('Very Good', 'Good', 'Mediocre', 'Bad', 'Very Bad'))
    if rating == 'Very Good':
        st.write('You selected Very Good.')
    elif rating == 'Good':
        st.write('You selected Good.')
    elif rating == 'Mediocre':
        st.write('You selected Mediocre.')
    elif rating == 'Bad':
        st.write('You selected Bad.')
    elif rating == 'Very Bad':
        st.write('You selected Very Bad.')
    else:
        st.write("You didn't select.")
    
    msg = st.text_area('What could we improve?', placeholder='Your valuable suggestion')
    if rating == '' or msg == '':
        st.warning("All input field must be filled out before submitting the feedback")
    elif st.button('Submit Feedback'):
         st.success('We received your valuable feedback!')
         row = [rating, msg]
         # open the file in the write mode
         with open('feedback.csv', 'a', newline='') as f:
              # create the csv writer
              writer = csv.writer(f)
              # write a row to the csv file
              writer.writerow(row)
    
    
    

    df = pd.read_csv("feedback.csv")
    st.write(df)

    very_good = 0
    good = 0
    mediocre = 0
    bad = 0
    very_bed = 0
    
    for rate in df['rating']:
        if rate == 'Very Good':
            very_good = very_good + 1
        elif rate == 'Good':
            good = good + 1
        elif rate == 'Mediocre':
            mediocre = mediocre + 1
        elif rate == 'Bad':
            bad = bad + 1
        else:
            very_bed = very_bed + 1

    

    st.write("\n")
    st.write("\n")
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Very Good', 'Good', 'Mediocre', 'Bad', 'Very Bad'
    sizes = [very_bed, good, mediocre, bad, very_bed]
    explode = (0, 0, 0, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)
    