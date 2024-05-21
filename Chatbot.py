from openai import OpenAI
import streamlit as st

# Display FAQs
st.title("Greetings from the Elmento AI team!")

st.markdown("""
Elmento AI is a Russian neural network that analyzes large files in any format, from PDF and Word to PNG and PPTX.

Using OCR (Optical Character Recognition) technology, the neural network can read scans and photos.

Its functionality also includes creating summaries for documents, accessing the ChatGPT model, answering questions about any uploaded file, and working with information from its own database.

The beta version of Elmento AI already offers you many advantages over other neural networks, and we are striving to make it even better.

Thank you for your interest in Elmento, and we wish you success with your tasks!
""")

st.title("Frequently Asked Questions (FAQ):")

st.markdown("""
1. **How to use the neural network?**
   1) Go to the "My Profile" section and create an account there. Log in to it.
   2) For the neural network to work, you need to enter the API key, which is prominently displayed on each page.
   3) You can upload documents in the "Files" section.
   4) In the "Files" section, you can select a document for processing. You can click the "Get Summary" button to get a summary of the document or "Interact with AI" to ask a question about the file.

2. **When will the full version be released?**
   Elmento AI is currently in the development and testing phase. We expect to complete the main part of the work within a few months.

3. **What are the planned pricing options?**
   Currently, there are no pricing plans. The neural network is available for free during the first month.

4. **I found a bug/error. Where should I report it?**
    ...chat to me - sasha.korovkina2003@gmail.com.
""")
