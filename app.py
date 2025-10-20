# app.py
import os
import streamlit as st
from components import section_title, card, pill
from utils import load_lottie_url
from streamlit_lottie import st_lottie

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Ruchi Manjalkar — Data Portfolio",
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
st.sidebar.markdown("📧 [ruchi.manjalkar@gmail.com](mailto:ruchi.manjalkar@gmail.com)")
st.sidebar.markdown("🔗 [LinkedIn](https://linkedin.com/in/ruchi-manjalkar)")
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
st.subheader("Data Engineer • Data Scientist • AI Researcher")
st.markdown("""
> “Where data meets intelligence — building systems that not only analyze, but think.”  

I design intelligent data systems that combine analytics, automation, and agentic AI for real-world impact.  
My expertise spans **data pipelines**, **ML modeling**, and **LLM-based agent systems** that make data adaptive, explainable, and scalable.
""")

st.markdown("---")

# -------------------- TABS --------------------
tabs = st.tabs([
    "👩‍💻 About",
    "💼 Experience",
    "🚀 Projects",
    "🧠 Skills",
    "🎓 Education",
    "🏅 Certifications",
    "📬 Contact"
])

# -------------------- ABOUT --------------------
with tabs[0]:
    section_title("About Me", "👩‍💻")
    st.markdown("""
    I'm a **Data Engineer and AI Researcher** passionate about transforming raw data into intelligent decisions.  
    My background bridges **data engineering, machine learning, and generative AI**, with a focus on creating **Agentic AI frameworks** 
    that orchestrate data, models, and reasoning agents autonomously.

    - ⚙️ Experienced in **ETL pipelines**, **data orchestration**, and **cloud architecture (GCP/Azure)**.  
    - 🤖 Researching **multi-agent orchestration using LangChain and event-driven systems**.  
    - 🧩 Skilled in **Python, SQL, Airflow, Kafka**, and **containerized deployment with Docker**.  
    - 📊 Passionate about **data visualization** (Power BI, Streamlit, Tableau).  
    - 💬 Advocate for **Explainable & Responsible AI**.
    """)

# -------------------- EXPERIENCE --------------------
with tabs[1]:
    section_title("Professional Experience", "💼")

    card("Omnisent AI", "AI Engineer Intern", "June 2025 – Sep 2025 | Remote", [
        "🧩 Built **real-time ML pipelines** integrating Twitter & Reddit APIs using Kafka + Celery + PostgreSQL.",
        "☁️ Automated ingestion using **GCP Pub/Sub + Cloud Functions** for sentiment analytics.",
        "📈 Developed **Streamlit dashboards** for sports trend prediction (NBA, NFL).",
        "🧠 Integrated **LangChain LLMs** for data summarization and sentiment anomaly detection."
    ])

    card("HDFC Bank", "Deputy Manager — Data Analytics & Reporting", "Jul 2022 – Oct 2023 | Mumbai, India", [
        "📊 Automated financial reporting pipelines using **SQL, Power BI, and Python**.",
        "🔍 Analyzed 10M+ digital transactions for performance and compliance KPIs.",
        "🤝 Collaborated across business units to streamline analytics and report automation."
    ])

    card("Reliance Jio Infocomm", "Data Intern — Data Automation & Visualization", "Feb 2021 – Jun 2021 | Mumbai, India", [
        "⚙️ Automated operational KPI reports using **Python + Excel VBA scripts**.",
        "📉 Created **Tableau dashboards** improving executive decision visibility."
    ])

# -------------------- PROJECTS --------------------
with tabs[2]:
    section_title("Projects & Research", "🚀")

    # 1️⃣ AI-AGENTIC FRAMEWORK
    card("🌊 AI-Agentic Framework for Harmful Algal Bloom Prediction", "Master’s Thesis — SRH Hochschule Heidelberg", "Jan 2025 – Sep 2025", [
        "Developed a **multi-agent orchestration framework** integrating climate (ERA5), satellite (Sentinel-2), and in-situ (UBA) data.",
        "Built **event-bus communication** between agents (Collect → Process → Predict → Visualize).",
        "Used **LangChain** for inter-agent reasoning, enabling explainable coordination and decision flow.",
        "Deployed predictive models (**XGBoost, SARIMA, LSTM**) with SHAP-based feature interpretability.",
        "Hosted workflows on **GCP (BigQuery, Pub/Sub, Cloud Functions)** for scalable execution.",
        "Created dynamic **Power BI dashboards** for temporal-spatial bloom predictions."
    ])
    pill(["Python", "LangChain", "Event Bus", "GCP", "Airflow", "Power BI", "XGBoost", "LSTM", "SHAP"])

    # 2️⃣ OMNISENT SPORTS SENTIMENT PIPELINE
    card("🏀 Omnisent Sports Sentiment Analytics", "Enterprise AI Pipeline", "Jan 2025 – Apr 2025", [
        "Developed **real-time sentiment ingestion pipeline** for NBA & NFL events using Twitter + Reddit APIs.",
        "Used **Kafka, Celery, and PostgreSQL** to manage streaming data workloads.",
        "Implemented **LLM-based context summarization (LangChain)** for event-driven news classification.",
        "Built **Streamlit dashboards** to visualize Pulse scores and sentiment anomalies."
    ])
    pill(["Kafka", "Celery", "Streamlit", "PostgreSQL", "LangChain", "Docker", "GCP"])

    # 3️⃣ SPEECH AI PROJECTS
    card("🎙️ Speech Enhancement & Noise Reduction", "Deep Learning for Audio Clarity", "Jan 2024 – Mar 2024", [
        "Trained a **CRNN model** to remove background noise from speech recordings using TensorFlow + Librosa.",
        "Performed **spectrogram and MFCC-based feature extraction** for robust model performance.",
        "Improved signal-to-noise ratio by 20%, validated on noisy datasets."
    ])
    pill(["TensorFlow", "CRNN", "Librosa", "MFCC", "Audio DSP"])

    card("🗣️ Speech-to-Text Model Optimization", "Transformer Fine-tuning", "Nov 2024 – Jan 2025", [
        "Fine-tuned **Wav2Vec2 & DeepSpeech** models to enhance transcription accuracy.",
        "Applied **data augmentation** (pitch shift, time-stretch, speed variation) for generalization.",
        "Achieved ~10% WER improvement on custom German-English dataset."
    ])
    pill(["PyTorch", "SpeechBrain", "Transformers", "Hugging Face", "Audio Augmentation"])

    # 4️⃣ NLP / DATA AUTOMATION
    card("🤖 Hush Hush Recruiter", "AI-Powered Recruitment Assistant", "Nov 2023 – Feb 2024", [
        "Developed a **Flask-based web app** for GitHub candidate screening using clustering & NLP.",
        "Reduced manual screening by 40%, improved talent-matching accuracy by 85%.",
        "Used **Scikit-learn, BeautifulSoup, and Flask** for full pipeline automation."
    ])
    pill(["Flask", "Scikit-learn", "BeautifulSoup", "NLP", "Docker"])

    # 5️⃣ VISUALIZATION & BI
    card("📊 US FBI Crime Data Dashboard", "Data Visualization Project", "Oct 2024 – Nov 2024", [
        "Designed Tableau dashboards to visualize **12% rise in hate crimes (2009–2019)** across states.",
        "Mapped top categories by Race/Ethnicity and Location using LOD expressions.",
        "Enabled interactive KPI filters for trend comparison and time analysis."
    ])
    pill(["Tableau", "SQL", "Python", "Data Visualization"])

    # 6️⃣ ML & HEALTHCARE
    card("🫁 LungDetect — Pneumonia Detection", "Deep Learning for Healthcare", "May 2023 – Dec 2023", [
        "Developed **DenseNet121 CNN model** achieving 95% accuracy on chest X-ray dataset.",
        "Integrated **Grad-CAM** explainability for clinical validation and model transparency.",
        "Collaborated with healthcare mentors for model evaluation and interpretability."
    ])
    pill(["TensorFlow", "DenseNet121", "Grad-CAM", "Keras", "OpenCV"])

# -------------------- SKILLS --------------------
# -------------------- SKILLS --------------------
with tabs[3]:
    section_title("Technical Skills", "🧠")

    col1, col2, col3 = st.columns(3)

    # ------------------ COLUMN 1 ------------------
    with col1:
        st.markdown("#### 💻 Programming & Scripting")
        pill(["Python", "SQL", "R", "Bash", "JavaScript (basic)"])

        st.markdown("#### ⚙️ Data Engineering & Pipelines")
        pill([
            "Apache Airflow", "Kafka", "dbt", "ETL Pipelines",
            "Apache Spark", "Dataflow", "Terraform", "Event-Driven Design"
        ])

        st.markdown("#### 🤖 Agentic & Generative AI")
        pill([
            "LangChain", "OpenAI API", "LlamaIndex", "CrewAI",
            "Multi-Agent Orchestration", "Event Bus Architecture",
            "Retrieval-Augmented Generation (RAG)", "Vector Databases (FAISS / Chroma)",
            "Prompt Engineering", "Tool Integration & Memory Chains"
        ])

    # ------------------ COLUMN 2 ------------------
    with col2:
        st.markdown("#### ☁️ Cloud & DevOps")
        pill([
            "Google Cloud Platform (GCP)", "Azure", "AWS (S3, EC2)",
            "BigQuery", "Pub/Sub", "Docker", "Kubernetes",
            "GitHub Actions", "CI/CD", "Linux Server Management"
        ])

        st.markdown("#### 📊 Visualization & BI")
        pill([
            "Power BI", "Tableau", "Streamlit", "Looker Studio",
            "Matplotlib", "Seaborn", "Plotly", "Altair"
        ])

        st.markdown("#### 🧩 Databases & Storage")
        pill([
            "PostgreSQL", "MySQL", "MongoDB", "BigQuery",
            "SQLite", "ElasticSearch", "Snowflake", "Cloud Storage Buckets"
        ])

    # ------------------ COLUMN 3 ------------------
    with col3:
        st.markdown("#### 🤖 Machine & Deep Learning")
        pill([
            "Scikit-learn", "TensorFlow", "PyTorch",
            "XGBoost", "LightGBM", "LSTM / RNNs",
            "Transformers (Hugging Face)", "Computer Vision (CNN, Grad-CAM)",
            "Model Explainability (SHAP, LIME)"
        ])

        st.markdown("#### 🧠 NLP & LLM Ecosystem")
        pill([
            "Hugging Face Transformers", "Tokenization / Embeddings",
            "Sentence-Transformers", "Text Summarization / QnA Pipelines",
            "LLM Fine-Tuning", "LangSmith Tracing", "Prompt Templates"
        ])

        st.markdown("#### 🧰 Tools, Collaboration & Analytics")
        pill([
            "Excel VBA", "Git / GitHub", "Jira", "Confluence",
            "Notion", "Miro", "Slack Automation", "API Testing (Postman)"
        ])


# -------------------- EDUCATION --------------------
with tabs[4]:
    section_title("Education", "🎓")

    card("🎓 SRH Hochschule Heidelberg", "M.Sc. in Applied Data Science & Analytics", "Oct 2023 – Nov 2025 | Germany", [
        "Specialization: Cloud Engineering, Machine Learning, and Agentic AI Systems.",
        "Thesis: AI-Agentic Framework integrating Event Bus, LangChain, and GCP microservices."
    ])

    card("🏫 K.J. Somaiya College of Engineering", "B.E. in Electronics Engineering", "Aug 2018 – May 2022 | India", [
        "Capstone Project: Pneumonia Detection using DenseNet121 CNN with Grad-CAM.",
        "Focused coursework in DSP, Machine Learning, and Embedded Systems."
    ])

# -------------------- CERTIFICATIONS --------------------
with tabs[5]:
    section_title("Professional Certifications", "🏅")
    st.markdown("""
    - 🎓 **IBM Data Science Professional Certificate** — Coursera (2023)  
      *Python for Data Science, SQL, Visualization, and Applied Capstone.*  

    - 🤖 **Machine Learning A–Z: Hands-On Python & R** — Udemy (2023)  
      *Practical ML workflows using scikit-learn and R-based analytics.*  

    - 📊 **Microsoft Power BI Desktop for Business Intelligence** — Udemy (2024)  
      *Data modeling, DAX, and performance-tuned dashboards.*  

    - 🧠 **Fundamentals of Deep Learning** — NVIDIA (2024)  
      *CNNs, RNNs, and GPU-accelerated DL optimization.*  

    - 🧩 **LangChain for LLM Applications** — LangChain Academy (2024)  
      *Building modular AI agents, prompt orchestration, and reasoning pipelines.*  

    - ☁️ **Google Cloud Data Engineer Associate** — Google Cloud (2024)  
      *Designed & deployed pipelines with Pub/Sub, BigQuery, and Dataflow.*  

    - 🐳 **Docker Masterclass for Data Science** — Udemy (2024)  
      *Containerized ML environments for reproducible pipelines.*  

    - 💬 **Generative AI Masterclass** — Udemy (2024)  
      *Built LLM-based apps using OpenAI APIs & LangChain integrations.*  

    - 🪄 **Advanced Prompt Engineering & RAG Systems** — Deeplearning.ai (2025)  
      *Designed retrieval-augmented generation pipelines with FAISS and OpenAI APIs.*  

    - 📈 **Exploring SAP Analytics Cloud** — SAP Learning Hub (2024)  
      *Created predictive data stories, dashboards, and business KPIs in SAC.*  
    """)

# -------------------- CONTACT --------------------
with tabs[6]:
    section_title("Get in Touch", "📬")
    st.markdown("""
    I’d love to connect!  
    Whether you’re interested in AI agent frameworks, data engineering solutions, or ML visualization — drop me a message below.
    """)

    st.markdown("""
    <form id="contactForm" action="https://formsubmit.co/ruchi.manjalkar@gmail.com" method="POST" onsubmit="showMessage()">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message" required></textarea>
        <button type="submit">Send Message</button>
    </form>

    <script>
        function showMessage() {alert('✅ Your message has been sent successfully!');}
    </script>

    <style>
        form {display:flex;flex-direction:column;gap:10px;width:100%;max-width:500px;}
        input, textarea {
            padding:10px;border-radius:8px;border:none;
            background:#171A21;color:#F1F5F9;font-size:15px;
        }
        textarea {height:120px;resize:none;}
        button {
            background:#0078D7;color:white;border:none;padding:10px;
            border-radius:8px;font-size:16px;font-weight:bold;
            transition:0.3s;
        }
        button:hover {background:#005fa3;cursor:pointer;}
    </style>
    """, unsafe_allow_html=True)
