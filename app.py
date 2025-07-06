import streamlit as st
from sql_generator import generate_sql_query

st.set_page_config(page_title="LLM SQL Query Generator", layout="wide")

st.title("🧠 LLM-Based SQL Query Generator")
st.markdown("Convert plain English prompts into SQL queries using OpenAI and LangChain.")

user_input = st.text_input("Enter your natural language query:", "")

if st.button("Generate SQL Query"):
    if user_input:
        sql_query = generate_sql_query(user_input)
        st.code(sql_query, language='sql')
    else:
        st.warning("Please enter a query to generate SQL.")
