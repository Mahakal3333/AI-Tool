import streamlit as st
import google.generativeai as genai
import os

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="GhostRoot AI | Cyber Mentor",
    page_icon="⚡",
    layout="centered"
)

# --- 2. CUSTOM CSS FOR RICH UI ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #0E1117;
    }
    
    /* Elegant Buttons */
    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 3.5em;
        background-color: #00FF41;
        color: black;
        font-weight: bold;
        border: none;
        transition: 0.3s;
        font-size: 1.1rem;
    }
    
    div.stButton > button:hover {
        background-color: #008F11;
        color: white;
        box-shadow: 0px 0px 20px #00FF41;
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
        padding: 30px;
        border-radius: 15px;
        border-left: 6px solid #00FF41;
        margin-top: 25px;
        line-height: 1.6;
        color: #e6edf3;
    }
    
    /* Title Styling */
    .main-title {
        font-family: 'Courier New', Courier, monospace;
        color: #00FF41;
        text-align: center;
        font-size: 3.5rem;
        font-weight: 900;
        letter-spacing: 2px;
        margin-bottom: 0px;
    }
    
    .sub-title {
        color: #8b949e;
        text-align: center;
        font-style: italic;
        margin-bottom: 50px;
    }

    /* Alert Styling */
    .stAlert {
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. UI HEADER ---
st.markdown("<h1 class='main-title'>GHOSTROOT</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Master the shadows with daily-life analogies</p>", unsafe_allow_html=True)

# --- 4. MAIN INTERFACE ---
with st.container():
    col1, col2 = st.columns([1, 1])
    
    with col1:
        level = st.selectbox(
            "Your Skill Level",
            ["Newbie (Basic)", "Scout (Intermediate)", "Vanguard (Advanced)", "Ghost (Expert)"]
        )
    
    with col2:
        topic = st.text_input("Security Topic", placeholder="e.g. Phishing, SQLi, VPN")

    st.write("") # Spacer
    generate_btn = st.button("INITIATE LEARNING PROTOCOL")

# --- 5. AI LOGIC & EXECUTION ---
if generate_btn:
    if topic:
        with st.spinner("🚀 Decoding complex protocols..."):
            try:
                # Retrieve API Key from Streamlit Secrets
                api_key = os.getenv("GEMINI_API_KEY")
                
                if not api_key:
                    st.error("🚨 System Error: API Key not found in Secrets.")
                else:
                    genai.configure(api_key=api_key)
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    
                    # The Instructional Prompt
                    prompt = f"""
                    Act as GhostRoot, an elite but friendly cyber security mentor. 
                    Your mission is to explain '{topic}' to a learner at the '{level}' level.
                    
                    Structure your response as follows:
                    1. **THE REAL-WORLD ANALOGY**: Explain the concept using a vivid everyday example (like a house, a bank, or a car).
                    2. **THE SHADOW REALITY**: Explain how this analogy maps directly to technical cybersecurity.
                    3. **GHOST PROTOCOL**: Provide one expert, actionable tip to stay safe or implement this properly.
                    
                    Use clear markdown, bolding, and a professional yet 'hacker-cool' tone.
                    """
                    
                    response = model.generate_content(prompt)
                    
                    # Display the response in a Rich UI Card
                    st.markdown(f"""
                        <div class="lesson-card">
                            {response.text}
                        </div>
                    """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"❌ Connection to Neural Network failed. Error: {str(e)}")
    else:
        st.warning("⚠️ Please specify a target topic to begin the session.")

# --- 6. FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.caption("GhostRoot AI v1.0 | Built by Srivatsa A | Unauthorized access is strictly encouraged (for learning).")
