import streamlit as st

def section_title(title, icon=""):
    st.markdown(f"""
    <h2 style='margin-top:40px;'>{icon} {title}</h2>
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
        <h3>{title}</h3>
        <p style="color:#9CA3AF;">{subtitle}</p>
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


CLOUD_AI = {
    "name": "Ruchi Manjalkar",
    "title": "AI Engineer • Generative AI • Data Product Owner",
    "location": "Mannheim, Germany",
    "email": "ruchimanjalkar23@gmail.com",
    "linkedin": "https://linkedin.com/in/ruchi-manjalkar-360a97191",
    "github": "https://github.com/ruchimanjalkar",

    "summary": (
        "AI Engineer with 2+ years of experience building ML pipelines, data platforms, "
        "and generative AI systems using LangChain, RAG, and cloud technologies."
    ),

    "skills": {
        "Programming": "Python, SQL, SAS",
        "AI/GenAI": "LangChain, LangGraph, RAG, OpenAI API",
        "Machine Learning": "Scikit-learn, TensorFlow, XGBoost",
        "Data Engineering": "ETL Pipelines, FastAPI, Airflow, dbt",
        "Cloud": "AWS, GCP, Azure",
        "Visualization": "Power BI, Tableau, Streamlit",
    },

    "experience": [
        {
            "company": "e.Ray Europa GmbH",
            "role": "AI Engineer / Data Product Owner",
            "period": "Oct 2025 – Present",
            "bullets": [
                "Designed analytics-ready datasets supporting ML workflows.",
                "Built ETL pipelines reducing manual effort by 35%.",
                "Improved reporting efficiency by 20%.",
                "Implemented data quality monitoring reducing incidents by 40%.",
                "Defined KPIs and built scalable data products."
            ],
        },
        {
            "company": "Omnisent Sports",
            "role": "Data Science Intern",
            "period": "Jun 2025 – Sep 2025",
            "bullets": [
                "Built real-time sentiment pipelines using Twitter/X and Reddit.",
                "Developed data ingestion using Celery, Redis, PostgreSQL.",
                "Applied NLP models for sentiment and topic analysis.",
                "Created dashboards in Streamlit and Power BI."
            ],
        },
        {
            "company": "HDFC Bank",
            "role": "Deputy Manager — Data Analytics",
            "period": "Jul 2022 – Oct 2023",
            "bullets": [
                "Processed 1M+ daily transactions using SQL pipelines.",
                "Automated reconciliation reducing effort by 30%.",
                "Built anomaly detection dashboards."
            ],
        },
    ],

    "projects": [
        {
            "name": "Agentic AI Pipeline for Harmful Algal Bloom Detection",
            "bullets": [
                "Designed multi-agent system using LangGraph + LangChain.",
                "Built RAG pipelines with evaluation (RAGAS).",
                "Integrated satellite and climate datasets.",
                "Implemented LLM reasoning workflows."
            ],
            "tags": ["LangGraph", "RAG", "GCP"],
        },
        {
            "name": "Industrial Anomaly Detection (RENOLIT)",
            "bullets": [
                "Built VAE model for anomaly detection in production lines.",
                "Detected deviations in sensor data improving quality.",
                "Reduced production losses via early detection.",
                "Developed real-time Streamlit dashboard."
            ],
            "tags": ["VAE", "Deep Learning"],
        },
        {
            "name": "ML Pipeline Development & Predictive Analytics",
            "bullets": [
                "Built modular ML pipelines for classification and regression.",
                "Automated preprocessing and feature engineering.",
                "Improved model performance using structured workflows."
            ],
            "tags": ["ML Pipelines", "Scikit-learn"],
        },
    ],

    "education": [
        {
            "school": "SRH Hochschule Heidelberg",
            "degree": "M.Sc. Applied Data Science & Analytics",
            "period": "2023 – 2025",
        },
        {
            "school": "K.J. Somaiya College of Engineering",
            "degree": "B.Tech Electronics Engineering",
            "period": "2018 – 2022",
        },
    ],
}
