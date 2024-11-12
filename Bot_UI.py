import streamlit as st
from study_bot import final_result

st.set_page_config(layout="wide")
def main():
    st.title("US Study Bot")
    prompt = st.text_input("You:", "")
    if st.button("Send"):
        if prompt:
            with st.spinner("Thinking..."):
                response = final_result(prompt)
            st.text_area("Bot:", value=response, height=500)
        else:
            st.warning("Please enter something.")

if __name__ == "__main__":
    print("UI Page")
    main()
