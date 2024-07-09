import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Google API key from the environment variables or secrets
api_key = os.getenv("GOOGLE_API_KEY", st.secrets.get("GOOGLE_API_KEY"))

# Configure the Google Generative AI with the API key
genai.configure(api_key=api_key)

# Set the page configuration for the Streamlit app
st.set_page_config(
    page_title="Computer Skills Tutor",
    page_icon="💻",
    layout="wide",
)

# Sidebar for API key input and links
with st.sidebar:
    st.title("Settings")
    if api_key:
        st.success('API key already provided!', icon='✅')
    else:
        api_key = st.text_input('Enter Google API Key:', type='password')
        if not api_key.startswith('AI'):
            st.warning('Please enter your API Key!', icon='⚠️')
        else:
            st.success('Success!', icon='✅')
    os.environ['GOOGLE_API_KEY'] = api_key

    st.markdown("[Get a Google Gemini API key]( https://makersuite.google.com/app/home)")
    st.markdown("[View the source code](https://github.com/gatwirival/TeachcompAI)")

# Set the title and caption for the Streamlit app
st.title("💻 Computer Skills Tutor")
st.caption("📚 A Streamlit app powered by Google Gemini to teach professionals basic computer skills")

# Create tabs for different skill categories
tabs = st.tabs(["📝 Basic Office Skills", "🌐 Internet Skills", "🔧 Troubleshooting", "🔍 Research Skills", "🎨 Design Skills"])

# Function to generate content
def generate_content(skill_name, level, category):
    prompt = f"Create a tutorial for {skill_name} for a {level} level professional in the category of {category}."
    config = {
        "temperature": 0.8,
        "max_output_tokens": 2048,
    }
    model = genai.GenerativeModel("gemini-pro", generation_config=config)
    with st.spinner("Generating your tutorial using Gemini..."):
        response = model.generate_content(prompt)
        if response:
            st.write("### Your tutorial:")
            st.write(response.text)

# Basic Office Skills
with tabs[0]:
    st.header("📄 Learn Basic Office Skills")
    st.subheader("📝 Generate Office Skills Tutorials")

    skill_name = st.text_input("Enter the office skill you want to learn (e.g., Excel basics, Word formatting):", key="skill_name", value="Excel basics")
    level = st.selectbox("Select your proficiency level:", ["Beginner", "Intermediate", "Advanced"], key="level_office")

    if st.button("Generate Tutorial", key="generate_office_tutorial"):
        generate_content(skill_name, level, "Office Skills")

# Internet Skills
with tabs[1]:
    st.header("🌐 Learn Internet Skills")
    st.subheader("🔍 Generate Internet Skills Tutorials")

    skill_name = st.text_input("Enter the internet skill you want to learn (e.g., safe browsing, effective searching):", key="internet_skill_name", value="safe browsing")
    level = st.selectbox("Select your proficiency level:", ["Beginner", "Intermediate", "Advanced"], key="level_internet")

    if st.button("Generate Tutorial", key="generate_internet_tutorial"):
        generate_content(skill_name, level, "Internet Skills")

# Troubleshooting
with tabs[2]:
    st.header("🔧 Learn Troubleshooting Skills")
    st.subheader("🛠️ Generate Troubleshooting Tutorials")

    issue_name = st.text_input("Enter the issue you want to troubleshoot (e.g., computer won't start, slow internet):", key="issue_name", value="slow internet")
    level = st.selectbox("Select your proficiency level:", ["Beginner", "Intermediate", "Advanced"], key="level_troubleshooting")

    if st.button("Generate Troubleshooting Guide", key="generate_troubleshooting_guide"):
        generate_content(issue_name, level, "Troubleshooting")

# Research Skills
with tabs[3]:
    st.header("🔍 Learn Research Skills")
    st.subheader("📚 Generate Research Skills Tutorials")

    skill_name = st.text_input("Enter the research skill you want to learn (e.g., literature review, data analysis):", key="research_skill_name", value="literature review")
    level = st.selectbox("Select your proficiency level:", ["Beginner", "Intermediate", "Advanced"], key="level_research")

    if st.button("Generate Tutorial", key="generate_research_tutorial"):
        generate_content(skill_name, level, "Research Skills")

# Design Skills
with tabs[4]:
    st.header("🎨 Learn Design Skills")
    st.subheader("🖌️ Generate Design Skills Tutorials")

    skill_name = st.text_input("Enter the design skill you want to learn (e.g., graphic design, UI/UX):", key="design_skill_name", value="graphic design")
    level = st.selectbox("Select your proficiency level:", ["Beginner", "Intermediate", "Advanced"], key="level_design")

    if st.button("Generate Tutorial", key="generate_design_tutorial"):
        generate_content(skill_name, level, "Design Skills")

# Add a disclaimer at the bottom of the app
st.markdown("---")
st.markdown("### Disclaimer")
st.markdown("""
This app is intended for educational purposes only. The content generated by the Google Gemini API is based on the information provided and is not guaranteed to be accurate or comprehensive.
Please use the tutorials and guides as a supplement to other learning resources.
The developers of this app are not responsible for any errors or omissions in the content generated.
""")
