import speech_recognition as sr
import streamlit.components.v1 as comp
# from streamlit_mic_recorder import mic_recorder
import bucket_list as bl
import os
import streamlit as st
from dataclasses import dataclass
from typing import Literal
import pyttsx3
import googlemaps
import requests
from requests.structures import CaseInsensitiveDict
# import module_1_prediction
st.set_page_config(
    layout='wide'
)
recognizer = sr.Recognizer()
inp_name = ""
def speak_bot(txt):
    engine = pyttsx3.init()
    engine.say(txt)
    engine.runAndWait()

text = "Hey, this is a bot made by PM"
speak_bot(text)

# def places(text):
#     pl

def user_speech_input():
    with sr.Microphone() as source:
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source,duration=2)
        # recognizer.non_speaking_duration = 0.5
        # recognizer.operation_timeout = 0.5
        print("\nListening.....")
        st.write("\nListening.....")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...\n")
        st.write("Recognizing...\n")
        # input = recognizer.recognize_google(audio,language="en-US")
        text = recognizer.recognize_google(audio,language='en-US')
        # text =  recognizer.
        text = text.lower()
        # text = input.lower()
        print(f"You said: {text}")
        # st.write(f"You said: {text}")
        positioning(f"You said: {text}","")
    except KeyboardInterrupt:
        print("A Keyboard interrupt encountered, so signing off!")
        st.write("A Keyboard interrupt encountered, so signing off!")
        exit(0)
    except sr.RequestError as re:
        print("Error: (0)",format(re))
        st.write("Error: (0)",format(re))
        text = ""
    except sr.UnknownValueError:
        print("Sorry, I couldn't get your input...\n\n")
        st.write("Sorry, I couldn't get your input...\n\n")
        pass
    return text

# def play_video(title):
    # pywhatkit.playonyt(title)
    
def speech_processing(txt,user_name):
    if 'goodbye' or 'bye' or 'stop' or 'quit' in txt:
        speak_bot(f"Goodbye {user_name}!, have a nice day!")
        print(f"Bot: Goodbye {user_name}!, have a nice day!")
        # st.write(f"Bot: Goodbye {user_name}!, have a nice day!")
        positioning(txt,f"Goodbye {user_name}!, have a nice day!")
        return True
    else:
        print("I couldn't understand your command, Please try again.")
        st.write("I couldn't understand your command, Please try again.")
    return False


# red_square = "🔴"
# microphone = "🎙️"
# play_button = "\U000025B6"
# def mic_button(microphone,red_square):
#     button = st.button("Click me", icon=microphone)
#     # If the button is clicked, change the icon
#     if button:
#         button.icon = red_square

def bucket():
    loop = True
    while(loop):
    # if loop:
        speak_bot("Do you want to create a list or modify an existing one?")
        print("Bot: Do you want to create a list or modify an existing one?")
        # st.write("Bot: Do you want to create a list or modify an existing one?")
        positioning("","Do you want to create a list or modify an existing one?")
        list_text = user_speech_input()
        if 'new' in list_text:
            speak_bot("what would be the name of the list??")
            print("what would be the name of the list??")
            # st.write("what would be the name of the list??")
            positioning(list_text,"what would be the name of the list??")
            list_name = user_speech_input()
            bl.create_new_list(list_name)
            speak_bot("Bot: Try giving another name of the list")
            
        elif 'existing' in list_text:
            
            if bl.show_list():
                # while True:
                speak_bot("what is the name of the list you want to modify?")
                print("what is the name of the list you want to modify?")
                # st.write("what is the name of the list you want to modify")
                positioning(list_text,"what is the name of the list you want to modify?")
                name_of_list = user_speech_input()
                bl.display_list(name_of_list)
                    # if not dec_res:
                    # speak_bot("Did I get you wrong??\n(Yes/No)")
                    # print("Did I get you wrong??\n(Yes/No)")
                    # st.write("Did I get you wrong??\n(Yes/No)")
                        # wrong_inp = user_speech_input()
                        # if wrong_inp == "no":
                        #     break
                        # else:
                        #     continue
                speak_bot("Do yo want to add, delete of change any item in this list?")
                print("Do yo want to add, delete of change any item in this list?")
                # st.write("Do yo want to add, delete of change any item in this list??")
                positioning(list_text,"Do yo want to add, delete of change any item in this list?")  
                decision = user_speech_input()
                if 'add' in decision:
                    speak_bot("what item you want to add?")
                    print("what item you want to add?")
                    # st.write("what item you want to add?")
                    positioning(decision,"what item you want to add?")
                    item_add = user_speech_input()
                    bl.add_item_to_list(name_of_list,item_add)
                elif 'delete' in decision:
                    speak_bot("which item you want to delete?")
                    print("which item you want to delete?")
                    # st.write("which item you want to delete?")
                    positioning(decision,"what item you want to delete?")
                    item_del = user_speech_input()
                    bl.remove_item_from_list(name_of_list,item_del)
                elif 'change' in decision:
                    speak_bot("which item you want to change?")
                    print("which item you want to change?")
                    # st.write("which item you want to change??")
                    positioning(decision,"what item you want to change?")
                    bl.display_list(name_of_list)
                    item_change_old = user_speech_input()
                    speak_bot(f"what new item you want to replace {item_change_old} with??")
                    print(f"what new item you want to replace {item_change_old} with??")
                    st.write(f"what new item you want to replace {item_change_old} with??")
                    item_change_new = user_speech_input()
                    bl.modify(name_of_list,item_change_old,item_change_new)
            else:
                speak_bot("There is no list present, please create one if you want")
                print("Bot: There is no list present, please create one if you want")
                st.write("Bot: There is no list present, please create one if you want") 
        
        else:
            loop = False
            speak_bot("Thank you for your modifications, please feel free to modify anything at anytime you want")
            print("Thank you for your modifications, please feel free to modify anything at anytime you want")
            st.write("Bot: Thank you for your modifications, please feel free to modify anything at anytime you want")

def talk():
    st.write("My Bot")
    # if mic_button(microphone,red_square):
    # speak_bot("Hey there!")
    text = user_speech_input()
    initial = False
    if 'jarvis' in text:
        initial = True
    while initial:
        # if  'play' in text:
        #     speak_bot("what do you want to play?")
        #     print("what do you want to play?")
        #     title_inp = user_speech_input()
        #     play_video(title_inp)
        #     recognizer.pause_threshold = 10
        # speak_bot("Hello!, how may I help you ??")
        # text = user_speech_input()
        if 'hello' in text:
            speak_bot("Hello!, may I know your name please ?")
            print("Bot: Hello!, may I know your name please ?")
            st.write("Bot: Hello!, may I know your name please ?")
            inp_name = user_speech_input()
            speak_bot(f"Hello!, {inp_name.capitalize()}")
            print(f"Bot: Hello! {inp_name.capitalize()}")
            st.write(f"Bot: Hello! {inp_name.capitalize()}")
            speak_bot("What do you want to do today? Would you like to the list of places to visit??")
            print("Would you like to modify or create a list of places to visit??")
            st.write("Would you like to modify or create a list of places to visit??")
            dec = user_speech_input()
            if 'yes' in dec:
                bucket()
            else:
                speak_bot("Okay, anything else that i can do for you?")
                print("Okay, anything else that i can do for you?")
                st.write("Bot:Okay, anything else that i can do for you?")
                continue            
        # elif 'explore' or 'go' or 'enjoy' or 'weekend' in text:
        #     speak_bot("okay, please provide me your preferences based on the following list of touirst spot types")
        #     print("Cultural\nAdventure\nMedical\nBusiness\nCulinary(food and drink)\nEcotourism(ecology and tourism)\nHistorical\nReligious\nBeach\nWildlife\nInternational\nAgritourism - agriculture, tourism")
        # elif 'place' and 'find' in text:
        #     speak_bot("name the place you want to search...")
        #     print("Bot: Name the place you want to search...")
        #     place_inp = user_speech_input()
        #     places(place_inp)
        else:
            initial = speech_processing(text,inp_name)
            break
        text = user_speech_input()

def positioning(human,ai):
    @dataclass
    class Message:
        """Class for keeping track of a chat message."""
        origin: Literal["human", "ai"]
        message: str

    def load_css():
        with open("static/styles.css", "r") as f:
            css = f"<style>{f.read()}</style>"
            st.markdown(css, unsafe_allow_html=True)

    def initialize_session_state():
        if "history" not in st.session_state:
            st.session_state.history = []
        # if "human_prompt" not in st.session_state:
        #     st.session_state.human_prompt = "Hii"

    def on_click_callback(ai, human):
        # with get_openai_callback() as cb:
        # human_prompt = st.session_state.human_prompt
        # llm_response = st.session_state.conversation.run(
        #     human_prompt
        # )
        # if human == "hii":
        #     ai = "hello this is jarvis"
        # if human == "how are you":
        #     ai = "I am fine, thank you for your concern"
        ai_response = ai
        st.session_state.history.append(
            Message("human", human)
        )
        st.session_state.history.append(
            Message("ai", ai_response)
        )

    initialize_session_state()

    chat_placeholder = st.container()
    prompt_placeholder = st.container()

    with chat_placeholder:
        for chat in st.session_state.history:
            div = f"""
                <div class="chat-row 
                    {'' if chat.origin == 'ai' else 'row-reverse'}">
                    <img class="chat-icon" src="static/{
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

    human = "how are you"


    with prompt_placeholder:

        st.markdown("**Chat**")
        cols = st.columns((6, 1))
        
        with cols[0]:
            # if human == "hii":
            #     ai = "hello this is jarvis"
            # if human == "how are you":
            #     ai = "I am fine, thank you for your concern"      
            human = st.chat_input("Chat here...", key="human_prompt", on_submit=on_click_callback(ai,human))
            # "Chat",
            # value="Hello bot",
            # label_visibility="collapsed",
        # cols[1].button(
        #     "Mic",   
        #     type="primary", 
        #     on_click=on_click_callback, 
        # )
# c1, c2 = st.columns([5, 1],gap='medium')
# with c1:
#     if st.chat_input("Chat here..."):
#         talk()
# with c2:
#     click = st.button(label='🎙️')
#     if click:
#         talk()
# click = st.button(label='🎙️')
# if click:
#     talk()
# elif st.chat_input("Chat here..."):
#     talk()

# c = st.container(height=320)
# with c:
#     st.write("this is the main content space....")
#     C = st.container(height=500)

#     c1,c2 = st.columns([0.8,0.2])
#     with c1:
#         res = st.chat_input("chat here...")
#         if res:
#             talk()
#             # st.write(res)
#     with c2:
#         click = st.button("🎙️")
#         if click:
#             talk()
        #     comp.html(
        # '''
        # <html lang="en">

        # <head>
        #     <meta charset="UTF-8">
        #     <meta name="viewport" content="width=device-width, initial-scale=1.0">
        #     <title>Chat Box</title>
        #     <link rel="stylesheet" href="1.css">
        # </head>

        # <body>

        #     <div class="chat-box">
        #         <div class="messages">
        #         </div>
        #         <div class="input-area">
        #             <input type="text" placeholder="Type your message...">
        #             <button><img src="C:/Users/KIIT/OneDrive/Desktop/codes set/MY CODES/MINOR PROJECT/mic.png" alt="Microphone"></button>
        #         </div>
        #     </div>
        #     <style>
        #         body {
        #             margin: 0;
        #             padding: 0;
        #             font-family: Arial, sans-serif;
        #         }

        #         .chat-box {
        #             left: 70px;
        #             position: fixed;
        #             bottom: 20px;
        #             width: 90%;
        #             background-color: grey;
        #             border-top: 1px solid #ccc;
        #             border-radius: 8px;
        #             overflow: hidden;
        #         }

        #         .messages {
        #             height: 200px;
        #             overflow-y: auto;
        #             padding: 10px;
        #         }

        #         .input-area {
        #             display: flex;
        #             padding: 25px;
        #         }

        #         input {
        #             flex: 1;
        #             padding: 20px;
        #             font-size: large;
        #             border: 3px solid #ccc;
        #             border-radius: 10px 0 0 10px;
        #         }

        #         button {
        #             padding: 10px 23px;
        #             background-color: lightblue;
        #             border: none;
        #             color: white;
        #             border-radius: 5px;

        #         }

        #         button:hover {
        #             background-color: deepskyblue;
        #             cursor: pointer;

        #         }

        #         button img {
        #             width: 25px;
        #             height: 25px;
        #         }
        #     </style>
        # </body>

        # </html>
        #     '''
        # )



# st.write("this is the main content space....")
# C = st.container(height=300)
# st.markdown('''
#             <style>
#             body {      
#             overflow-y: hidden; 
#             overflow-x: hidden; 
#             }
#             </style>
#             ''', unsafe_allow_html=True)
# css = '''
# <style>
# section.main > div:has(~ footer ) {
#     padding-bottom: 5px;
# }
# </style>
# '''
# st.markdown(css, unsafe_allow_html=True)



# c1,c2 = st.columns([0.8,0.2])
# with c1:
#     res = st.chat_input("chat here...")
#     if res:
#         talk()
#         # st.write(res)
# with c2:
#     click = st.button("🎙️")
#     if click:
#         talk()
# talk()
# st.markdown("This is **bold** text.", unsafe_allow_html=True)
# with open("styles.css") as f:
#     css = f.read()
#     st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)




# c1,c2 = st.columns([0.8,0.2])
# with c1:
#     res = st.chat_input("chat here...")
#     if res:
#         talk()
#         # st.write(res)
# with c2:
#     click = st.button("🎙️")