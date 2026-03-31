import streamlit as st

def card(title, subtitle, meta, bullets):
    st.markdown(f"""
    <div class="card">
        <h3>{title}</h3>
        <p style="color:#94a3b8;">{subtitle}</p>
        <p style="color:#64748b; font-size:13px;">{meta}</p>
    """, unsafe_allow_html=True)

    for b in bullets:
        st.markdown(f"- {b}")

    st.markdown("</div>", unsafe_allow_html=True)


def pill(items):
    html = ""
    for i in items:
        html += f"<span class='tag'>{i}</span>"
    st.markdown(html, unsafe_allow_html=True)
