import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Google API key from environment variables or secrets
api_key = os.getenv("GOOGLE_API_KEY", st.secrets.get("GOOGLE_API_KEY"))

# Configure Google Generative AI with the API key
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

    st.markdown("[Get a Google Gemini API key](https://makersuite.google.com/app/home)")
    st.markdown("[View the source code](https://github.com/gatwirival/TeachcompAI)")

# Page navigation
pages = ["Home", "Quizzes"]
page = st.sidebar.radio("Navigation", options=pages)

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

# Function to generate quiz
def generate_quiz(topic):
    prompt = f"Generate a quiz on {topic} with 5 multiple-choice questions."
    config = {
        "temperature": 0.8,
        "max_output_tokens": 1024,
    }
    model = genai.GenerativeModel("gemini-pro", generation_config=config)
    with st.spinner("Generating your quiz using Gemini..."):
        response = model.generate_content(prompt)
        if response:
            st.write("### Your quiz:")
            st.write(response.text)

# Home page
if page == "Home":
    # Set the title and caption for the Streamlit app
    st.title("💻 Computer Skills Tutor")
    st.caption("📚 A Streamlit app powered by Google Gemini to teach professionals basic computer skills")

    # Create tabs for different skill categories
    tabs = st.tabs(["📝 Basic Office Skills", "🌐 Internet Skills", "🔧 Troubleshooting", "🔍 Research Skills", "🎨 Design Skills", "📈 Data Analysis"])

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

    # Data Analysis Skills
    with tabs[5]:
        st.header("📈 Learn Data Analysis Skills")
        st.subheader("📊 Generate Data Analysis Skills Tutorials")

        skill_name = st.text_input("Enter the data analysis skill you want to learn (e.g., data visualization, statistical analysis):", key="data_analysis_skill_name", value="data visualization")
        level = st.selectbox("Select your proficiency level:", ["Beginner", "Intermediate", "Advanced"], key="level_data_analysis")

        if st.button("Generate Tutorial", key="generate_data_analysis_tutorial"):
            generate_content(skill_name, level, "Data Analysis")

    # Adding a FAQ section
    st.markdown("---")
    st.markdown("### Frequently Asked Questions (FAQ)")
    faq_expander = st.expander("How does this app work?")
    faq_expander.write("""
    This app uses the Google Gemini API to generate tutorials and guides for various computer skills. You provide the skill and your proficiency level, and the app generates content tailored to your needs.
    """)

    faq_expander = st.expander("Is the content generated always accurate?")
    faq_expander.write("""
    The content generated by the Google Gemini API is based on the information provided and is not guaranteed to be accurate or comprehensive. It should be used as a supplement to other learning resources.
    """)

    faq_expander = st.expander("How can I get a Google Gemini API key?")
    faq_expander.write("""
    You can get a Google Gemini API key by signing up on the [Google Gemini Makersuite website](https://makersuite.google.com/app/home).
    """)

    # Disclaimer
    st.markdown("---")
    st.markdown("### Disclaimer")
    st.markdown("""
    This app is intended for educational purposes only. The content generated by the Google Gemini API is based on the information provided and is not guaranteed to be accurate or comprehensive.
    Please use the tutorials and guides as a supplement to other learning resources.
    The developers of this app are not responsible for any errors or omissions in the content generated.
    """)

# Quizzes page
elif page == "Quizzes":
    st.title("📝 Computer Skills Quizzes")
    st.caption("🎯 Test your knowledge with quizzes generated by Google Gemini")

    quiz_topic = st.text_input("Enter the topic for the quiz (e.g., Excel basics, safe browsing):", key="quiz_topic", value="Excel basics")

    if st.button("Generate Quiz", key="generate_quiz"):
        generate_quiz(quiz_topic)
