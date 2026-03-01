import streamlit as st
import google.generativeai as genai

# Website ka naam aur icon tab ke liye
st.set_page_config(page_title="Vudoo AI", page_icon="🪄")

# Website Interface
st.title("🪄 Vudoo AI")
st.subheader("Viral YouTube Hook Generator")
st.write("Enter your video topic and get 3 highly engaging hooks to boost retention!")

# API Key Input
api_key = st.text_input("Paste your Gemini API Key here (Secure & Private):", type="password")

# User Topic Input (Examples updated)
topic = st.text_input("Enter your video topic (e.g., Free Fire headshot trick, iQOO Neo 10R review, After Effects tutorial):")

# Generate Logic
if st.button("Generate Hooks 🔥"):
    if not api_key:
        st.warning("Please paste your API key first!")
    elif not topic:
        st.warning("Please enter a video topic!")
    else:
        try:
            # Connecting to AI
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-2.5-flash') 
            
            # The Master Prompt
            prompt = f"You are a master YouTube retention expert. The user is making a video about '{topic}'. Write 3 punchy, 10-second script hooks in English designed to stop someone from clicking away. Keep it natural, create a strong curiosity gap, and make it sound professional. Do not use generic words like 'Hey guys'."
            
            with st.spinner("Vudoo AI is crafting your hooks..."):
                response = model.generate_content(prompt)
                st.success("Here are your Viral Hooks!")
                st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
