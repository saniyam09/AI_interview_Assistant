import streamlit as st
from groq import Groq

st.set_page_config(page_title='AI Interview Assistant' , layout='centered')
st.title(' AI Interview Assistant')
st.caption('Practice interviews with AI-generated questions and constructive feedback.') 
st.caption('Launched By Saniya M')
st.write('Department of AI & DS')

try:
  client = Groq(api_key=st.secrets['GROQ_API_KEY'])
  st.write("API connections successfully")
except (KeyError, FileNotFoundError):
  st.error('GROQ_API_KEY is missing . Add it to Streamlit Cloud -> App setting secrets')
  st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("AI Interview Assistant")

role = st.selectbox("Select Job Role",[
"Python Developer",
"Java Developer",
"Data Analyst",
"Machine Learning Engineer",
"Software Engineer",
"HR Executive"
])

if st.button("Generate Interview questions"):
  prompt = "Generate  5 interview questions for the role of " + role
  response = client.chat.completions.create(
    model = "openai/gpt-oss-120b",
    messages= [
              {"role" : "system", "content" : "You are an expert technical Interviewer"},
        {"role" : "user" ,"content" : prompt}
  ]
  )

  output = response.choices[0].message.content
  st.write(output)
