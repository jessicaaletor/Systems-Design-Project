from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from GenerateOutput import generateOutput
from ReadMyFile import ReadMyFile




win = Tk()
app = Frame(win)
app.grid(row=6, column=2)
usrentered1 = StringVar()
usrentered2 = StringVar()
selectedvar = StringVar()
usrmode = 0
path1 = 'firstFile.csv'
path2 = 'secondFile.csv'


path1Lists = ReadMyFile(path1)
path2Lists = ReadMyFile(path2)

def Gui_Implementation():

    win.title("Keele Library Map")

    Label(win, text = "Please Select an Option:").grid(row=1, column=2, sticky=W) #Display label asking users to select an option
    # Label(win, text = "1. SubjectName").grid(row=2, column=2, sticky=W)
    # Label(win, text = "2. ClassMark").grid(row=3, column=2, sticky=W)
    # Label(win, text = "3. Location").grid(row=4, column=2, sticky=W)
    entry1 =  ttk.Combobox(win, textvariable=usrentered1, values=['SubjectName','ClassMark', 'Location' ], state='readonly') #entry input box to capture user input
    entry1.bind('<<ComboboxSelected>>', Get_Entry1) #bind a return event to the input box
    entry1.grid(row=2, column=2, sticky=W)
    Button(win, text="Reset", command=ClearAll).grid(row=2, column=5, sticky=W) #reset button to reset the frame app

    win.geometry("850x400")
    win.mainloop

#reset the app frame so input fields and their values
#  are set to empty and new search can be done
def ClearAll():
    global app;
    global usrentered1
    global usrentered2
    global selectedvar
    app.destroy()
    app = Frame(win)
    app.grid(row=6, column=2)
    usrentered2 = StringVar() #reset variable so the input field will be null
    selectedvar = StringVar() #reset variable so the input field will be null

#Gets the user input for either SubjectName,Location and ClassMark 
# and process the next step. User selection is tracked via usrmode
def Get_Entry1(event):
    global usrmode #accessing the usrmode globally so we can modify it
    gui_user_entered  = usrentered1.get()
    #check to see what user entered it could be an integer or the string 
    if (gui_user_entered == '1') | (gui_user_entered.lower() == "subjectname") : 
        Label(app, text = "Please enter subject").grid(row=1, column=1, sticky=W)
        entry2 =  Entry(app, textvariable=usrentered2)
        entry2.bind('<Return>', Get_Entry2)
        entry2.grid(row=2, column=1, sticky=W)
        usrmode = 1
    elif (gui_user_entered == '2') | (gui_user_entered.lower() == "classmark"):
        Label(app, text = "Please Enter ClassMark").grid(row=1, column=1, sticky=W)
        entry2 =  Entry(app, textvariable=usrentered2)
        entry2.bind('<Return>', Get_Entry2)
        entry2.grid(row=2, column=1, sticky=W)
        usrmode = 2
    elif (gui_user_entered == '3') | (gui_user_entered.lower() == "location"):
        usrmode = 3
        Label(app, text = "Please Select a Location").grid(row=1, column=1, sticky=W)
        #display dropdown in a combo box to list locations
        lb = Combobox(app, textvariable=selectedvar, state='readonly')
        values = []
        for location in path2Lists:
            values.append(location[0])
        lb['values'] = values
        lb.grid(row=2, column=1, sticky=W)
        lb.bind('<<ComboboxSelected>>', OnSelect) #event to bind combobox once selected
    else :
        Label(app, text = "Invalid option Entered!!!").grid(row=1, column=1, sticky=W)

 #Event to get user Location selection 
# and process the output by calling displayOutput   
def OnSelect(event):
    us2 = selectedvar.get()
    output = generateOutput(usrmode, us2, path2Lists, path1Lists)
    DisplayOutput(output)

#Event to get user selection for either ClassMark or Subjectname 
# and process the output by calling displayOutput
def Get_Entry2(event):
    us2  = usrentered2.get()
    output = generateOutput(usrmode, us2, path2Lists, path1Lists)
    DisplayOutput(output)

#Displays output based on the arraylist supplied to it
def DisplayOutput(output):
    #displays the ouput in a table
    tree = ttk.Treeview(app, column=("Subject", "ClassMark", "Floor"), show='headings')
    tree.heading("# 1", text="Subject")
    tree.heading("# 2", text="ClassMark")
    tree.heading("# 3", text="Floor")
    for outpt in output:
        splittedoutput =  outpt.split('|') #splits the output based on |
        tree.insert('', 'end', text="1", values=(splittedoutput[0],splittedoutput[1], splittedoutput[2]) )
    tree.grid(row=3, column=1, sticky=W)




Gui_Implementation()
input()