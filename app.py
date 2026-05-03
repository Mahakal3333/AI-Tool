import streamlit as st
import google.generativeai as genai
import os

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="GhostRoot AI | Cyber Mentor",
    page_icon="⚡",
    layout="centered"
)

# --- CUSTOM CSS FOR RICH UI ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #0E1117;
    }
    
    /* Elegant Cards for Content */
    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #00FF41;
        color: black;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    
    div.stButton > button:hover {
        background-color: #008F11;
        color: white;
        box-shadow: 0px 0px 15px #00FF41;
    }

    /* Input Box Styling */
    .stTextInput input {
        border-radius: 10px;
        border: 1px solid #30363d;
        background-color: #161b22;
        color: white;
    }

    /* Lesson Card Styling */
    .lesson-card {
        background-color: #1c2128;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #00FF41;
        margin-top: 20px;
    }
    
    /* Title Styling */
    .main-title {
        font-family: 'Inter', sans-serif;
        color: #00FF41;
        text-align: center;
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0px;
    }
    
    .sub-title {
        color: #8b949e;
        text-align: center;
        margin-bottom: 40px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- UI HEADER ---
st.markdown("<h1 class='main-title'>GHOSTROOT</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Master the shadows with daily-life analogies</p>", unsafe_allow_html=True)

# --- MAIN INTERFACE ---
with st.container():
    col1, col2 = st.columns([1, 1])
    
    with col1:
        level = st.selectbox(
            "Your Skill Level",
            ["Newbie (Basic)", "Scout (Intermediate)", "Vanguard (Advanced)", "Ghost (Expert)"]
        )
    
    with col2:
        topic = st.text_input("Security Topic", placeholder="e.g. Phishing, SQLi, VPN")

    generate_btn = st.button("INITIATE LEARNING")

# --- AI LOGIC ---
if generate_btn:
    if topic:
        with st.spinner("Decoding complex protocols..."):
            try:
                genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                prompt = f"""
                Act as GhostRoot, an elite but friendly cyber mentor. 
                Explain '{topic}' to a {level} learner.
                Structure:
                1. The 'Real Life' Scenario: Use a vivid everyday analogy.
                2. The 'Shadow' Reality: How this maps to cyber security.
                3. The 'Ghost Protocol': One expert safety tip.
                Keep it sleek, professional, and use markdown for bolding.
                """
                
                response = model.generate_content(prompt)
                
                # Displaying as a Rich Card
                st.markdown(f"""
                    <div class="lesson-card">
                        {response.text}
                    </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error("Connection to Neural Network failed. Check API Key.")
    else:
        st.warning("Please specify a target topic.")

# --- FOOTER ---
st.markdown("---")
st.caption("GhostRoot AI v1.0 | Built for the Open Web")
