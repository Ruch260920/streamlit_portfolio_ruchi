# app.py
import streamlit as st
from data_ruchi import CLOUD_AI
import pandas as pd
import numpy as np

data = CLOUD_AI

st.set_page_config(layout="wide")

st.title(data["name"])
st.subheader(data["title"])
st.write(data["summary"])

# ---------------- EXPERIENCE ----------------
st.header("💼 Experience")

for exp in data["experience"]:
    st.subheader(f"{exp['company']} — {exp['role']}")
    st.caption(exp["period"])
    for b in exp["bullets"]:
        st.write(f"- {b}")

# ---------------- PROJECTS ----------------
st.header("🚀 Projects")

for proj in data["projects"]:
    st.subheader(proj["name"])
    for b in proj["bullets"]:
        st.write(f"- {b}")
    st.write("Tags:", ", ".join(proj["tags"]))

# ---------------- DEMO TAB ----------------
st.header("🧪 AI Demo Lab")

st.subheader("🤖 AI Assistant")
q = st.text_input("Ask about AI")

if q:
    st.success("Demo AI response — connect OpenAI API for real answers")

st.subheader("📊 ML Prediction")

temp = st.slider("Temp", 0, 40, 25)
humidity = st.slider("Humidity", 0, 100, 60)

score = temp * 0.4 + humidity * 0.6
st.metric("Risk Score", round(score, 2))

st.subheader("📈 Analytics")

df = pd.DataFrame({
    "x": range(50),
    "y": np.random.randn(50).cumsum()
})

st.line_chart(df)
