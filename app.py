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
    page_icon="💻"
)

# Check if the Google API key is provided in the sidebar
with st.sidebar:
    if api_key:
        st.success('API key already provided!', icon='✅')
    else:
        api_key = st.text_input('Enter Google API Key:', type='password')
        if not api_key.startswith('AI'):
            st.warning('Please enter your API Key!', icon='⚠️')
        else:
            st.success('Success!', icon='✅')
    os.environ['GOOGLE_API_KEY'] = api_key
    "[Get a Google Gemini API key](https://ai.google.dev/)"
    "[View the source code](https://github.com/gatwirival/TeachcompAI)"

# Set the title and caption for the Streamlit app
st.title("💻 Computer Skills Tutor")
st.caption("📚 A Streamlit app powered by Google Gemini to teach professionals basic computer skills")

# Create tabs for different skill categories
tab1, tab2, tab3 = st.tabs(["📝 Basic Office Skills", "🌐 Internet Skills", "🔧 Troubleshooting"])

# Code for Basic Office Skills
with tab1:
    st.write("📄 Learn Basic Office Skills")
    st.subheader("📝 Generate Office Skills Tutorials")

    skill_name = st.text_input("Enter the office skill you want to learn (e.g., Excel basics, Word formatting):", key="skill_name", value="Excel basics")
    level = st.selectbox("Select your proficiency level:", ["Beginner", "Intermediate", "Advanced"], key="level")

    prompt = f"""Create a tutorial for {skill_name} for a {level} level professional.
    """

    config = {
        "temperature": 0.8,
        "max_output_tokens": 2048,
    }

    generate_tutorial = st.button("Generate Tutorial", key="generate_tutorial")
    model = genai.GenerativeModel("gemini-pro", generation_config=config)
    if generate_tutorial and prompt:
        with st.spinner("Generating your tutorial using Gemini..."):
            tutorial_tab, prompt_tab = st.tabs(["Tutorial", "Prompt"])
            with tutorial_tab:
                response = model.generate_content(prompt)
                if response:
                    st.write("Your tutorial:")
                    st.write(response.text)
            with prompt_tab:
                st.text(prompt)

# Code for Internet Skills
with tab2:
    st.write("🌐 Learn Internet Skills")
    st.subheader("🔍 Generate Internet Skills Tutorials")

    skill_name = st.text_input("Enter the internet skill you want to learn (e.g., safe browsing, effective searching):", key="internet_skill_name", value="safe browsing")
    level = st.selectbox("Select your proficiency level:", ["Beginner", "Intermediate", "Advanced"], key="internet_level")

    prompt = f"""Create a tutorial for {skill_name} for a {level} level professional.
    """

    config = {
        "temperature": 0.8,
        "max_output_tokens": 2048,
    }

    generate_tutorial = st.button("Generate Tutorial", key="generate_internet_tutorial")
    model = genai.GenerativeModel("gemini-pro", generation_config=config)
    if generate_tutorial and prompt:
        with st.spinner("Generating your tutorial using Gemini..."):
            tutorial_tab, prompt_tab = st.tabs(["Tutorial", "Prompt"])
            with tutorial_tab:
                response = model.generate_content(prompt)
                if response:
                    st.write("Your tutorial:")
                    st.write(response.text)
            with prompt_tab:
                st.text(prompt)

# Code for Troubleshooting
with tab3:
    st.write("🔧 Learn Troubleshooting Skills")
    st.subheader("🛠️ Generate Troubleshooting Tutorials")

    issue_name = st.text_input("Enter the issue you want to troubleshoot (e.g., computer won't start, slow internet):", key="issue_name", value="slow internet")
    level = st.selectbox("Select your proficiency level:", ["Beginner", "Intermediate", "Advanced"], key="troubleshoot_level")

    prompt = f"""Create a troubleshooting guide for {issue_name} for a {level} level professional.
    """

    config = {
        "temperature": 0.8,
        "max_output_tokens": 2048,
    }

    generate_guide = st.button("Generate Troubleshooting Guide", key="generate_troubleshooting_guide")
    model = genai.GenerativeModel("gemini-pro", generation_config=config)
    if generate_guide and prompt:
        with st.spinner("Generating your troubleshooting guide using Gemini..."):
            guide_tab, prompt_tab = st.tabs(["Guide", "Prompt"])
            with guide_tab:
                response = model.generate_content(prompt)
                if response:
                    st.write("Your guide:")
                    st.write(response.text)
            with prompt_tab:
                st.text(prompt)
