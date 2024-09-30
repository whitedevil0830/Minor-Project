import streamlit as st

# mic_on = True
# if mic_on:
#     if st.button("🎙️"):
#         st.write("Listening...")
#         if st.button("🔴"):
#             mic_on = False
        
# else:
#     if st.button("🎙️"):
#         if st.button("🔴"):
#             st.write("Listening stopped...")



# import streamlit as st

# # Function to simulate recording
# def simulate_recording():
#     st.write("Recording...")
#     if mic_on:
#         if st.button("🎙️ Recording (Click to stop)"):
#             mic_on = False

# # Main Streamlit app
# def main():
#     st.title("Microphone Icon Button")

#     # Initialize microphone state
#     mic_on = True

#     # Display microphone icon button
#     if mic_on:
#         if st.button("🎙️ Recording (Click to stop)"):
#             mic_on = True
#     else:
#         if st.button("🔴 Mic Off (Click to start recording)"):
#             mic_on = True
#             simulate_recording()

# if __name__ == "__main__":
#     main()



# from streamlit_mic_recorder import mic_recorder




# """Record audio from the microphone."""
# red_square = "🔴"
# # red_square = "\wave_button.ico"
# microphone = "🎙️"
# play_button = "\U000025B6"

# recording = mic_recorder(start_prompt=microphone, stop_prompt=red_square, just_once=True)




# import streamlit as st

# c = st.container(height=700,border=False)
# with c:
#     st.write("this is the main content space....")
#     C = st.container(height=550)
#     c1,c2 = st.columns([0.8,0.2])
#     with c1:
#         st.chat_input("this is the chat box...")
#     with c2:
#         st.button("click me")


# import streamlit as st
# from streamlit_chatbox import *
# import time
# import simplejson as json


# llm = FakeLLM()
# chat_box = ChatBox()


# with st.sidebar:
#     st.subheader('start to chat using streamlit')
#     streaming = st.checkbox('streaming', True)
#     in_expander = st.checkbox('show messages in expander', True)
#     show_history = st.checkbox('show history', False)

#     st.divider()

#     btns = st.container()

    # file = st.file_uploader(
    #     "chat history json",
    #     type=["json"]
    # )

    # if st.button("Load Json") and file:
    #     data = json.load(file)
    #     chat_box.from_dict(data)


# chat_box.init_session()
# chat_box.output_messages()

# if query := st.chat_input('input your question here'):
#     chat_box.user_say(query)
#     if streaming:
#         generator = llm.chat_stream(query)
#         elements = chat_box.ai_say(
#             [
#                 # you can use string for Markdown output if no other parameters provided
#                 Markdown("Listening", in_expander=in_expander,
#                          expanded=True, title="Reply"),
#                 # Markdown("", in_expander=in_expander, title="references"),
#             ]
#         )
#         time.sleep(1)
#         text = ""
#         for x, docs in generator:
#             text += x
#             chat_box.update_msg(text, element_index=0, streaming=True)
#         # update the element without focus
#         chat_box.update_msg(text, element_index=0, streaming=False, state="complete")
#         chat_box.update_msg("\n\n".join(docs), element_index=1, streaming=False, state="complete")
#     else:
#         text, docs = llm.chat(query)
#         chat_box.ai_say(
#             [
#                 Markdown(text, in_expander=in_expander,
#                          expanded=True, title="Reply"),
#                 Markdown("\n\n".join(docs), in_expander=in_expander,title="references"),
#             ]
#         )

# cols = st.columns(2)
# if cols[0].button('show me the multimedia'):
#     chat_box.ai_say(Image(
#         'https://tse4-mm.cn.bing.net/th/id/OIP-C.cy76ifbr2oQPMEs2H82D-QHaEv?w=284&h=181&c=7&r=0&o=5&dpr=1.5&pid=1.7'))
#     time.sleep(0.5)
#     chat_box.ai_say(
#         Video('https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4'))
#     time.sleep(0.5)
#     chat_box.ai_say(
#         Audio('https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4'))

# if cols[1].button('run agent'):
#     chat_box.user_say('run agent')
#     agent = FakeAgent()
#     text = ""

#     # streaming:
#     chat_box.ai_say() # generate a blank placeholder to render messages
#     for d in agent.run_stream():
#         if d["type"] == "complete":
#             chat_box.update_msg(expanded=False, state="complete")
#             chat_box.insert_msg(d["llm_output"])
#             break

#         if d["status"] == 1:
#             chat_box.update_msg(expanded=False, state="complete")
#             text = ""
#             chat_box.insert_msg(Markdown(text, title=d["text"], in_expander=True, expanded=True))
#         elif d["status"] == 2:
#             text += d["llm_output"]
#             chat_box.update_msg(text, streaming=True)
#         else:
#             chat_box.update_msg(text, streaming=False)

# # btns.download_button(
# #     "Export Markdown",
# #     "".join(chat_box.export2md()),
# #     file_name=f"chat_history.md",
# #     mime="text/markdown",
# # )

# # btns.download_button(
# #     "Export Json",
# #     chat_box.to_json(),
# #     file_name="chat_history.json",
# #     mime="text/json",
# # )

# if btns.button("clear history"):
#     chat_box.init_session(clear=True)
#     st.experimental_rerun()


# if show_history:
#     st.write(chat_box.history)




# import streamlit as st

# placeholder = st.empty()

# # Replace the placeholder with some text:
# placeholder.text("Hello")

# # Replace the text with a chart:
# # placeholder.line_chart({"data": [1, 5, 2, 6]})

# code = '''def hello():
#     print("Hello, Streamlit!")'''
# placeholder.code(code, language='python')

# placeholder.

# Replace the chart with several elements:
# with placeholder.container():
#     st.write("This is one element")
#     st.write("This is another")

# Clear all those elements:
# placeholder.empty()









import streamlit as st
# import sr_new as se
from streamlit_chat import message

def main():
    message("This is a chat bot.",is_user=False)
    message("hii this is the user",is_user=True)
    
    message.position = "down"

if __name__ == "__main__":
    with st.container(height=300):
        # with st.container(height=70):
        st.button("mic",type="primary",on_click=main())
            

        