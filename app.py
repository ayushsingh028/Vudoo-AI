import streamlit as st
import google.generativeai as genai

# Website Configuration
st.set_page_config(page_title="Vudoo AI Pro", page_icon="🪄")

# Load API Key from Streamlit Secrets
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("Setup incomplete! Please add GEMINI_API_KEY in Streamlit Secrets.")

st.title("🪄 Vudoo AI Pro")
st.subheader("Viral YouTube Hook Generator")

# Usage Logic (Daily Limit)
if 'usage_count' not in st.session_state:
    st.session_state.usage_count = 0

limit = 3
remaining = limit - st.session_state.usage_count

if remaining > 0:
    st.info(f"You have {remaining} free generations left.")
    topic = st.text_input("Enter your video topic (e.g., Gaming Tips):")
    
    if st.button("Generate Hooks 🔥"):
        if topic:
            with st.spinner("Vudoo AI is generating hooks..."):
                prompt = f"Write 3 viral YouTube hooks for: {topic}. High retention, curiosity gap."
                response = model.generate_content(prompt)
                st.session_state.usage_count += 1
                st.success("Here are your viral hooks!")
                st.write(response.text)
        else:
            st.warning("Please enter a topic first.")
else:
    # Monetization Section
    st.error("⚡ Daily Free Limit Reached!")
    st.write("Upgrade to **Vudoo AI Pro** for unlimited viral hooks.")
    
    upi_id = "8318128201@fam" 
    st.code(f"UPI ID: {upi_id}", language=None)
    
    st.write("Pay **₹29** and send the screenshot on Instagram for unlimited access.")
    st.link_button("Pay via FamPay/UPI", f"upi://pay?pa={upi_id}&pn=VudooAI&am=29&cu=INR")
    st.info("Instant activation after payment verification.")
