import os
path = "C:/Users/KIIT/OneDrive/Desktop/codes set/MY CODES/MINOR PROJECT/bucket lists/"
files = os.listdir(path)
if files:
    print("List of files:\n")
        # st.write("List of files:\n")
    for file in files:
        file_name = file.split(".txt")
        print(file_name[0])
        # st.write(file_name)