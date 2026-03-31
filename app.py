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
    "🧠 Skills",
    "🎓 Education",
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

    I bring a strong mix of **engineering + product thinking**, enabling scalable and business-aligned AI systems.
    """)

# -------------------- EXPERIENCE --------------------
with tabs[1]:
    section_title("Professional Experience", "💼")

    card("e.Ray Europa GmbH", "AI Engineer / Data Product Owner", "Oct 2025 – Present | Heidelberg, Germany", [
        "🚀 Designed analytics-ready datasets and semantic metric layers.",
        "⚙️ Built Python + SQL ETL pipelines reducing manual work by 35%.",
        "📊 Improved reporting efficiency by 20%.",
        "🛡️ Implemented data quality monitoring reducing issues by 40%.",
        "🤝 Defined KPIs and built scalable data products."
    ])

    card("Omnisent AI", "Product & Analytics Intern", "Jun 2025 – Sep 2025 | Remote", [
        "📊 Analyzed 500K+ event records for behavioral insights.",
        "📈 Designed KPI frameworks for funnel analysis.",
        "📊 Built Tableau dashboards reducing reporting effort by 25%."
    ])

    card("HDFC Bank", "Deputy Manager — Data Analytics", "Jul 2022 – Oct 2023 | Mumbai", [
        "⚙️ Processed 1M+ daily transactions using SQL pipelines.",
        "🔄 Automated reconciliation reducing effort by 30%.",
        "📊 Built anomaly detection dashboards."
    ])

    card("Jio Platforms Ltd.", "Data Science Intern", "Jan 2022 – Jun 2022 | Mumbai", [
        "🤖 Built computer vision models (88% accuracy).",
        "📊 Analyzed telecom datasets for insights.",
        "⚙️ Reduced preprocessing time by 40%."
    ])

# -------------------- PROJECTS --------------------
with tabs[2]:
    section_title("Projects & Research", "🚀")

    card("🌊 Agentic AI Pipeline for Harmful Algal Bloom Detection", "Master’s Thesis", "2025", [
        "🤖 Multi-agent system using LangGraph + LangChain.",
        "🧠 RAG pipelines with evaluation (RAGAS).",
        "📡 Satellite + climate data integration.",
        "🔗 LLM reasoning workflows with OpenAI APIs.",
        "⚙️ Modular ML pipelines for prediction."
    ])
    pill(["LangGraph", "LangChain", "RAG", "RAGAS", "OpenAI"])

    card("⚙️ Modular ML Pipeline System", "Predictive Analytics", "2024", [
        "Built reusable ML pipelines for classification & regression.",
        "Automated preprocessing and feature engineering.",
        "Improved model performance via structured workflows."
    ])
    pill(["Scikit-learn", "Pandas", "ML Pipelines"])

# -------------------- SKILLS --------------------
with tabs[3]:
    section_title("Technical Skills", "🧠")

    st.markdown("### 🤖 AI & Generative AI")
    pill(["LangChain", "LangGraph", "RAG", "RAGAS", "OpenAI API", "NVIDIA NeMo", "MCP"])

    st.markdown("### 💻 Programming")
    pill(["Python", "SQL", "SAS", "TypeScript"])

    st.markdown("### ⚙️ Data Engineering")
    pill(["ETL Pipelines", "Airflow", "dbt", "FastAPI", "REST APIs", "GraphQL"])

    st.markdown("### ☁️ Cloud & MLOps")
    pill(["AWS", "GCP", "Azure", "Docker", "Kubernetes", "MLflow", "CI/CD"])

    st.markdown("### 📊 Visualization")
    pill(["Tableau", "Power BI", "Plotly", "Matplotlib", "D3.js"])

    st.markdown("### 🧰 Tools")
    pill(["Git", "Jira", "Confluence", "Terraform"])

# -------------------- EDUCATION --------------------
with tabs[4]:
    section_title("Education", "🎓")

    card("🎓 SRH Hochschule Heidelberg", "M.Sc. Applied Data Science", "2023 – 2025", [
        "Focus: ML, Data Engineering, Generative AI",
        "Thesis: Agentic AI Pipeline using LangGraph"
    ])

    card("🏫 K.J. Somaiya College", "B.Tech Engineering", "2018 – 2022", [])

# -------------------- CONTACT --------------------
with tabs[5]:
    section_title("Get in Touch", "📬")

    st.markdown("""
    📧 **ruchimanjalkar23@gmail.com**  
    🔗 **LinkedIn:** https://linkedin.com/in/ruchi-manjalkar-360a97191  
    💻 **GitHub:** https://github.com/ruchimanjalkar  
    """)
