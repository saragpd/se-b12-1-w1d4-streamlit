import streamlit as st


# -----------------------------
# Grade calculation from Day 2
# -----------------------------
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Thisharvi Student Grade Manager",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Thisharvi School")
st.subheader("Student Grade Manager")

st.write("Add student marks and view the class performance.")


# -----------------------------
# Session State
# -----------------------------
if "students" not in st.session_state:
    st.session_state.students = []


# -----------------------------
# Add Student Form
# -----------------------------
st.header("➕ Add Student")

with st.form("add_student"):
    name = st.text_input("Student Name")

    mark = st.number_input(
        "Mark",
        min_value=0,
        max_value=100,
        value=0,
        step=1
    )

    submitted = st.form_submit_button("Add Student")

    if submitted:
        if not name.strip():
            st.error("Please enter the student name.")
        else:
            student = {
                "Name": name.strip(),
                "Mark": mark,
                "Grade": get_grade(mark)
            }

            st.session_state.students.append(student)

            st.success(f"{name.strip()} added successfully!")


# -----------------------------
# Display Students
# -----------------------------
st.header("📋 Student Results")

if st.session_state.students:

    st.table(st.session_state.students)

    # Get all marks
    marks = [student["Mark"] for student in st.session_state.students]

    # Class calculations
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    # -----------------------------
    # Class Metrics
    # -----------------------------
    st.header("📊 Class Performance")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Class Average", f"{average:.2f}")

    with col2:
        st.metric("Highest Mark", highest)

    with col3:
        st.metric("Lowest Mark", lowest)

else:
    st.info("No students added yet. Add the first student using the form above.")
