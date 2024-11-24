from openai import OpenAI
import streamlit as st

st.title("MyBotGPT")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Whatz UP?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})



# import streamlit as st
# import random
# import time

# # Streamed response emulator
# def response_generator():
#     response = random.choice(
#         [
#             "Hello there! How can I assist you today?",
#             "Hi, Human! Is there anything I can help you with?",
#             "Do you need help?"
#         ]
#     )
#     for word in response.split():
#         yield word + " "
#         time.sleep(0.05)
    
# st.title("Simple Chat")

# #Initialize chat history
# if "message" not in st.session_state:
#     st.session_state.message = []

# #Display chat messages from history on app rerun
# for message in st.session_state.message:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# #Accept user input
# if prompt := st.chat_input("Whatz Up?"):
#     #add user message to chat history
#     st.session_state.message.append({"role": "user", "content": prompt})
#     #Display user message in chat message container
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     #Display assistan response in chat message container
#     with st.chat_message("assistant"):
#         response = st.write_stream(response_generator())
#     #Add assistant response to chat history
#     st.session_state.message.append({"role": "assistant", "content": response})



#part1
# with st.chat_message("User"):
#     st.write("Heyllooo!!")
#part2
# prompt = st.chat_input("Say something...")
# if prompt:
#     st.write(f"User has sent the following prompt:{prompt}")
#part3

# st.title("Echo Bot")

# #Initialize chat history
# if "message" not in st.session_state:
#     st.session_state.message = []

# #Display chat messages from history on app rerun
# for message in st.session_state.message:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# #React to user input
# if prompt := st.chat_input("What is up?"):
#     #Display user message in chat message container
#     st.chat_message("user").markdown(prompt)
#     #Add user message to chat history
#     st.session_state.message.append({"role": "user", "content": prompt})

#     response = f"Echo: {prompt}"
#     #Display assistant response in chat message container
#     with st.chat_message("assistant"):
#         st.markdown(response)
#     #Add assistant response t chat history
#     st.session_state.message.append({"role": "assistant", "content": response})