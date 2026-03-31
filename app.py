import sys
import os
sys.path.append(os.path.dirname(__file__))

import streamlit as st
import components
from data_ruchi import CLOUD_AI

card = components.card
pill = components.pill

st.set_page_config(layout="wide")

data = CLOUD_AI

# ---------- CSS ----------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #020617, #0f172a);
}

.hero-title {
    font-size: 50px;
    font-weight: 800;
    background: linear-gradient(90deg, #38bdf8, #6366f1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.section {
    font-size: 28px;
    font-weight: 700;
    margin-top: 40px;
    color: #e2e8f0;
}

.card {
    background: rgba(15, 23, 42, 0.7);
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
    border: 1px solid #1e293b;
}

.tag {
    background: linear-gradient(90deg, #38bdf8, #6366f1);
    padding: 6px 12px;
    margin: 4px;
    border-radius: 20px;
    font-size: 12px;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# HERO
st.markdown(f"""
<div class="hero-title">{data['name']}</div>
<h3>{data['title']}</h3>
<p>{data['summary']}</p>
""", unsafe_allow_html=True)

# EXPERIENCE
st.markdown('<div class="section">💼 Experience</div>', unsafe_allow_html=True)
for exp in data.get("experience", []):
    card(exp["company"], exp["role"], exp["period"], exp["bullets"])

# PROJECTS
st.markdown('<div class="section">🚀 Projects</div>', unsafe_allow_html=True)
for proj in data.get("projects", []):
    card(proj["name"], "Project", "", proj["bullets"])
    pill(proj["tags"])

# SKILLS
st.markdown('<div class="section">🧠 Skills</div>', unsafe_allow_html=True)
for k, v in data.get("skills", {}).items():
    st.markdown(f"**{k}**")
    pill(v.split(", "))

# EDUCATION
st.markdown('<div class="section">🎓 Education</div>', unsafe_allow_html=True)
for edu in data.get("education", []):
    st.markdown(f"**{edu['school']}** — {edu['degree']} ({edu['period']})")

# CERTIFICATIONS
st.markdown('<div class="section">🏅 Certifications</div>', unsafe_allow_html=True)
for cert in data.get("certifications", []):
    st.markdown(f"- {cert}")

# CONTACT
st.markdown('<div class="section">📬 Contact</div>', unsafe_allow_html=True)
st.markdown(f"{data['email']} | {data['linkedin']} | {data['github']}")
