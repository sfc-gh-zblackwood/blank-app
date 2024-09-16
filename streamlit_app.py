import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.write("My name is Zachary")

st.button("Press me!")

st.checkbox("Check me")

students = ["Felicity", "Elsie", "Emory", "Elizabeth", "Kathryn"]

st.write("Yo")

st.write(students)

student = st.selectbox("Who is the best student?", students)

st.write(student)
