# app.py
import os
import streamlit as st
from components import section_title, card, pill
from utils import load_lottie_url
from streamlit_lottie import st_lottie

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Ruchi Manjalkar — AI Portfolio",
    page_icon="💫",
    layout="wide"
)

# -------------------- CUSTOM CSS --------------------
st.markdown("""
<style>
.main .block-container {max-width: 1150px;}
h1, h2, h3, h4, h5, h6 {color: #E4E6EB !important;}
p, li, span, div {color: #E4E6EB;}
footer, header {visibility: hidden;}
.tag {
    display:inline-block;
    padding:5px 12px;
    margin:5px 5px 0 0;
    border-radius:20px;
    background-color:#0078D7;
    color:white;
    font-size:13px;
    font-weight:500;
}
</style>
""", unsafe_allow_html=True)

# -------------------- SIDEBAR --------------------
if os.path.exists("assets/ruchi.jpg"):
    st.sidebar.image("assets/ruchi.jpg", use_column_width=True)

st.sidebar.markdown("### 👩‍💻 Ruchi Manjalkar")
st.sidebar.markdown("📍 Mannheim, Germany")
st.sidebar.markdown("📧 ruchimanjalkar23@gmail.com")
st.sidebar.markdown("🔗 [LinkedIn](https://linkedin.com/in/ruchi-manjalkar-360a97191)")
st.sidebar.markdown("💻 [GitHub](https://github.com/ruchimanjalkar)")

resume_path = "assets/resume.pdf"
if os.path.exists(resume_path):
    with open(resume_path, "rb") as f:
        st.sidebar.download_button(
            "⬇️ Download Resume",
            f,
            file_name="Ruchi_Manjalkar_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )

# -------------------- HEADER --------------------
lottie_data = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_jcikwtux.json")
st_lottie(lottie_data, height=220, key="header_anim")

st.title("💫 Ruchi Manjalkar")
st.subheader("AI Engineer • Generative AI • Data Product Owner")

st.markdown("""
> “Building intelligent systems where data, models, and reasoning agents work together.”

I am an **AI Engineer with 3+ years of experience** designing scalable data systems, machine learning pipelines, and generative AI applications.  

- 🧠 LLM orchestration (**LangChain, LangGraph, RAG**)  
- ⚙️ Production data systems (**ETL, SQL, APIs**)  
- 📊 KPI-driven **data products & analytics**  
- ☁️ Cloud ML systems (**GCP, AWS, Azure**)  

I focus on building **end-to-end intelligent systems** that are scalable, explainable, and impactful.
""")

st.info("💡 Currently building production-ready AI systems combining data pipelines, LLM reasoning, and scalable cloud architecture.")

st.markdown("---")

# -------------------- TABS --------------------
tabs = st.tabs([
    "👩‍💻 About",
    "💼 Experience",
    "🚀 Projects",
    "🧪 Demo Lab",   # ✅ NEW TAB
    "🧠 Skills",
    "🎓 Education",
    "🏅 Certifications",
    "📬 Contact"
])

# -------------------- ABOUT --------------------
with tabs[0]:
    section_title("About Me", "👩‍💻")
    st.markdown("""
    I specialize in building **AI-driven data systems** that combine:
    
    - Data Engineering ⚙️  
    - Machine Learning 📊  
    - Generative AI 🤖  

    My work focuses on **agentic AI systems**, where multiple intelligent components collaborate
    to automate decisions, insights, and workflows.
    """)

# -------------------- EXPERIENCE --------------------
with tabs[1]:
    section_title("Professional Experience", "💼")

    card("e.Ray Europa GmbH", "AI Engineer / Data Product Owner", "Oct 2025 – Present | Heidelberg, Germany", [
        "🚀 Designed analytics-ready datasets and semantic metric layers enabling ML workflows.",
        "⚙️ Built Python + SQL ETL pipelines reducing manual effort by 35%.",
        "📊 Improved reporting efficiency by 20%.",
        "🛡️ Implemented data quality monitoring reducing incidents by 40%.",
        "🤝 Defined KPIs and built scalable data products.",
        "☁️ Worked on cloud-based architectures integrating analytics pipelines."
    ])

    card("Omnisent AI", "Product & Analytics Intern", "Jun 2025 – Sep 2025 | Remote", [
        "📊 Analyzed 500K+ event records for insights.",
        "📈 Designed KPI frameworks for experimentation.",
        "⚙️ Built ML pipelines integrating social APIs.",
        "☁️ Used GCP Pub/Sub + Cloud Functions.",
        "🧠 Applied LLM-based sentiment analytics."
    ])

# -------------------- PROJECTS --------------------
with tabs[2]:
    section_title("Projects & Research", "🚀")

    card("🌊 Agentic AI Pipeline", "Master’s Thesis", "2025", [
        "Multi-agent system using LangGraph + LangChain.",
        "RAG pipelines with evaluation (RAGAS).",
        "LLM reasoning workflows using OpenAI APIs."
    ])
    pill(["LangGraph", "LangChain", "RAG"])

# -------------------- 🧪 DEMO LAB --------------------
with tabs[3]:
    section_title("AI Demo Lab", "🧪")

    # ---------- AI CHAT ----------
    st.markdown("### 🤖 AI Assistant")
    user_input = st.text_input("Ask about AI, ML, or pipelines:")

    if user_input:
        if "pipeline" in user_input.lower():
            st.success("AI Response: Data pipelines automate ingestion → transformation → storage → analytics.")
        elif "llm" in user_input.lower():
            st.success("AI Response: LLMs use transformer architectures for contextual understanding.")
        else:
            st.success("AI Response: Demo assistant — connect OpenAI API for real responses.")

    st.markdown("---")

    # ---------- ML SIMULATOR ----------
    st.markdown("### 📊 ML Prediction Simulator")

    col1, col2 = st.columns(2)

    with col1:
        temp = st.slider("Temperature (°C)", 0, 40, 25)
        humidity = st.slider("Humidity (%)", 0, 100, 60)

    with col2:
        wind = st.slider("Wind Speed", 0, 50, 10)
        pollution = st.slider("Pollution Index", 0, 300, 120)

    score = (temp*0.3 + humidity*0.2 + wind*0.1 + pollution*0.4)

    st.metric("Bloom Risk Score", round(score, 2))

    if score > 150:
        st.error("High Risk")
    elif score > 80:
        st.warning("Moderate Risk")
    else:
        st.success("Low Risk")

    st.markdown("---")

    # ---------- ANALYTICS ----------
    st.markdown("### 📈 Real-Time Analytics")

    import pandas as pd
    import numpy as np

    data = pd.DataFrame({
        "Time": range(50),
        "Sentiment": np.random.randn(50).cumsum(),
        "Engagement": np.random.randint(50, 200, 50)
    })

    st.line_chart(data.set_index("Time"))
    st.bar_chart(data["Engagement"])

    st.info("Simulated real-time streaming analytics")

# -------------------- SKILLS --------------------
with tabs[4]:
    section_title("Skills", "🧠")
    pill(["Python", "SQL", "LangChain", "GCP", "AWS", "Docker"])

# -------------------- EDUCATION --------------------
with tabs[5]:
    section_title("Education", "🎓")
    st.write("SRH Hochschule Heidelberg — M.Sc.")

# -------------------- CERTIFICATIONS --------------------
with tabs[6]:
    section_title("Certifications", "🏅")
    st.write("Refer LinkedIn")

# -------------------- CONTACT --------------------
with tabs[7]:
    section_title("Contact", "📬")
    st.write("Email / LinkedIn / GitHub")
