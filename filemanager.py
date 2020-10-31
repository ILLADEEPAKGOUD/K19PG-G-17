from tkinter import *
from PIL import ImageTk, Image
import shutil         
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb

# Main functions in file manager

# opening a file box window 
def open_window():
    read=easygui.fileopenbox()
    return read

#  for opening  a file 
def open_file():
    string = open_window()
    try:
        os.startfile(string)
    except:
        mb.showinfo('confirmation', "the File not found!")

# for copying a  file 
def copy_file():
    source1 = open_window()
    destination1=filedialog.askdirectory()
    shutil.copy(source1,destination1)
    mb.showinfo('confirmation', "sucessfully File Copied !")

# for deleting file 
def delete_file():
    del_file = open_window()
    if os.path.exists(del_file):
        os.remove(del_file)             
    else:
        mb.showinfo('confirmation', "File does not exist  !")

# for renaming  file 
def rename_file():
    chosenFile = open_window()
    path1 = os.path.dirname(chosenFile)
    extension=os.path.splitext(chosenFile)[1]
    print("Enter a  new name for the selected  file")
    newName=input()
    path = os.path.join(path1, newName+extension)
    print(path)
    os.rename(chosenFile,path) 
    mb.showinfo('confirmation', "successfully File Renamed !")

# for moving  file 
def move_file():
    source = open_window()
    destination =filedialog.askdirectory()
    if(source==destination):
        mb.showinfo('confirmation', "Source and destination are same")
    else:
        shutil.move(source, destination)  
        mb.showinfo('confirmation', "the File Moved !")

#  for making  a new folder
def make_folder():
    newFolderPath = filedialog.askdirectory()
    print("Enter name of new folder")
    newFolder=input()
    path = os.path.join(newFolderPath, newFolder)  
    os.mkdir(path)
    mb.showinfo('confirmation', "the Folder created !")

# for removing a folder
def remove_folder():
    delFolder = filedialog.askdirectory()
    os.rmdir(delFolder)
    mb.showinfo('confirmation', "the Folder Deleted !")

# for to list all the files in folder
def list_files():
    folderList = filedialog.askdirectory()
    sortlist=sorted(os.listdir(folderList))       
    i=0
    print("Files in ", folderList, "the folder are:")
    while(i<len(sortlist)):
        print(sortlist[i]+'\n')
        i+=1
    

#Creating the UI of LPU file manager

root = Tk()

Label(root, text="LPU File Manager", font=("Helvetica", 16), fg="blue").grid(row = 5, column = 2)

Button(root, text = "Open a File", command = open_file).grid(row=15, column =2)

Button(root, text = "Copy a File", command = copy_file).grid(row = 25, column = 2)

Button(root, text = "Delete a File", command = delete_file).grid(row = 35, column = 2)

Button(root, text = "Rename a File", command = rename_file).grid(row = 45, column = 2)

Button(root, text = "Move a File", command = move_file).grid(row = 55, column =2)

Button(root, text = "Make a Folder", command = make_folder).grid(row = 75, column = 2)

Button(root, text = "Remove a Folder", command = remove_folder).grid(row = 65, column =2)

Button(root, text = "List all Files in Directory", command = list_files).grid(row = 85,column = 2)



root.mainloop()