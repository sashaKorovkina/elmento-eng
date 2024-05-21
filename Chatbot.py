from openai import OpenAI
import streamlit as st

# Display FAQs
st.title("Вас приветствует команда Elmento AI!")

st.markdown("""
Elmento AI - это российская нейросеть, которая анализирует объёмные файлы в любом расширении: от pdf и word до png и pptx. 

С помощью технологии OCR (компьютерного зрения), нейросеть может читать сканы и фотографии. 

В её функционал также входит создание краткого содержания (сводки) к документам, доступ к модели ChatGPT , ответы на вопросы по любому загруженному файлу и работа с информацией из её собственной базы данных. 

Beta-версия Elmento AI уже предлагает вам множество преимуществ перед другими нейросетями, а мы стараемся делать её лучше. 

Благодарим вас за интерес к Elmento и желаем удачи с вашими задачами!

""")

st.title("Часто задаваемые вопросы (FAQ):")

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
