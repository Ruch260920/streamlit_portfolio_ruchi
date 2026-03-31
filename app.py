import sys
import os
sys.path.append(os.path.dirname(__file__))

import streamlit as st
from data_ruchi import CLOUD_AI
import components

section_title = components.section_title
card = components.card
pill = components.pill

st.set_page_config(layout="wide")

data = CLOUD_AI

# ---------- CSS (SAFE ANIMATIONS) ----------
st.markdown("""
<style>

body {
    background-color:#020617;
}

/* Fade-in animation */
.fade-in {
    animation: fadeIn 0.8s ease-in;
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(15px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Card styling */
.card {
    background-color:#0f172a;
    padding:20px;
    border-radius:12px;
    margin-bottom:20px;
    border:1px solid #1e293b;
    transition: all 0.3s ease;
}

/* Hover effect */
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 10px 25px rgba(0,0,0,0.4);
}

/* Tag styling */
.tag {
    background:#2563EB;
    padding:6px 12px;
    margin:4px;
    border-radius:20px;
    font-size:12px;
    display:inline-block;
}

</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown(f"""
<div class="fade-in">
<h1>{data['name']}</h1>
<h3 style='color:#9CA3AF'>{data['title']}</h3>
<p style='max-width:700px'>{data['summary']}</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------- EXPERIENCE ----------
section_title("Experience", "💼")

for exp in data["experience"]:
    st.markdown('<div class="fade-in card">', unsafe_allow_html=True)
    card(exp["company"], exp["role"], exp["period"], exp["bullets"])
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- PROJECTS ----------
section_title("Projects", "🚀")

for proj in data["projects"]:
    st.markdown('<div class="fade-in card">', unsafe_allow_html=True)
    card(proj["name"], "Project", "", proj["bullets"])
    pill(proj["tags"])
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- SKILLS ----------
section_title("Skills", "🧠")

for k, v in data["skills"].items():
    st.markdown(f"<div class='fade-in'><b>{k}</b></div>", unsafe_allow_html=True)
    pill(v.split(", "))

# ---------- EDUCATION ----------
section_title("Education", "🎓")

for edu in data["education"]:
    st.markdown(f"""
    <div class="fade-in card">
        <b>{edu['school']}</b><br>
        {edu['degree']} ({edu['period']})
    </div>
    """, unsafe_allow_html=True)

# ---------- CONTACT ----------
section_title("Contact", "📬")

st.markdown(f"""
<div class="fade-in">
📧 {data['email']}  
🔗 {data['linkedin']}  
💻 {data['github']}
</div>
""", unsafe_allow_html=True)
