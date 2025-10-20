# components.py
import streamlit as st
from typing import List

def section_title(title: str, emoji: str = "⭐"):
    st.markdown(f"<h2>{emoji} {title}</h2>", unsafe_allow_html=True)

def card(title: str, subtitle: str = "", meta: str = "", bullets: List[str] = None):
    st.markdown(
        f"""
        <div style="
            border:1px solid rgba(255,255,255,0.1);
            background:rgba(255,255,255,0.02);
            border-radius:16px;padding:16px;margin:10px 0;">
            <b>{title}</b><br>
            <span style='opacity:0.85'>{subtitle}</span><br>
            <span style='opacity:0.6;font-size:0.9rem'>{meta}</span>
        </div>
        """, unsafe_allow_html=True)
    if bullets:
        for b in bullets:
            st.markdown(f"- {b}")

def pill(text: str):
    st.markdown(
        f"""
        <span style="
            display:inline-block;padding:4px 10px;margin:4px;
            border-radius:10px;background:#0078D7;color:#fff;
            font-size:12px;">{text}</span>
        """,
        unsafe_allow_html=True,
    )
