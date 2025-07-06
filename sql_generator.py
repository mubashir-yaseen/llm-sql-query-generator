import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

def generate_sql_query(user_input):
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("Please set the OPENAI_API_KEY environment variable.")
    
    llm = ChatOpenAI(temperature=0, openai_api_key=openai_api_key)

    prompt = PromptTemplate(
        input_variables=["user_input"],
        template="Convert the following natural language request into an SQL query:\n\n{user_input}"
    )
    query = prompt.format(user_input=user_input)
    response = llm.predict(query)

    return response.strip()
