import streamlit as st
import google.generativeai as genai
import os

# 1. Setup - Use an environment variable for your key
# Get your free key at: https://aistudio.google.com/
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

st.set_page_config(page_title="Cyber Guard Academy", page_icon="🛡️")

st.title("🛡️ Cyber Guard Academy")
st.subheader("Master Security through Daily Life Examples")

# 2. User Input
level = st.select_slider(
    "Select your current knowledge level:",
    options=["Beginner", "Intermediate", "Advanced", "Expert"]
)

topic = st.text_input("What do you want to learn about? (e.g., Phishing, Passwords, VPNs)")

if st.button("Teach Me!"):
    if topic:
        with st.spinner("Translating tech-speak into real life..."):
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # The "Expert Teacher" Prompt
            prompt = (
                f"You are a master cybersecurity teacher. Explain the concept of '{topic}' "
                f"to a learner at the '{level}' level. Use a clear, relatable analogy "
                f"from daily life (like a house, a car, or a grocery store). "
                f"Keep it engaging and conclude with one 'Pro-Tip' for staying safe."
            )
            
            response = model.generate_content(prompt)
            st.markdown("---")
            st.markdown(response.text)
    else:
        st.warning("Please enter a topic first!")
