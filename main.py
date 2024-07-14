import os
import streamlit as st
import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_community.chat_models import ChatOpenAI
from apikey import apikey

# Place your openai API key here
os.environ["OPENAI_API_KEY"] = ""

# Define Streamlit app
def app():
    st.title("AI SQL Brain. :brain:")
    st.title("(LLM App By :green[Adad Al Sabab])")
    st.markdown(":red[Talk to your Database] with **:blue[natural language]**.")
    st.write("Upload a CSV file and enter a query to get an answer.")
    file = st.file_uploader("Upload CSV file", type=["csv"])
    if file is not None:
        data = pd.read_csv(file)
        st.write("Data Preview:")
        st.dataframe(data.head())
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        agent = create_pandas_dataframe_agent(llm, data,agent_type="openai-tools", verbose=True)

        query = st.text_input("Enter a query:")

    if st.button("Execute"):
        answer = agent.run(query)
        st.write("Answer:")
        st.write(answer)


if __name__ == "__main__":
    app()
