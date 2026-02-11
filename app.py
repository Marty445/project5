import streamlit as st
st.title("Test")
st.write("What is the largest ocean in the world?")
user_answer1 = st.text_input(" Your answer", key="w")
if st.button("Check answer for question 1"):
  if user_answer1.strip().lower() == "The Pacific Ocean":
    st.success("Correct!")
  else:
    st.error("Incorrect!")
st.write("Which country has the largest population in the world?")
user_answer1 = st.text_input(" Your answer", key="w")
if st.button("Check answer for question 2"):
  if user_answer1.strip().lower() == "India":
    st.success("Correct!")
  else:
    st.error("Incorrect!")
st.write("What is the longest river in the world?")
user_answer1 = st.text_input(" Your answer", key="w")
if st.button("Check answer for question 3"):
  if user_answer1.strip().lower() == "The Nile River":
    st.success("Correct!")
  else:
    st.error("Incorrect!")
st.write("Which continent is the Sahara Desert located on?")
user_answer1 = st.text_input(" Your answer", key="w")
if st.button("Check answer for question 4"):
  if user_answer1.strip().lower() == "Africa":
    st.success("Correct!")
  else:
    st.error("Incorrect!")
st.write("What is the capital city of Japan?")
user_answer1 = st.text_input(" Your answer", key="w")
if st.button("Check answer for question 5"):
  if user_answer1.strip().lower() == "Tokyo":
    st.success("Correct!")
  else:
    st.error("Incorrect!")

