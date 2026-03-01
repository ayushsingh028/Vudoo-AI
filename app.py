import streamlit as st
import google.generativeai as genai

# Website Title
st.set_page_config(page_title="Vudoo AI Pro", page_icon="🪄")

# API Key Secrets se uthana
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("Setup incomplete! Please add GEMINI_API_KEY in Streamlit Settings.")

st.title("🪄 Vudoo AI Pro")
st.subheader("Viral YouTube Hook Generator")

# Free Limit Logic
if 'usage_count' not in st.session_state:
    st.session_state.usage_count = 0

limit = 3
remaining = limit - st.session_state.usage_count

if remaining > 0:
    st.info(f"Aapke paas {remaining} free search bache hain.")
    topic = st.text_input("Apna video topic likhein:")
    
    if st.button("Generate Hooks 🔥"):
        if topic:
            with st.spinner("AI hooks bana raha hai..."):
                prompt = f"Write 3 viral YouTube hooks for: {topic}. High retention, curiosity gap."
                response = model.generate_content(prompt)
                st.session_state.usage_count += 1
                st.success("Ye rahe viral hooks!")
                st.write(response.text)
else:
    st.error("⚡ Free Limit Khatam!")
    st.write("For Unlimited hooks recharage ₹49.")
    st.code("UPI ID: 8318128201@fam", language=None)
    st.link_button("Pay via FamPay/UPI", "upi://pay?pa=ayush@fampay&pn=VudooAI&am=29&cu=INR")
        except Exception as e:
            st.error(f"An error occurred: {e}")
