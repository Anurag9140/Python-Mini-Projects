import googletrans
import asyncio

async def main():
    translator = googletrans.Translator()
    print(googletrans.LANGUAGES)

    translated = await translator.translate("HOW ARE YOU", dest='hi')
    print(translated.text)

asyncio.run(main())

import streamlit as st
import googletrans
import asyncio

translator = googletrans.Translator()

def get_key(val):
    for key, value in googletrans.LANGUAGES.items():
        if val == value:
            return key
    return "key doesn't exist"

st.markdown(
    """
    <style>
        .stApp {
            background-color:black;
        }
        
        
    </style>
    """,
    unsafe_allow_html=True
)

option = st.selectbox('Select Language', tuple(googletrans.LANGUAGES.values()))
text = st.text_area('Input Your Text Here')

if text: 
    translated = asyncio.run(translator.translate(text, dest=get_key(option)))
    st.write(translated.text)

