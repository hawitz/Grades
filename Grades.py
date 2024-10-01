import streamlit as st

# Function to calculate grades (includes absences, prelim exams, quizzes, etc.)
def calculate_grade(absences, prelim_exam, quizzes, requirements, recitation):
    try:
        # Attendance Calculation
        attendance = 100 - (absences * 10)

        if absences >= 4:
            return "FAILED due to absences."
        
        # Class Standing Calculation
        class_standing = (0.40 * quizzes) + (0.30 * requirements) + (0.30 * recitation)

        # Prelim Grade Calculation
        prelim_grade = (0.60 * prelim_exam) + (0.10 * attendance) + (0.30 * class_standing)

        # Midterm/Final Grades for 75 Passing
        prelim_percent = 0.20
        midterm_percent = 0.30
        final_percent = 0.50

        passing_grade = 75
        passing_grade2 = 90  # Dean's Lister Grade

        current_total = prelim_grade * prelim_percent
        required_total = passing_grade - current_total
        required_total2 = passing_grade2 - current_total

        # Midterm/Final Grades for 75 Passing
        required_midterm_and_final = required_total / (midterm_percent + final_percent) if required_total > 0 else 0

        # Midterm/Final Grades for 90 Passing (Dean's Lister)
        required_midterm_and_final2 = required_total2 / (midterm_percent + final_percent) if required_total2 > 0 else 0

        result = (f"**Prelim Grade:** {prelim_grade:.2f}%\n\n"
                  f"To pass with **75%**, you need a Midterm grade of **{required_midterm_and_final:.2f}%** "
                  f"and a Final grade of **{required_midterm_and_final:.2f}%**.\n\n"
                  f"To achieve **90%**, you need a Midterm grade of **{required_midterm_and_final2:.2f}%** "
                  f"and a Final grade of **{required_midterm_and_final2:.2f}%**.")
        return result

    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except Exception as e:
        return f"Error: {e}"

# Streamlit app layout
st.set_page_config(page_title="Grades Calculator", page_icon="📊", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #121212; /* Black background */
            color: #ff9800; /* Orange text */
            font-family: Arial, sans-serif;
        }
        .stButton>button {
            background-color: #ff9800; /* Orange button */
            color: white; /* Button text */
            border: none; /* No border */
            border-radius: 5px; /* Rounded corners */
            padding: 10px 20px; /* Padding */
        }
        .stButton>button:hover {
            background-color: #e68a00; /* Darker orange on hover */
        }
        .container {
            background-color: #1e1e1e; /* Darker gray for container */
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(255, 152, 0, 0.3);
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("🎓 Grades Calculator")
st.markdown("### Enter your grades and absences below:")

# User inputs
absences = st.number_input("Enter Number of Absences", min_value=0, step=1)
prelim_exam = st.number_input("Enter Prelim Exam Grade (0-100)", min_value=0.0, max_value=100.0, step=0.01)
quizzes = st.number_input("Enter Quizzes Grade (0-100)", min_value=0.0, max_value=100.0, step=0.01)
requirements = st.number_input("Enter Requirements Grade (0-100)", min_value=0.0, max_value=100.0, step=0.01)
recitation = st.number_input("Enter Recitation Grade (0-100)", min_value=0.0, max_value=100.0, step=0.01)

# Button to trigger grade calculation
if st.button("Calculate Grade"):
    # Calculate and display the result
    result = calculate_grade(absences, prelim_exam, quizzes, requirements, recitation)
    st.markdown(f"<div class='result'>{result}</div>", unsafe_allow_html=True)