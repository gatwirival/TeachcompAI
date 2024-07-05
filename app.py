import streamlit as st
from fpdf import FPDF
from googletrans import Translator
from google.generativeai import GenerativeModel, configure
from dotenv import load_dotenv
import os
import logging

# Load environment variables
load_dotenv()
google_api_key = os.getenv('GOOGLE_API_KEY')

# Configure logging
logging.basicConfig(filename='app.log', level=logging.ERROR)

# Configure the Google Generative AI
configure(api_key=google_api_key)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

system_prompt = """
You are a domain expert in computer education. You are tasked with
creating educational content for professionals to learn basic computer skills.
Your expertise will help in crafting detailed lessons and quizzes.

Your key responsibilities:
1. Detailed Lessons: Provide comprehensive explanations on computer basics, internet usage, and productivity software.
2. Quizzes: Create questions that help reinforce the learning of the lesson content.
3. Accessibility: Ensure the content is clear and understandable for learners with different levels of prior knowledge.
"""

model = GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=generation_config,
    safety_settings=safety_settings
)

st.set_page_config(page_title="Basic Computer Skills", page_icon="💻", layout="wide")
st.title("Basic Computer Skills for Professionals 💻")
st.subheader("An interactive app to teach basic computer skills")

translator = Translator()
languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh-cn"
}
selected_language = st.selectbox("Choose the language for the course", list(languages.keys()))

# Define educational content using Gemini API
def generate_course_content(prompt):
    response = model.generate_content([prompt, system_prompt])
    return response.text

courses = {
    "Introduction to Computers": {
        "prompt": """
        Create a lesson on Introduction to Computers including:
        1. What is a computer?
        2. Basic components of a computer.
        3. Operating systems and software.
        """,
        "quizzes": [
            {
                "question": "What is a computer?",
                "options": ["A typewriter", "An electronic device", "A cooking appliance"],
                "answer": "An electronic device"
            },
            {
                "question": "Which of these is a basic component of a computer?",
                "options": ["Monitor", "Keyboard", "Both"],
                "answer": "Both"
            },
            {
                "question": "Which of the following is an operating system?",
                "options": ["Windows", "MS Word", "Excel"],
                "answer": "Windows"
            }
        ]
    },
    "Using the Internet": {
        "prompt": """
        Create a lesson on Using the Internet including:
        1. How to browse the internet.
        2. Using search engines.
        3. Email management.
        """,
        "quizzes": [
            {
                "question": "Which of the following is a search engine?",
                "options": ["Google", "Facebook", "Microsoft Word"],
                "answer": "Google"
            },
            {
                "question": "What is a browser?",
                "options": ["A tool for cooking", "A software to browse the internet", "A type of computer"],
                "answer": "A software to browse the internet"
            },
            {
                "question": "Which is a common email provider?",
                "options": ["Yahoo Mail", "Spotify", "Netflix"],
                "answer": "Yahoo Mail"
            }
        ]
    },
    "Productivity Software": {
        "prompt": """
        Create a lesson on Productivity Software including:
        1. Basics of word processing.
        2. Creating spreadsheets.
        3. Making presentations.
        """,
        "quizzes": [
            {
                "question": "Which software is used for word processing?",
                "options": ["Excel", "PowerPoint", "Word"],
                "answer": "Word"
            },
            {
                "question": "Which software is used for creating spreadsheets?",
                "options": ["Word", "Excel", "PowerPoint"],
                "answer": "Excel"
            },
            {
                "question": "Which software is used for making presentations?",
                "options": ["Excel", "Word", "PowerPoint"],
                "answer": "PowerPoint"
            }
        ]
    },
    "Computer Security Basics": {
        "prompt": """
        Create a lesson on Computer Security Basics including:
        1. Importance of computer security.
        2. Common security threats (viruses, malware, phishing).
        3. Best practices for maintaining computer security.
        """,
        "quizzes": [
            {
                "question": "What is the importance of computer security?",
                "options": ["To protect data", "To enhance gaming performance", "To increase internet speed"],
                "answer": "To protect data"
            },
            {
                "question": "Which of the following is a common security threat?",
                "options": ["Phishing", "Word Processing", "Spreadsheet Creation"],
                "answer": "Phishing"
            },
            {
                "question": "Which is a best practice for maintaining computer security?",
                "options": ["Sharing passwords", "Using strong passwords", "Ignoring software updates"],
                "answer": "Using strong passwords"
            }
        ]
    },
    "Introduction to Programming": {
        "prompt": """
        Create a lesson on Introduction to Programming including:
        1. What is programming?
        2. Basic concepts of programming (variables, loops, conditionals).
        3. Introduction to a programming language (e.g., Python).
        """,
        "quizzes": [
            {
                "question": "What is programming?",
                "options": ["Cooking food", "Writing instructions for computers", "Drawing pictures"],
                "answer": "Writing instructions for computers"
            },
            {
                "question": "Which of these is a basic concept of programming?",
                "options": ["Variables", "Recipes", "Songs"],
                "answer": "Variables"
            },
            {
                "question": "Which language is commonly used for programming?",
                "options": ["Python", "French", "Spanish"],
                "answer": "Python"
            }
        ]
    },
    "Database Basics": {
        "prompt": """
        Create a lesson on Database Basics including:
        1. What is a database?
        2. Types of databases (relational, non-relational).
        3. Basic SQL queries.
        """,
        "quizzes": [
            {
                "question": "What is a database?",
                "options": ["A collection of recipes", "A collection of data", "A collection of songs"],
                "answer": "A collection of data"
            },
            {
                "question": "Which of these is a type of database?",
                "options": ["Relational", "Fictional", "Musical"],
                "answer": "Relational"
            },
            {
                "question": "What does SQL stand for?",
                "options": ["Structured Query Language", "Simple Query Language", "Standard Query Language"],
                "answer": "Structured Query Language"
            }
        ]
    },
    "Networking Fundamentals": {
        "prompt": """
        Create a lesson on Networking Fundamentals including:
        1. What is a computer network?
        2. Types of networks (LAN, WAN).
        3. Basic networking concepts (IP addresses, routers).
        """,
        "quizzes": [
            {
                "question": "What is a computer network?",
                "options": ["A group of connected computers", "A type of computer", "A programming language"],
                "answer": "A group of connected computers"
            },
            {
                "question": "Which of these is a type of network?",
                "options": ["LAN", "RAM", "ROM"],
                "answer": "LAN"
            },
            {
                "question": "What does IP stand for in IP address?",
                "options": ["Internet Protocol", "Internal Process", "Internet Program"],
                "answer": "Internet Protocol"
            }
        ]
    },
    "Web Development Basics": {
        "prompt": """
        Create a lesson on Web Development Basics including:
        1. Introduction to HTML, CSS, and JavaScript.
        2. Building a simple webpage.
        3. Basics of web hosting.
        """,
        "quizzes": [
            {
                "question": "What is HTML used for?",
                "options": ["Styling a webpage", "Structuring a webpage", "Programming a webpage"],
                "answer": "Structuring a webpage"
            },
            {
                "question": "Which language is used for styling a webpage?",
                "options": ["HTML", "CSS", "JavaScript"],
                "answer": "CSS"
            },
            {
                "question": "Which language is used for making a webpage interactive?",
                "options": ["HTML", "CSS", "JavaScript"],
                "answer": "JavaScript"
            }
        ]
    },
    "Data Science and Analysis": {
        "prompt": """
        Create a lesson on Data Science and Analysis including:
        1. Introduction to data science.
        2. Basic data analysis techniques.
        3. Introduction to tools like Excel, Python, and R.
        """,
        "quizzes": [
            {
                "question": "What is data science?",
                "options": ["The study of stars", "The study of data", "The study of computers"],
                "answer": "The study of data"
            },
            {
                "question": "Which of these is a data analysis tool?",
                "options": ["Excel", "PowerPoint", "Word"],
                "answer": "Excel"
            },
            {
                "question": "Which programming language is commonly used in data science?",
                "options": ["Python", "HTML", "CSS"],
                "answer": "Python"
            }
        ]
    }
}

selected_course = st.selectbox("Select a course", list(courses.keys()))
course_prompt = courses[selected_course]["prompt"]
course_content = generate_course_content(course_prompt)
quizzes = courses[selected_course]["quizzes"]

if languages[selected_language] != "en":
    translated = translator.translate(course_content, dest=languages[selected_language])
    course_content = translated.text

st.markdown(course_content)

# Add a button to navigate to the quiz section
if st.button("Take Quiz"):
    st.session_state.quiz_mode = True

# Quiz Section
if st.session_state.get("quiz_mode"):
    st.subheader("Quiz")
    with st.form(key='quiz_form'):
        for idx, quiz in enumerate(quizzes):
            st.markdown(f"**{quiz['question']}**")
            options = quiz['options']
            chosen_option = st.radio("", options, key=f"quiz_{idx}")
            st.session_state[f"answer_{idx}"] = chosen_option

        submit_button = st.form_submit_button("Submit Answers")

        if submit_button:
            correct_answers = 0
            for idx, quiz in enumerate(quizzes):
                if st.session_state.get(f"answer_{idx}") == quiz['answer']:
                    correct_answers += 1
            st.write(f"You got {correct_answers} out of {len(quizzes)} correct.")

st.markdown("""
    **Disclaimer:** This app is designed to provide basic computer skills education.
    Always seek further professional training for more advanced skills.
""")
