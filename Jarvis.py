import speech_recognition as sr
# import Speech_bot_new as sr1
import bucket_list as bl
import streamlit as st
from dataclasses import dataclass
from typing import Literal
import pyttsx3

recognizer = sr.Recognizer()
inp_name = ""
def speak_bot(txt):
    engine = pyttsx3.init()
    engine.say(txt)
    engine.runAndWait()

# text = "Hey, this is a bot made by PM"
# speak_bot(text)

def user_speech_input():
    with sr.Microphone() as source:
        recognizer.pause_threshold = 2
        recognizer.adjust_for_ambient_noise(source,duration=2)
        # recognizer.non_speaking_duration = 20
        # recognizer.operation_timeout = 8
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
        on_click_callback(text,"")
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
    
def speech_processing(txt,user_name):
    if 'goodbye' or 'bye' or 'stop' or 'quit' in txt:
        speak_bot(f"Goodbye {user_name}!, have a nice day!")
        print(f"Bot: Goodbye {user_name}!, have a nice day!")
        on_click_callback(txt,f"Goodbye {user_name}!, have a nice day!")
        return True
    else:
        print("I couldn't understand your command, Please try again.")
        st.write("I couldn't understand your command, Please try again.")
    return False

def bucket():
    loop = True
    while(loop):
        speak_bot("Do you want to create a list or modify an existing one?")
        print("Bot: Do you want to create a list or modify an existing one?")
        on_click_callback("","Do you want to create a list or modify an existing one?")
        list_text = user_speech_input()
        if 'create' in list_text:
            speak_bot("what would be the name of the list??")
            print("what would be the name of the list??")
            on_click_callback(list_text,"what would be the name of the list??")
            list_name = user_speech_input()
            bl.create_new_list(list_name)
        elif 'existing' in list_text:
            
            if bl.show_list():
                speak_bot("what is the name of the list you want to modify")
                print("what is the name of the list you want to modify")
                on_click_callback(list_text,"what is the name of the list you want to modify")
                name_of_list = user_speech_input()
                bl.display_list(name_of_list)
                speak_bot("Do yo want to add, delete of change any item in this list??")
                print("Do yo want to add, delete of change any item in this list??")
                on_click_callback(name_of_list,"Do yo want to add, delete of change any item in this list??") 
                decision = user_speech_input()
                if 'add' in decision:
                    speak_bot("what item you want to add?")
                    print("what item you want to add?")
                    on_click_callback(decision,"what item you want to add?")
                    item_add = user_speech_input()
                    bl.add_item_to_list(name_of_list,item_add)
                elif 'delete' in decision:
                    speak_bot("which item you want to delete?")
                    print("which item you want to delete?")
                    on_click_callback(decision,"which item you want to delete?")
                    item_del = user_speech_input()
                    bl.remove_item_from_list(name_of_list,item_del)
                elif 'change' in decision:
                    speak_bot("which item you want to change??")
                    print("which item you want to change??")
                    on_click_callback(decision,"which item you want to change??")
                    bl.display_list(name_of_list)
                    item_change_old = user_speech_input()
                    speak_bot(f"what new item you want to replace {item_change_old} with??")
                    print(f"what new item you want to replace {item_change_old} with??")
                    on_click_callback(item_change_old,f"what new item you want to replace {item_change_old} with??")
                    item_change_new = user_speech_input()
                    bl.modify(name_of_list,item_change_old,item_change_new)
            else:
                speak_bot("There is no list present, please create one if you want")
                print("Bot: There is no list present, please create one if you want")
                on_click_callback("","There is no list present, please create one if you want") 
        
        else:
            loop = False
            speak_bot("Thank you for your modifications, please feel free to modify anything at anytime you want")
            print("Thank you for your modifications, please feel free to modify anything at anytime you want")
            on_click_callback(list_text,"Thank you for your modifications, please feel free to modify anything at anytime you want")

def positioning():
    def load_css():
        with open("static/styles.css", "r") as f:
            css = f"<style>{f.read()}</style>"
            st.markdown(css, unsafe_allow_html=True)
    load_css()
    def initialize_session_state():
        if "history" not in st.session_state:
            st.session_state.history = []

    chat_placeholder = st.container()

    initialize_session_state()
    with chat_placeholder:
        for chat in st.session_state.history:
            div = f"""
                <div class="chat-row 
                    {'' if chat.origin == 'ai' else 'row-reverse'}">
                    {'<i class="fa-solid fa-robot"></i>' if chat.origin == 'ai' else '<i class="fa-solid fa-user"></i>'}
                    <div class="chat-bubble
                    {'ai-bubble' if chat.origin == 'ai' else 'human-bubble'}">
                        &#8203;{chat.message}
                    </div>
                </div>
            """
            st.session_state.history = []
            st.markdown(div, unsafe_allow_html=True)

def on_click_callback(human,ai):
    @dataclass
    class Message:
        """Class for keeping track of a chat message."""
        origin: Literal["human", "ai"]
        message: str    
            
    positioning()
    
    ai_response = ai
    if human != "":
        st.session_state.history.append(
            Message("human", human)
        )
    if ai != "":
        st.session_state.history.append(
            Message("ai", ai_response)
        )
        
def talk():
    st.write("My Bot")
    text = user_speech_input()
    initial = False
    if 'jarvis' in text:
        initial = True
    while initial:
        if 'hello' in text:
            speak_bot("Hello!, may I know your name please ?")
            print("Bot: Hello!, may I know your name please ?")
            on_click_callback(text,"Hello!, may I know your name please ?")
            inp_name = user_speech_input()
            speak_bot(f"Hello!, {inp_name.capitalize()}")
            print(f"Bot: Hello! {inp_name.capitalize()}")
            on_click_callback(inp_name,f"Hello!, {inp_name.capitalize()}")
            speak_bot("What do you want to do today? Would you like to the list of places to visit??")
            print("Would you like to modify or create a list of places to visit??")
            on_click_callback("","Would you like to modify or create a list of places to visit??")
            dec = user_speech_input()
            if 'yes' in dec:
                bucket()
            else:
                speak_bot("Okay, anything else that i can do for you?")
                print("Okay, anything else that i can do for you?")
                # text_inp = user_speech_input()
                on_click_callback(dec,"Okay, anything else that i can do for you?")
                what_else = user_speech_input()
                initial = speech_processing(what_else,inp_name)
        else:
            initial = speech_processing(text,inp_name)
            break
        text = user_speech_input()
        
placeholder = st.empty()
chat_container = st.container(height=400)
def run_button():  
    # if chat:
    #     with chat_container:
    #         sr1.talk(chat)
    # else:
    with chat_container:
        talk()
    
with st.container(height=75,border=False):
    c1,c2 = st.columns([0.9,0.1])
    with c1:
        chat = st.chat_input("Message...")
        if chat:
            run_button()
    with c2:
        if st.button("🎙️",type="primary"):
            run_button()
