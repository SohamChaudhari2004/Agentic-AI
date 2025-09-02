from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
import os
llm = ChatMistralAI(
    model_name= 'mistral-large-latest',
    temperature= 0.6,
    api_key= os.getenv("MISTRAL_API_KEY")
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that assists with a detailed research on any given topic.",
        ),
        ("human", "{input}"),
    ]
)

chain = prompt | llm

def research(input: str):
    return chain.invoke({"input": input})