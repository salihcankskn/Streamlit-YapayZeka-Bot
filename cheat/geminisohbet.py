# ( python -m streamlit run geminisohbet.py )  çalıştırmak için terminale yazılacak

import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyD6SnncAftrvkVUVEBLutrOh9YxpJ0OETE")
#poogle genarativeden yeni key alınmalı

st.title("Gemini İle Sohbet Edelim")
model=genai.GenerativeModel("gemini-1.5-pro-latest")

chat=model.start_chat(history=[])

soru=st.text_input("Geminiye Bir Soru Sor")
if st.button("Sor"):
    cevap=chat.send_message(soru)
    st.write(cevap.text)
    chat.history.append(cevap)
    st.write(chat.history)


    #bir yapay zeka botu projesi