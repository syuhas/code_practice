import os
import datetime
import shutil

######### Writing to a file ##########

""" f_object = open('C:\\Users\\syuha\OneDrive\\Desktop\\Code_Snippets_Practice_Etc\\File_Manipulation\\hello.txt', 'r+')


print(f"\n \nThis is the text currrently in the file: \n\n {f_object.read()} \n\n")

newtxt = str(input('Enter the new text you would like to add to the file: '))

f_object.write(f"\n\n {newtxt}")

f_object.close() """

######### Displaying date and time creation and modificaiton of a filename entered by the user ##########

""" path = 'C:\\Users\\syuha\OneDrive\\Desktop\\Code_Snippets_Practice_Etc\\File_Manipulation\\'

f_name = str(input('Enter the file name: '))

if f_name in os.listdir(path):
    full_path = os.path.join(path, f_name)

    c_time = os.path.getctime(full_path)

    m_time = os.path.getmtime(full_path)

    c_dt = datetime.datetime.fromtimestamp(c_time)

    m_dt = datetime.datetime.fromtimestamp(m_time)

    print(f"File name: {f_name}")

    print(f"File creation time: {c_dt}")
    print(f"File modification time: {m_dt}")
else:
    print("File does not exist in the directory.") """

########## Moving a file to a new directory ##########


path = 'C:\\Users\\syuha\OneDrive\\Desktop\\Code_Snippets_Practice_Etc\\File_Manipulation\\'

f_name = 'hello.txt'

new_path = 'C:\\Users\\syuha\OneDrive\\Desktop\\Code_Snippets_Practice_Etc\\File_Manipulation\\TestFolder\\'

try:
    shutil.move(os.path.join(path, f_name), new_path)
    print(f"File {f_name} moved to {new_path}")
except Exception as err:
    print(f"This is the error that was thrown: {err}")
