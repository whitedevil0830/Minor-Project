
# import streamlit as st
# from streamlit_chat import message

# st.title("Welcome to my page 2")

# if 'generated' not in st.session_state:
#     st.session_state['generated'] = ["I'm you cenversational agent, what can we talk about today"]

# if 'past' not in st.session_state:
#     st.session_state['past'] = ['Hi']
# def on_callback():
#     human_prompt = st.session_state.human_prompt
#     st.session_state.past.append(human_prompt)


# response_container = st.container()
# input_container = st.container()

# with response_container:
#     for chat in st.session_state.history:
#         st.markdown(chat)
# #User input

# # Function for taking user-provided prompt as input

# def get_text():
#     input_text = st.text_input("You: ", "", key="input")
#     return input_text

# # ## Applying the user input box

# with response_container:
#     if st.session_state['generated']:
#          for i in range(len(st.session_state['generated'])):
#                message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
#                message(st.session_state['generated'][i], key=str(i))

# with input_container:
#      user_input = st.chat_input("Chat here...")
#      if user_input:
#           response = "You are welcome"
#           st.session_state.past.append(user_input)
#           st.session_state.generated.append(response)








# import streamlit as st
# import ollama

# st.title("💬 llama2 (7B) Chatbot")

# if "messages" not in st.session_state:
#     st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# ### Write Message History
# for msg in st.session_state.messages:
#     if msg["role"] == "user":
#         st.chat_message(msg["role"], avatar="🧑‍💻").write(msg["content"])
#     else:
#         st.chat_message(msg["role"], avatar="🤖").write(msg["content"])

# ## Generator for Streaming Tokens
# def generate_response():
#     response = ollama.chat(model='llama2', stream=True, messages=st.session_state.messages)
#     for partial_resp in response:
#         token = partial_resp["message"]["content"]
#         st.session_state["full_message"] += token
#         yield token

# if prompt := st.chat_input():
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     st.chat_message("user", avatar="🧑‍💻").write(prompt)
#     st.session_state["full_message"] = ""
#     st.chat_message("assistant", avatar="🤖").write_stream(generate_response)
#     st.session_state.messages.append({"role": "assistant", "content": st.session_state["full_message"]})   
    



# from dataclasses import dataclass
# from typing import Literal
# import streamlit as st

# from langchain import OpenAI
# from langchain.callbacks import get_openai_callback
# from langchain.chains import ConversationChain
# from langchain.chains.conversation.memory import ConversationSummaryMemory
# import streamlit.components.v1 as components

# @dataclass
# class Message:
#     """Class for keeping track of a chat message."""
#     origin: Literal["human", "ai"]
#     message: str

# def load_css():
#     with open("static/styles.css", "r") as f:
#         css = f"<style>{f.read()}</style>"
#         st.markdown(css, unsafe_allow_html=True)

# def initialize_session_state():
#     if "history" not in st.session_state:
#         st.session_state.history = []
#     if "token_count" not in st.session_state:
#         st.session_state.token_count = 0
#     if "conversation" not in st.session_state:
#         llm = OpenAI(
#             temperature=0,
#             openai_api_key=st.secrets["openai_api_key"],
#             model_name="text-davinci-003"
#         )
#         st.session_state.conversation = ConversationChain(
#             llm=llm,
#             memory=ConversationSummaryMemory(llm=llm),
#         )

# def on_click_callback():
#     with get_openai_callback() as cb:
#         human_prompt = st.session_state.human_prompt
#         llm_response = st.session_state.conversation.run(
#             human_prompt
#         )
#         st.session_state.history.append(
#             Message("human", human_prompt)
#         )
#         st.session_state.history.append(
#             Message("ai", llm_response)
#         )
#         st.session_state.token_count += cb.total_tokens

# load_css()
# initialize_session_state()

# st.title("Hello Custom CSS Chatbot 🤖")

# chat_placeholder = st.container()
# prompt_placeholder = st.form("chat-form")
# credit_card_placeholder = st.empty()

# with chat_placeholder:
#     for chat in st.session_state.history:
#         div = f"""
# <div class="chat-row 
#     {'' if chat.origin == 'ai' else 'row-reverse'}">
#     <img class="chat-icon" src="app/static/{
#         'ai_icon.png' if chat.origin == 'ai' 
#                       else 'user_icon.png'}"
#          width=32 height=32>
#     <div class="chat-bubble
#     {'ai-bubble' if chat.origin == 'ai' else 'human-bubble'}">
#         &#8203;{chat.message}
#     </div>
# </div>
#         """
#         st.markdown(div, unsafe_allow_html=True)
    
#     for _ in range(3):
#         st.markdown("")

# with prompt_placeholder:
#     st.markdown("**Chat**")
#     cols = st.columns((6, 1))
#     cols[0].text_input(
#         "Chat",
#         value="Hello bot",
#         label_visibility="collapsed",
#         key="human_prompt",
#     )
#     cols[1].form_submit_button(
#         "Submit", 
#         type="primary", 
#         on_click=on_click_callback, 
#     )

# credit_card_placeholder.caption(f"""
# Used {st.session_state.token_count} tokens \n
# Debug Langchain conversation: 
# {st.session_state.conversation.memory.buffer}
# """)

# components.html("""
# <script>
# const streamlitDoc = window.parent.document;

# const buttons = Array.from(
#     streamlitDoc.querySelectorAll('.stButton > button')
# );
# const submitButton = buttons.find(
#     el => el.innerText === 'Submit'
# );

# streamlitDoc.addEventListener('keydown', function(e) {
#     switch (e.key) {
#         case 'Enter':
#             submitButton.click();
#             break;
#     }
# });
# </script>
# """, 
#     height=0,
#     width=0,
# )


















# import streamlit as st
# from streamlit_chat import message
# from streamlit_extras.colored_header import colored_header
# from streamlit_extras.add_vertical_space import add_vertical_space
# from hugchat import hugchat
# from hugchat.login import Login

# # Log in to huggingface and grant authorization to huggingchat
# EMAIL = "abpmishra08@gmail.com"
# PASSWD = "your password"
# cookie_path_dir = "./cookies/" # NOTE: trailing slash (/) is required to avoid errors
# sign = Login(EMAIL, PASSWD)
# cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)

# # Create your ChatBot
# chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"


# if 'generated' not in st.session_state:
#     st.session_state['generated'] = ["I'm HugChat, How may I help you?"]

# if 'past' not in st.session_state:
#     st.session_state['past'] = ['Hi!']
    
# input_container = st.container()
# colored_header(label='', description='', color_name='blue-30')
# response_container = st.container()


# # User input
# ## Function for taking user provided prompt as input
# def get_text():
#     input_text = st.text_input("You: ", "", key="input")
#     return input_text

# ## Applying the user input box
# with input_container:
#     user_input = get_text()
    
# # Response output
# ## Function for taking user prompt as input followed by producing AI generated responses
# def generate_response(prompt):
#     chatbot = hugchat.ChatBot()
#     response = chatbot.chat(prompt)
#     return response

# ## Conditional display of AI generated responses as a function of user provided prompts
# with response_container:
#     if user_input:
#         response = generate_response(user_input)
#         st.session_state.past.append(user_input)
#         st.session_state.generated.append(response)
        
#     if st.session_state['generated']:
#         for i in range(len(st.session_state['generated'])):
#             message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
#             message(st.session_state["generated"][i], key=str(i))

# import streamlit as st

# def initialize_session_state():
#     if "history" not in st.session_state:
#         st.session_state.history = []
#     # if 'human_prompt' not in st.session_state:
#     #     st.session_state.human_prompt = []


# def on_click_callback():
#     human_prompt = st.session_state.human_prompt
#     st.session_state.history.append(human_prompt)
    
# initialize_session_state()

# st.markdown("My Bot")

# chat_placeholder = st.container(height=400)
# prompt_placeholder = st.container()

# with chat_placeholder:
#     for chat in st.session_state.history:
#         st.markdown(chat)

# for _ in range(3):
#     st.markdown("")

# with prompt_placeholder:
    
#     cols = st.columns([6,1])
#     cols[0].chat_input(
#         # "Chat",
#         # value="Hello Bot",
#         key="human_prompt",
#         # label_visibility= "collapsed",
#         on_submit=on_click_callback
#     )
#     # cols[1].form_submit_button(
#     #     "Submit",
#     #     type="primary",
#     #     on_click=on_click_callback
#     # )
    
    
    
    
    
    
    
    
    
import streamlit as st
from dataclasses import dataclass
from typing import Literal

@dataclass
class Message:
    """Class for keeping track of a chat message."""
    origin: Literal["human", "ai"]
    message: str

def load_css():
    with open("static/styles.css", "r") as f:
        css = f"<style>{f.read()}</style>"
        st.markdown(css, unsafe_allow_html=True)

load_css()

def initialize_session_state():
    if "history" not in st.session_state:
        st.session_state.history = []
    # if "human_prompt" not in st.session_state:
    #     st.session_state.human_prompt = "Hii"

def on_click_callback(human,ai):
    # with get_openai_callback() as cb:
    # human_prompt = st.session_state.human_prompt
    # llm_response = st.session_state.conversation.run(
    #     human_prompt
    # )
    # if human == "hii":
    #     ai = "hello this is jarvis"
    # if human == "how are you":
    #     ai = "I am fine, thank you for your concern"
    initialize_session_state()
    
    chat_placeholder = st.container()
    # prompt_placeholder = st.container()

    with chat_placeholder:
        for chat in st.session_state.history:
            div = f"""
                <div class="chat-row 
                    {'' if chat.origin == 'ai' else 'row-reverse'}">
                    <img class="chat-icon" src=static/"{
                        'ai_icon.png' if chat.origin == 'ai'
                                    else 'user_icon.png'}"
                        width=32 height=32>
                    <div class="chat-bubble
                    {'ai-bubble' if chat.origin == 'ai' else 'human-bubble'}">
                        &#8203;{chat.message}
                    </div>
                </div>
            """
            st.markdown(div, unsafe_allow_html=True)
    ai_response = ai
    st.session_state.history.append(
        Message("human", human)
    )
    st.session_state.history.append(
        Message("ai", ai_response)
    )

initialize_session_state()
# chat_placeholder = st.container()
# prompt_placeholder = st.container()

# with chat_placeholder:
#     for chat in st.session_state.history:
#         div = f"""
#             <div class="chat-row 
#                 {'' if chat.origin == 'ai' else 'row-reverse'}">
#                 <img class="chat-icon" src=static/"{
#                     'ai_icon.png' if chat.origin == 'ai'
#                                 else 'user_icon.png'}"
#                     width=32 height=32>
#                 <div class="chat-bubble
#                 {'ai-bubble' if chat.origin == 'ai' else 'human-bubble'}">
#                     &#8203;{chat.message}
#                 </div>
#             </div>
#         """
#         st.markdown(div, unsafe_allow_html=True)

# human = "how are you"


# st.page_link("pages/world_map.py")
# st.divider()

# st.link_button("world_map",url="")

# with prompt_placeholder:

#     st.markdown("**Chat**")
#     cols = st.columns((6, 1))
    
#     with cols[0]:
#         if human == "hii":
#             ai = "hello this is jarvis"
#         if human == "how are you":
#             ai = "I am fine, thank you for your concern"      
#         human = st.chat_input("Chat here...", key="human_prompt", on_submit=on_click_callback(ai,human))
        # "Chat",
        # value="Hello bot",
        # label_visibility="collapsed",
    # cols[1].button(
    #     "Mic",   
    #     type="primary", 
    #     on_click=on_click_callback, 
    # )