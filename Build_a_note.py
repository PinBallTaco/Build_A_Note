from tkinter import *
from tkinter.ttk import *
from tkinter import simpledialog
import Mbar

root = Tk()
root.title("Build a Note")
root.geometry("800x600")

# initialize menu bar
menu = Menu(root)
root.config(menu=menu)


#create text box
text = Text(root, wrap=WORD, font=("Arial", 12))
text.pack()


# Starters menu
startermenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Starters", menu=startermenu)
startermenu.add_command(label="Pain/Cueing", command=lambda: Mbar.open_pain_cueing_window(text))
startermenu.add_command(label="Exit", command=root.quit)

# signs and symptoms tab

SSmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="S&S", menu=SSmenu)

#S&S functions
def TTP_input_dialogue():
    TTPinput = simpledialog.askstring("Input", "Please enter area of TTP (tenderness to palpation):", parent=root)
    if TTPinput:
        text.insert(END, f" The patient has tenderness to palpation of the {TTPinput}.")

def SW_input_dialogue():
    SWinput = simpledialog.askstring("Input", "Please enter area of swelling", parent=root)
    if SWinput:
        SW2input = simpledialog.askstring("Input", "Please enter what restrictions it causes: ", parent=root)
        if SW2input and SWinput:
            text.insert(END, f" The patient shows swelling of the {SWinput} which causes {SW2input}.")
        else:
            text.insert(END, f" The patient shows swelling of the {SWinput}.")

def ROM_input_dialogue():
    ROMinput = simpledialog.askstring("Input", "Please enter which joint shows ROM/mobility deficits", parent=root)
    if ROMinput:
        ROM2input = simpledialog.askstring("Input", "Please enter direction of mobility deficit (e.g. flexion, extension, supination, etc): ", parent=root)
        if ROM2input:
            text.insert(END, f" The patient has range of motion deficits of {ROM2input} in the {ROMinput} joint.")
        else:
            text.insert(END, f" The patient has range of motion deficits of the {ROMinput} joint.")
    else:
        ROM2input = simpledialog.askstring("Input", " Please enter direction of mobility deficit (e.g. flexion, extension, supination, etc): ", parent=root)
        if ROM2input:
            text.insert(END, f" The patient presents with limitation of range of motion in {ROM2input}.")
        

def STR_input_dialogue():
    STRinput = simpledialog.askstring("Input", "Please enter what movement they show weakness of:", parent=root)
    if STRinput:
        text.insert(END, f" The patient shows strength deficits when performing {STRinput} activities ")
        if STRinput:
            STR2input = simpledialog.askstring("Input", "please explain why this is a problem (e.g. difficulty with ADLs, lift objects, etc): ", parent=root)
            if STR2input:
                text.insert(END, f"which can cause {STR2input}.")


def SEN_input_dialogue():
    SENinput = simpledialog.askstring("Input", "please specify area of sensory deficit", parent=root)
    if SENinput:
        text.insert(END, f" The patient has tingling/numbness of the {SENinput}.")

def END_input_dialogue():
    ENDinput = simpledialog.askstring("Input", "Please enter which joint you are testing", parent=root)
    if ENDinput:
        END2input = simpledialog.askstring("Input", "Please enter the endfeel", parent=root)
        if END2input and ENDinput:
            text.insert(END, f" When testing the endfeel of the {ENDinput} joint, the end feel was {END2input}.")

def PAIN_input_dialogue():
    PAINinput = simpledialog.askstring("Input", "Please which activities / movements increase pain", parent=root)
    if PAINinput:
        text.insert(END, f" The patient presents with an increase of pain while performing {PAINinput}.")

SSmenu.add_command(label="TTP", command=TTP_input_dialogue)
SSmenu.add_command(label="Swelling", command=SW_input_dialogue)
SSmenu.add_command(label="ROM", command=ROM_input_dialogue)
SSmenu.add_command(label="Strength", command=STR_input_dialogue)
SSmenu.add_command(label="Sensation", command=SEN_input_dialogue)
SSmenu.add_command(label="End Feel", command=END_input_dialogue)
SSmenu.add_command(label="Pain", command=PAIN_input_dialogue)
SSmenu.add_command(label="Other", command=lambda: text.insert(END, " The patient also presents with "))

# justifications page
justmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Justification", command=lambda: Mbar.open_justification_window(text))



root.mainloop()