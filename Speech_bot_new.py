# import streamlit as st

# # Initialize empty chat history
# chat_history = []

# # Function to simulate agent response (replace with your logic)
# def get_agent_response(user_input):
#   # Example logic: Mimic user input for simplicity
#   return f"Agent: {user_input}"

# def main():
#   # Sidebar layout
#   with st.sidebar:
#     st.header("Options")
#     # Dropdown button (not functional without external libraries)
#     # st.selectbox("Select...", ["Option 1", "Option 2"])
#     st.button("Clear History", key="clear_history")
#     st.button("Submit", key="submit")

#   # Chat history area
#   st.header("Chat History")
#   chat_box = st.empty()

#   # Microphone state (initially off)
#   mic_on = False
#   user_input = st.text_input("", key="user_input", disabled=mic_on)

#   # Text input or microphone toggle
#   if st.button("", key="mic_toggle"):
#     mic_on = not mic_on
#     user_input = st.text_input("", key="user_input", disabled=mic_on)

#   # Process user input
#   if (st.button("Send", key="send") or mic_on) and user_input:
#     chat_history.append({"user": user_input, "agent": ""})
#     chat_box.text("\n".join([msg["user"] for msg in chat_history]))

#     # Simulate agent response (replace with your logic)
#     agent_response = get_agent_response(user_input)
#     chat_history.append({"user": "", "agent": agent_response})
#     chat_box.text("\n".join([msg["user"] + "\n" + msg["agent"] for msg in chat_history]))

#     # Clear user input for next interaction
#     user_input = ""

#   # Clear chat history on button click
#   if st.sidebar.button("Clear History", key="clear_history"):
#     chat_history.clear()
#     chat_box.text("")

# if __name__ == "__main__":
#   main()


import speech_recognition as sr
# import streamlit.components.v1 as comp
from streamlit_chat import message
# from streamlit_mic_recorder import mic_recorder
import bucket_list as bl
# import os
import streamlit as st
# from dataclasses import dataclass
# from typing import Literal
import pyttsx3
# import pywhatkit
# import googlemaps
# import requests
# from requests.structures import CaseInsensitiveDict
# import module_1_prediction
# st.set_page_config(
#     layout='wide'
# )    
recognizer = sr.Recognizer()
inp_name = ""
def speak_bot(txt):
    engine = pyttsx3.init()
    engine.say(txt)
    engine.runAndWait()

text = "Hey, this is a bot made by PM"
speak_bot(text)

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
        # print(f"You said: {text}")
        # st.write(f"You said: {text}")
        message(text,is_user=True)
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
        # speak_bot(f"Goodbye {user_name}!, have a nice day!")
        print(f"Bot: Goodbye {user_name}!, have a nice day!")
        message(txt,is_user=True)
        message(f"Goodbye {user_name}!, have a nice day!",is_user=False)
        return True
    else:
        print("I couldn't understand your command, Please try again.")
        st.write("I couldn't understand your command, Please try again.")
    return False

def bucket():
    loop = True
    while(loop):
    # if loop:
        # speak_bot("Do you want to create a list or modify an existing one?")
        print("Bot: Do you want to create a list or modify an existing one?")
        # st.write("Bot: Do you want to create a list or modify an existing one?")
        message("Do you want to create a list or modify an existing one?",is_user=False)
        list_text = user_speech_input()
        if 'new' in list_text:
            # speak_bot("what would be the name of the list??")
            print("what would be the name of the list??")
            # st.write("what would be the name of the list??")
            message(list_text,is_user=True)
            message("what would be the name of the list??",is_user=False)
            list_name = user_speech_input()
            bl.create_new_list(list_name)
            # speak_bot("Bot: Try giving another name of the list")
            # message()
        elif 'existing' in list_text:
            
            if bl.show_list():
                # while True:
                # speak_bot("what is the name of the list you want to modify")
                print("what is the name of the list you want to modify")
                # st.write("what is the name of the list you want to modify")
                message(list_text,is_user=True,)
                message("what is the name of the list you want to modify",is_user=False)
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
                # speak_bot("Do yo want to add, delete of change any item in this list??")
                print("Do yo want to add, delete of change any item in this list??")
                # st.write("Do yo want to add, delete of change any item in this list??") 
                message(name_of_list,is_user=True)
                message("Do yo want to add, delete of change any item in this list??",is_user=False)
                decision = user_speech_input()
                if 'add' in decision:
                    # speak_bot("what item you want to add?")
                    print("what item you want to add?")
                    # st.write("what item you want to add?")
                    message(decision,is_user=True)
                    message("what item you want to add?",is_user=False)
                    item_add = user_speech_input()
                    bl.add_item_to_list(name_of_list,item_add)
                elif 'delete' or 'remove' in decision:
                    # speak_bot("which item you want to delete?")
                    print("which item you want to delete?")
                    # st.write("which item you want to delete?")

                    message(decision,is_user=True)
                    message("what item you want to delete?",is_user=False)
                    item_del = user_speech_input()
                    bl.remove_item_from_list(name_of_list,item_del)
                elif 'change' in decision:
                    # speak_bot("which item you want to change??")
                    print("which item you want to change??")
                    # st.write("which item you want to change??")
                    message(decision,is_user=True)
                    message("what item you want to change?",is_user=False)
                    bl.display_list(name_of_list)
                    item_change_old = user_speech_input()
                    # speak_bot(f"what new item you want to replace {item_change_old} with??")
                    print(f"what new item you want to replace {item_change_old} with??")
                    # st.write(f"what new item you want to replace {item_change_old} with??")
                    message(item_change_old,is_user=True)
                    message(f"what new item you want to replace {item_change_old} with??",is_user=False)
                    item_change_new = user_speech_input()
                    bl.modify(name_of_list,item_change_old,item_change_new)
            else:
                # speak_bot("There is no list present, please create one if you want")
                print("Bot: There is no list present, please create one if you want")
                # st.write("Bot: There is no list present, please create one if you want")
                message("There is no list present, please create one if you want",is_user=False) 
        
        else:
            loop = False
            # speak_bot("Thank you for your modifications, please feel free to modify anything at anytime you want")
            print("Thank you for your modifications, please feel free to modify anything at anytime you want")
            # st.write("Bot: Thank you for your modifications, please feel free to modify anything at anytime you want")
            message(list_text,is_user=True)
            message("Thank you for your modifications, please feel free to modify anything at anytime you want",is_user=False)
        
def talk(text):
    st.write("My Bot")
    # if mic_button(microphone,red_square):
    # speak_bot("Hey there!")
    # text = user_speech_input()
    initial = False
    if 'jarvis' in text:
        initial = True
    while initial:
        if 'hello' or 'hii' or 'hey' in text:
            # speak_bot("Hello!, may I know your name please ?")
            print("Bot: Hello!, may I know your name please ?")
            message(text,is_user=True)
            message("Hello!, may I know your name please ?",is_user=False)
            name = st.chat_input("")
            
            inp_name = name
            # speak_bot(f"Hello!, {inp_name.capitalize()}")
            print(f"Bot: Hello! {inp_name.capitalize()}")    
            message(inp_name,is_user=True)
            message(f"Hello!, {inp_name.capitalize()}",is_user=False)
            # speak_bot("What do you want to do today? Would you like to the list of places to visit??")
            print("Would you like to modify or create a list of places to visit??")
            message("Would you like to modify or create a list of places to visit??",is_user=False)
            dec = user_speech_input()
            if 'yes' in dec:
                bucket()
            else:
                # speak_bot("Okay, anything else that i can do for you?")
                print("Okay, anything else that i can do for you?")
                message(dec,is_user=True)
                message("Okay, anything else that i can do for you?",is_user=False)
                continue            
        else:
            initial = speech_processing(text,inp_name)
            break
        text = user_speech_input()

# placeholder = st.empty()
# chat_container = st.container(height=300)
# def run_button():    
#     with chat_container:
#         placeholder.button("",type="secondary")
#         placeholder.empty()
#         placeholder.write(talk())
    

# with st.container(height=70):
#     if st.button("🎙️",type="primary"):
#         run_button()