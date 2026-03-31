import streamlit as st

def section_title(title, icon=""):
    st.markdown(f"""
    <h2 style='margin-top:40px; font-weight:600;'>{icon} {title}</h2>
    """, unsafe_allow_html=True)

def card(title, subtitle, meta, bullets):
    st.markdown(f"""
    <div style="
        background-color:#0f172a;
        padding:20px;
        border-radius:12px;
        margin-bottom:20px;
        border:1px solid #1e293b;
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
        html += f"<span style='background:#2563EB;padding:6px 12px;margin:4px;border-radius:20px;font-size:12px'>{i}</span>"
    st.markdown(html, unsafe_allow_html=True)
