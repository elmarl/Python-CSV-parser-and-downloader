import csv                                  #CSV file reading tools
import urllib.request                       #Download file
import re                                   #Regular expressions
import tkinter as tk                        #Open file dialog
from tkinter.filedialog import askopenfile  #
from tkinter import simpledialog            #Ask user for delimiter
from tkinter import messagebox
import os                                   #make a directory
import sys                                  #exit script if nothing chosen

#folder to place downloaded files to
downloads_folder = "./results/"

#remove the Tkinter root window with .withdraw()
root = tk.Tk()
root.withdraw()

#select csv file with name as 1st column and HTTP address as 2nd column
try:
    file_path_IO = askopenfile(initialdir = "./",title = "Select file", filetypes = [("CSV Files","*.csv"), ("all files","*.*")])
except IOError as e:
    print("error opening file")

#check if user chose a file or not, if no file exit
if not file_path_IO:
    sys.exit()
else:
    file_path = file_path_IO.name

#create a folder to download the files
try:
    os.mkdir(downloads_folder)
except OSError as e:
    print("Directory already exists")

#Ask user for delimitator of chosen CSV file
delimiter = simpledialog.askstring(title="Delimiter",
                                  prompt="What is the delimiter in this CSV file? (space, coma, semicolon...):")
if not delimiter:
    sys.exit()

csv.register_dialect('myDialect',
delimiter = delimiter,
skipinitialspace=True)

#save the file based on the name in the first row in the csv file, not the name of the file on the web
with open(file_path, 'r') as csvFile:
    reader = csv.reader(csvFile, dialect='myDialect')
    for row in reader:
        if(row[1]!="NA"):
            if(re.search("pdf$", row[1])):
                if os.path.exists("".join((downloads_folder, row[0], ".pdf"))):
                    answer = messagebox.askyesnocancel("File already exists", "".join(("Do you want to overwrite the file: ", row[0], "?")))
                    if(answer == None):
                        sys.exit()
                    elif answer:
                        urllib.request.urlretrieve(row[1], "".join((downloads_folder, row[0], ".pdf")))
                else:
                    urllib.request.urlretrieve(row[1], "".join((downloads_folder, row[0], ".pdf")))
            if (re.search("doc$", row[1])):
                if os.path.exists("".join((downloads_folder, row[0], ".doc"))):
                    answer = messagebox.askyesnocancel("File already exists", "".join(("Do you want to overwrite the file: ", row[0], "?")))
                    if(answer == None):
                        sys.exit()
                    elif answer:
                        urllib.request.urlretrieve(row[1], "".join((downloads_folder, row[0], ".doc")))
                else:
                    urllib.request.urlretrieve(row[1], "".join((downloads_folder, row[0], ".doc")))


#csvFile.close() using 'with' with 'open' closes the file automatically at the end