import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="CGPA Calculator",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Advanced CGPA Calculator")

# Step 1
num_students = st.number_input(
    "Enter Number of Students",
    min_value=1,
    value=1
)

num_subjects = st.number_input(
    "Enter Number of Subjects",
    min_value=1,
    value=5
)

max_marks = st.number_input(
    "Enter Maximum Marks Per Subject",
    min_value=1,
    value=100
)

st.divider()

students_data = []

for i in range(num_students):

    st.subheader(f"Student {i+1}")

    student_name = st.text_input(
        f"Student Name {i+1}",
        key=f"name_{i}"
    )

    marks = []

    cols = st.columns(min(3, num_subjects))

    for j in range(num_subjects):

        mark = st.number_input(
            f"Subject {j+1}",
            min_value=0.0,
            max_value=float(max_marks),
            key=f"student_{i}_subject_{j}"
        )

        marks.append(mark)

    students_data.append({
        "name": student_name,
        "marks": marks
    })

st.divider()

if st.button("Review Information"):

    review_data = []

    for student in students_data:
        review_data.append(
            [student["name"]] + student["marks"]
        )

    columns = ["Student Name"] + [
        f"Subject {i+1}" for i in range(num_subjects)
    ]

    review_df = pd.DataFrame(review_data, columns=columns)

    st.subheader("📋 Review Details")
    st.dataframe(review_df, use_container_width=True)

    st.session_state.reviewed = True

if st.session_state.get("reviewed", False):

    confirm = st.checkbox(
        "I confirm all entered marks are correct."
    )

    if confirm:

        if st.button("Calculate CGPA"):

            results = []

            for student in students_data:

                total_marks = sum(student["marks"])
                maximum_total = max_marks * num_subjects

                percentage = (
                    total_marks / maximum_total
                ) * 100

                cgpa = percentage / 9.5

                if cgpa < 5:
                    remark = "😔 Work harder next time"
                else:
                    remark = "🎉 Hurraaahhhh, you are a genius"

                results.append({
                    "Student": student["name"],
                    "Total Marks": round(total_marks, 2),
                    "Percentage": round(percentage, 2),
                    "CGPA": round(cgpa, 2),
                    "Remark": remark
                })

            result_df = pd.DataFrame(results)

            st.success("CGPA Calculated Successfully!")

            st.subheader("🏆 Results")

            st.dataframe(
                result_df,
                use_container_width=True
            )

            st.balloons()