import openai
from langchain.chat_models import ChatOpenAI

# Set your OpenAI API key
key = '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'

def chat(prompt):
    chat = ChatOpenAI(
        openai_api_key=key,
        model_name="gpt-3.5-turbo",
        temperature=0.7
    )
    return chat.predict(prompt)
