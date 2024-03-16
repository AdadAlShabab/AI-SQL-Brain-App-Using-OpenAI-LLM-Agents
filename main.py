import os
import streamlit as st
import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
from apikey import apikey

# Place your openai API key here
os.environ["OPENAI_API_KEY"] = "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"


# Define Streamlit app
def app():
    st.title("AI SQL Brain. :brain: ")
    st.markdown(":red[Talk to your Database] with **:blue[natural language]**.")
    st.write("Upload a CSV file and enter a query to get an answer.")
    file = st.file_uploader("Upload CSV file", type=["csv"])
    if file is not None:
        data = pd.read_csv(file)
        st.write("Data Preview:")
        st.dataframe(data.head())

        agent = create_pandas_dataframe_agent(OpenAI(temperature=0), data, verbose=True)

        query = st.text_input("Enter a query:")

    if st.button("Execute"):
        answer = agent.run(query)
        st.write("Answer:")
        st.write(answer)


if __name__ == "__main__":
    app()
