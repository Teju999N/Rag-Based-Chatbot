import streamlit as st
from modules.chatbot import ask_chatbot

st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 RAG Chatbot")
st.write("Ask questions from the indexed PDF documents.")

question = st.text_input("Ask your question")

if st.button("Ask"):

    if question.strip():

        with st.spinner("Searching..."):

            answer, sources = ask_chatbot(question)

        st.success("Answer Generated")

        st.subheader("Answer")

        st.write(answer)

        st.subheader("Sources")

        shown = set()

        for source in sources:

            src = f"{source['filename']} (Page {source['page']})"

            if src not in shown:

                shown.add(src)

                st.write("•", src)