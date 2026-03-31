import streamlit as st
from data_ruchi import CLOUD_AI
from components import section_title, card, pill

st.set_page_config(layout="wide")

data = CLOUD_AI

# ---------- HERO ----------
st.title(data["name"])
st.subheader(data["title"])
st.write(data["summary"])

st.markdown("---")

# ---------- EXPERIENCE ----------
section_title("Experience", "💼")

for exp in data["experience"]:
    card(exp["company"], exp["role"], exp["period"], exp["bullets"])

# ---------- PROJECTS ----------
section_title("Projects", "🚀")

for proj in data["projects"]:
    card(proj["name"], "Project", "", proj["bullets"])
    pill(proj["tags"])

# ---------- SKILLS ----------
section_title("Skills", "🧠")

for k, v in data["skills"].items():
    st.markdown(f"**{k}**")
    pill(v.split(", "))

# ---------- EDUCATION ----------
section_title("Education", "🎓")

for edu in data["education"]:
    st.markdown(f"**{edu['school']}**")
    st.write(f"{edu['degree']} ({edu['period']})")

# ---------- CONTACT ----------
section_title("Contact", "📬")

st.markdown(f"""
📧 {data['email']}  
🔗 {data['linkedin']}  
💻 {data['github']}
""")
