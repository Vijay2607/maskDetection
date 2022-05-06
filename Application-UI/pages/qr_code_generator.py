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



def app():
    st.title('User Registration')
    
    user_name = st.text_input('Enter name', '', placeholder='name')
    user_email = st.text_input('Enter email address ', '', placeholder='name@gmail.com')
    user_moblie = st.text_input('Enter mobile number ', '', placeholder='+917428806557')
    user_roll = st.text_input('Enter roll no ','', placeholder='191IT142')

    user_status = st.selectbox(
        "Vaccination Status",
        ('Not Vaccinated', 'Partially Vaccinated', 'Fully Vaccinated'))

    st.write('You selected:', user_status)

    if user_name == '' or user_email == '' or user_status == '' or user_moblie == '' or user_roll == '':
        st.warning("All input field must be filled out before submitting the form")
    else:
        if st.button('Generate QR Code'):
            st.subheader("User Details:")
            st.write("Name : ", user_name)
            st.write("Email : ", user_email)
            st.write("Mobile : ", user_moblie)
            st.write("Roll No : ", user_roll)
            st.write("Vaccination Status : ", user_status)
            s = user_name + ' is ' + user_status + ".\n" + "Moblie Number : " + user_moblie + "\n" + "Roll No : " + user_roll 
            url = pyqrcode.create(s)
            #saving image
            img = "qr-code.png"
            url.png(img, scale=10)

            #opening image
            # image = Image.open('qr-code.png')
            # st.image(image, caption='QR Code')

            Sender_Email = "arena.developer.social@gmail.com"
            Reciever_Email = user_email
            Password = "Ritesh@0611"

            newMessage = EmailMessage()                         
            newMessage['Subject'] = "Registration Successful" 
            newMessage['From'] = Sender_Email                   
            newMessage['To'] = Reciever_Email                   
            newMessage.set_content('Find your QR Code below!\n Please do not share this as it is uniquely generated for you to get entry into your esteemed institutions.') 

            with open('qr-code.png', 'rb') as f:
                image_data = f.read()
                image_type = imghdr.what(f.name)
                image_name = f.name

            newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(Sender_Email, Password)              
                smtp.send_message(newMessage)
            st.success('QR code sent successfully!')



