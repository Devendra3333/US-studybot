import streamlit as st
from study_bot import chat

def main():
    st.title("US Study Bot")

    prompt = st.text_input("You:", "")
    if st.button("Send"):
        if prompt:
            with st.spinner("Thinking..."):
                response = chat(prompt)
            st.text_area("Bot:", response, height=500)
        else:
            st.warning("Please enter something.")

if __name__ == "__main__":
    main()
