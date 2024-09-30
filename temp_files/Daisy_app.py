import streamlit as st
import streamlit.components.v1 as components
# # import speech_engine as se



st.write("My Bot")
red_square = "\U0001F7E5"
microphone = "🎙️"
play_button = "\U000025B6"
# def mic_button(microphone,red_square):
#     st.button(microphone, on_click=change_icon)
#     # If the button is clicked, change the icon
#     # if button:
#     #     button.icon = red_square

#     # if mic_recorder(start_prompt=microphone, stop_prompt=red_square, just_once=False):
#         # se.talk()
# # se.talk()
# # st.write(recording['bytes'])

# # import streamlit as st

# def change_icon():
#     st.session_state.icon = "fa fa-microphone"
    

# st.button(microphone, on_click=change_icon)

# # if "icon" not in st.session_state:
# #     st.session_state.icon = "fa fa-home"

# # st.write(st.session_state.icon)



# mic_button(microphone,red_square)

# import streamlit as st
st.markdown(components.html("<html><body><a  href="'https://icons8.com/icon/85836/microphone'">Microphone</a> icon by <a href="'https://icons8.com'">Icons8</a></body></html>", width=50, height=50))
def change_icon():
    st.session_state.icon = red_square

st.button(microphone, on_click=change_icon)

if "icon" not in st.session_state:
    st.session_state.icon = microphone

st.write(st.session_state.icon)