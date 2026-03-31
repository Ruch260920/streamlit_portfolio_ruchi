import sys
import os
sys.path.append(os.path.dirname(__file__))

import streamlit as st
import components
from data_ruchi import CLOUD_AI

card = components.card
pill = components.pill

st.set_page_config(page_title="Ruchi Portfolio", layout="wide")

data = CLOUD_AI

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown("## 👩‍💻 Ruchi Manjalkar")
    st.markdown("AI Engineer | GenAI | Data")
    st.markdown("---")

    st.markdown("📍 Mannheim, Germany")
    st.markdown("📧 " + data["email"])
    st.markdown("🔗 [LinkedIn](" + data["linkedin"] + ")")
    st.markdown("💻 [GitHub](" + data["github"] + ")")

    st.markdown("---")
    st.markdown("### 🚀 Quick Skills")
    for k in list(data["skills"].keys())[:3]:
        st.write(f"• {k}")

# ---------- CSS ----------
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #020617, #0f172a);
}

/* HERO */
.hero {
    padding: 20px 0;
}

.hero-title {
    font-size: 52px;
    font-weight: 800;
    background: linear-gradient(90deg, #38bdf8, #6366f1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-sub {
    font-size: 20px;
    color: #94a3b8;
}

/* SECTION */
.section {
    font-size: 28px;
    font-weight: 700;
    margin-top: 50px;
    color: #e2e8f0;
}

/* GLASS CARD */
.card {
    background: rgba(15, 23, 42, 0.7);
    backdrop-filter: blur(12px);
    padding: 22px;
    border-radius: 14px;
    margin-bottom: 20px;
    border: 1px solid rgba(148, 163, 184, 0.1);
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-6px);
    border: 1px solid #38bdf8;
    box-shadow: 0px 12px 30px rgba(56, 189, 248, 0.2);
}

/* TAGS */
.tag {
    background: linear-gradient(90deg, #38bdf8, #6366f1);
    padding: 6px 14px;
    margin: 4px;
    border-radius: 20px;
    font-size: 12px;
    color: white;
}

/* METRIC BOX */
.metric {
    background: #0f172a;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
col1, col2 = st.columns([2,1])

with col1:
    st.markdown(f"""
    <div class="hero">
        <div class="hero-title">{data['name']}</div>
        <div class="hero-sub">{data['title']}</div>
        <p style="max-width:600px;">
            {data['summary']}
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric">
        <h3>3+ Years</h3>
        <p>Experience</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="metric">
        <h3>5+</h3>
        <p>Projects</p>
    </div>
    """, unsafe_allow_html=True)

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

cols = st.columns(2)

i = 0
for k, v in data.get("skills", {}).items():
    with cols[i % 2]:
        st.markdown(f"**{k}**")
        pill(v.split(", "))
    i += 1

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
    st.markdown(f"<div class='card'>✅ {cert}</div>", unsafe_allow_html=True)

# ---------- CONTACT ----------
st.markdown('<div class="section">📬 Contact</div>', unsafe_allow_html=True)

st.markdown(f"""
📧 {data['email']}  
🔗 {data['linkedin']}  
💻 {data['github']}
""")
