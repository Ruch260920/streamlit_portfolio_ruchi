import sys
import os
sys.path.append(os.path.dirname(__file__))

import streamlit as st
import components
from data_ruchi import CLOUD_AI

# Assign components
section_title = components.section_title
card = components.card
pill = components.pill

st.set_page_config(page_title="Ruchi Portfolio", layout="wide")

data = CLOUD_AI

# ---------- CSS ----------
st.markdown("""
<style>

/* Background */
body {
    background: linear-gradient(135deg, #020617, #020617, #0f172a);
}

/* Hero */
.hero-title {
    font-size: 50px;
    font-weight: 800;
    background: linear-gradient(90deg, #38bdf8, #6366f1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-sub {
    color: #94a3b8;
    font-size: 20px;
    margin-top: 5px;
}

/* Section Titles */
.section {
    font-size: 30px;
    font-weight: 700;
    margin-top: 50px;
    margin-bottom: 20px;
    color: #e2e8f0;
}

/* Cards */
.card {
    background: rgba(15, 23, 42, 0.7);
    backdrop-filter: blur(12px);
    padding: 25px;
    border-radius: 14px;
    margin-bottom: 20px;
    border: 1px solid rgba(148, 163, 184, 0.1);
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-6px);
    border: 1px solid #38bdf8;
    box-shadow: 0px 12px 35px rgba(56, 189, 248, 0.2);
}

/* Tags */
.tag {
    background: linear-gradient(90deg, #38bdf8, #6366f1);
    padding: 6px 14px;
    margin: 4px;
    border-radius: 20px;
    font-size: 12px;
    color: white;
    display: inline-block;
}

/* Divider */
hr {
    border: none;
    height: 1px;
    background: linear-gradient(to right, transparent, #334155, transparent);
    margin: 40px 0;
}

/* Fade animation */
.fade-in {
    animation: fadeIn 0.8s ease-in;
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown(f"""
<div class="fade-in">
    <div class="hero-title">{data['name']}</div>
    <div class="hero-sub">{data['title']}</div>
    <p style="max-width:750px; color:#cbd5f5; margin-top:10px;">
        {data['summary']}
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ---------- EXPERIENCE ----------
st.markdown('<div class="section">💼 Experience</div>', unsafe_allow_html=True)

for exp in data.get("experience", []):
    card(exp["company"], exp["role"], exp["period"], exp["bullets"])

# ---------- PROJECTS ----------
st.markdown('<div class="section">🚀 Projects</div>', unsafe_allow_html=True)

for proj in data.get("projects", []):
    card(proj["name"], "Project", "", proj["bullets"])
    pill(proj["tags"])

# ---------- SKILLS ----------
st.markdown('<div class="section">🧠 Skills</div>', unsafe_allow_html=True)

for k, v in data.get("skills", {}).items():
    st.markdown(f"<b>{k}</b>", unsafe_allow_html=True)
    pill(v.split(", "))

# ---------- EDUCATION ----------
st.markdown('<div class="section">🎓 Education</div>', unsafe_allow_html=True)

for edu in data.get("education", []):
    st.markdown(f"""
    <div class="card">
        <b>{edu['school']}</b><br>
        {edu['degree']} ({edu['period']})
    </div>
    """, unsafe_allow_html=True)

# ---------- CERTIFICATIONS ----------
st.markdown('<div class="section">🏅 Certifications</div>', unsafe_allow_html=True)

for cert in data.get("certifications", []):
    st.markdown(f"""
    <div class="card">✅ {cert}</div>
    """, unsafe_allow_html=True)

# ---------- CONTACT ----------
st.markdown('<div class="section">📬 Contact</div>', unsafe_allow_html=True)

st.markdown(f"""
📧 {data.get('email', '')}  
🔗 {data.get('linkedin', '')}  
💻 {data.get('github', '')}  
""")
