# utils.py
import requests
import streamlit as st

@st.cache_data
def load_lottie_url(url: str):
    """Loads Lottie animation from a URL"""
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
