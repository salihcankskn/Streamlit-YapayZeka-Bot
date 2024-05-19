# ( python -m streamlit run geminiresim.py )#çalıştırmak için terminale yazılacak

import streamlit as st
from PIL import Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyD6SnncAftrvkVUVEBLutrOh9YxpJ0OETE")
#google generativeden yeni key alınmalı 

st.title("Gemini İle Resim Analizi")
model=genai.GenerativeModel("gemini-pro-vision")

resim=st.file_uploader("Bir resim Yükleyiniz",type=["jpg","png","jpeg"])

if resim is not None:
    img=Image.open(resim)
    st.image(img)

soru=st.text_input("Sorunu Sor")
if st.button("Sor"):
    cevap=model.generate_content([soru,img],stream=True)
    cevap.resolve()
    st.write(cevap.text)

    #yüklenilen resim hakkında sorular sorup bilgi alabileceğimiz bir bir proje