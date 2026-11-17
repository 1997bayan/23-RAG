import streamlit as st 
import ollama 

st.set_page_config(
    page_title = "LangChain local chatbot",
    page_icon="🤖",
    layout ="wide"
)

# question = st.text_input("Ask a question about the PDF:")


# if st.button("ASK"):
#     with st.spinner("Generating answer ..."):
        
#         response = ollama.chat(
#             model = 'llama3',
#             messages = [{
#                 'role': 'user',
#                 'content': question
#             }]
#         )

#         st.subheader("Answer")
#         st.write(response['message']['content'])

st.title("lOCAL CHATBOT --> llAMA")
#SESSION FOR CHATBOT : STATE AND KEEP MESSAGES IN STATE


#chat_memory

if "messages" not in st.session_state:
    st.session_state.messages = []

#display old MSG

for msg in st.session_state.messages :
    with st.chat_message(msg['role']):
        st.write(msg["content"])


question = st.chat_input("Ask a question about the PDF:")


if question:
    st.session_state.messages.append(
        {
            "role":"user",
            "content":question
        }
    )

    with st.chat_message("user"):
        st.write(question)


    stream = ollama.chat(
        
            model = 'llama3',
            messages= st.session_state.messages,
            stream=True
            

        
    )

    #show answer
    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""
        for chunk in stream:
            token =chunk ['message']['content']
            full_response += token

            placeholder.markdown(full_response)



    st.session_state.messages.append({
        "role": "assistant",
        "content" : full_response 
    })
