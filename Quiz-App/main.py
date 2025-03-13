import streamlit as st  # for the web interface
import random # for randomizing the question
import time # 3 for the timer

# Title for app
st.title("📝 Quiz Application")

# quiz Questions, options and answers in the form of the list of dictionary
Questions = [
    {
        "Question": "What is the capital of Pakistan?",
        "Options" : ["Karachi", "Lahore", "Islamabad", "Peshawar"],
        "answer": "Islamabad"
    },
    {
        "Question": "Which programming language is known as the backbone of web development?",
        "Options": ["Python", "JavaScript", "C++", "Java"],
        "answer": "JavaScript"
    },
        {
        "Question": "What is the largest planet in our solar system?",
        "Options": ["Earth", "Jupiter", "Mars", "Venus"],
        "answer": "Jupiter"
    },
    {
        "Question": "Who wrote 'Hamlet'?",
        "Options": ["Charles Dickens", "William Shakespeare", "J.K. Rowling", "Leo Tolstoy"],
        "answer": "William Shakespeare"
    },
    {
        "Question": "Which element has the chemical symbol 'O'?",
        "Options": ["Gold", "Oxygen", "Silver", "Iron"],
        "answer": "Oxygen"
    },
    {
        "Question": "What is the powerhouse of the cell?",
        "Options": ["Nucleus", "Mitochondria", "Ribosome", "Golgi apparatus"],
        "answer": "Mitochondria"
    },
    {
        "Question": "Which country is famous for the Great Wall?",
        "Options": ["India", "China", "Japan", "Russia"],
        "answer": "China"
    },
    {
        "Question": "What is the currency of the United Kingdom?",
        "Options": ["Euro", "Dollar", "Pound Sterling", "Rupee"],
        "answer": "Pound Sterling"
    },
    {
        "Question": "Which gas do plants absorb from the atmosphere?",
        "Options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "answer": "Carbon Dioxide"
    },
    {
        "Question": "What is the capital of Japan?",
        "Options": ["Seoul", "Tokyo", "Bangkok", "Beijing"],
        "answer": "Tokyo"
    }
]


# Initialize a random questions if none exists in the session state
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(Questions)

# Get the current question from session state
question = st.session_state.current_question

# display the questions
st.subheader(question["Question"])

# Create radio button for the options
selected_option = st.radio("Choose your answer", question["Options"], key="answer")


# Submit button to check answer
if st.button("Submit Answer"):

    # check if the answer is correct by comparing the selected option with the answer in the question dictionary 
    if selected_option == question["answer"]:
        st.success("✅ Correct!")
        # st.balloons
    else:
        st.error("❌ Incorrect! the correct answer is: " + question["answer"])
    
    # Wait for 3 second before showing the nest question 
    time.sleep(3)

    # Select a new random question
    st.session_state.current_question = random.choice(Questions)

    # Rerun the app to display the next question 
    st.rerun()