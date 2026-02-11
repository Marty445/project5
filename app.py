import streamlit as st
st.write("What is the largest ocean in the world?")
st.text_input("The Pacific Ocean")
answer = st.radio(
  "What is the largest ocean in the world?",
  ("The Pacific Ocean", "ne")
)
if answer == "The Pacific Ocean":
  st.write("Correct!")
else:
  st.write("Incorrect!)
  
st.button()
