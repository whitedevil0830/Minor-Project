import os, streamlit as st
path = "C:/Users/KIIT/OneDrive/Desktop/codes set/MY CODES/MINOR PROJECT/bucket lists"
def create_new_list(list_name):
    with open(path + "/" +list_name + ".txt", "w") as f:
        print("New list created successfully!")
        st.write("New list created successfully!")

def modify(list_name,item_old,item_new):
    if os.path.exists(path + "/" + list_name + ".txt"):
        with open(path + "/" + list_name + ".txt","r") as f:
            lines = f.readlines()
    for i in range(len(lines)):
        if lines[i].strip() == item_old:
            lines[i] = item_new + '\n'
            break
    with open(path + "/" + list_name + ".txt","w") as file:
        file.writelines(lines)
        
def show_list():
    files = os.listdir(path)
    if files:
        print("List of files:\n")
        st.write("List of files:\n")
        for file in files:
            file_name = file.split(".txt")
            print(file_name[0])
            st.write(file_name[0])
        return True      
    else:
        print("The folder is empty...")
        st.write("The folder is empty...")
        return False
    
def display_list(list_name):
    if os.path.exists(path + "/" + list_name + ".txt"):
        with open(path + "/" + list_name + ".txt","r") as f:
            for i in f.readlines():
                item = i.split("\n")
                print(item[0])
                st.write(item[0])
            return True
    else:
        print("No such list exists!")
        st.write("No such list exists!")
        return False
def add_item_to_list(list_name,item):
    if os.path.exists(path + "/" + list_name + ".txt"):
        with open(path + "/" + list_name + ".txt","a") as f:
            f.write(item + "\n")
            print("Item added successfully!")
            st.write("Item added successfully!")
    else:
        print("No such list exists!")
        st.write("No such list exists!")

def remove_item_from_list(list_name,item):
    if os.path.exists(path + "/" + list_name + ".txt"):
        with open(path + "/" + list_name + ".txt","r") as f:
            lines = f.readlines()
        with open(path + "/" + list_name + ".txt","w") as f:
            for line in lines:
                if line.strip("\n") != item:
                    f.write(line)
            print("Item removed successfully!")
            st.write("Item removed successfully!")
    else:
        print("No such list exists!")
        st.write("No such list exists!")