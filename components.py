import streamlit as st

def section_title(title, icon=""):
    st.markdown(f"""
    <h2 style='margin-top:30px;'>{icon} {title}</h2>
    """, unsafe_allow_html=True)

def card(title, subtitle, meta, bullets):
    st.markdown(f"""
    <div style="
        background-color:#111827;
        padding:20px;
        border-radius:12px;
        margin-bottom:20px;
        border:1px solid #1f2937;
    ">
        <h3 style="margin-bottom:5px;">{title}</h3>
        <p style="color:#9CA3AF; margin:0;">{subtitle}</p>
        <p style="color:#6B7280; font-size:13px;">{meta}</p>
    """, unsafe_allow_html=True)

    for b in bullets:
        st.markdown(f"- {b}")

    st.markdown("</div>", unsafe_allow_html=True)

def pill(items):
    html = ""
    for i in items:
        html += f"<span class='tag'>{i}</span>"
    st.markdown(html, unsafe_allow_html=True)
