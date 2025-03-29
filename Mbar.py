from tkinter import *
from tkinter.ttk import *
from tkinter import simpledialog

#Open Pain/Cueing window function
def open_pain_cueing_window(text):
    pain_cueing = Toplevel()
    pain_cueing.title("Pain/Cueing")
    pain_cueing.geometry("400x600")

    #create radio buttons for pain/cueing options
    pain_cueing_frame = Frame(pain_cueing)
    pain_cueing_frame.pack(anchor=W, pady=5)
    pain_label = Label(pain_cueing_frame, text="Patient Pain: ")
    pain_label.pack(anchor=W,  pady=5)


    p = IntVar()
    Radiobutton(pain_cueing_frame, text = "none", variable=p, value=1).pack(anchor=W, pady=5)
    Radiobutton(pain_cueing_frame, text = "mild", variable=p, value=2).pack(anchor=W, pady=5)
    Radiobutton(pain_cueing_frame, text = "moderate", variable=p, value=3).pack(anchor=W, pady=5)
    Radiobutton(pain_cueing_frame, text = "severe", variable=p, value=4).pack(anchor=W, pady=5)

    verb_cueing_label = Label(pain_cueing_frame, text="Verbal Cueing: ")
    verb_cueing_label.pack(anchor=W, pady=5)

    v = IntVar()
    Radiobutton(pain_cueing_frame, text = "none", variable=v, value=1).pack(anchor=W, pady=5)
    Radiobutton(pain_cueing_frame, text = "minimal", variable=v, value=2).pack(anchor=W, pady=5)
    Radiobutton(pain_cueing_frame, text = "moderate", variable=v, value=3).pack(anchor=W, pady=5)
    Radiobutton(pain_cueing_frame, text = "maximal", variable=v, value=4).pack(anchor=W, pady=5)


    tac_cueing_label = Label(pain_cueing_frame, text="Tactile Cueing: ")
    tac_cueing_label.pack(anchor=W, pady=5)

    t = IntVar()
    Radiobutton(pain_cueing_frame, text = "none", variable=t, value=1).pack(anchor=W, pady=5)
    Radiobutton(pain_cueing_frame, text = "minimal", variable=t, value=2).pack(anchor=W, pady=5)
    Radiobutton(pain_cueing_frame, text = "moderate", variable=t, value=3).pack(anchor=W, pady=5)
    Radiobutton(pain_cueing_frame, text = "maximal", variable=t, value=4).pack(anchor=W, pady=5)


    # Submit button
    def submit():
        # Dynamically retrieve the selected values
        pain_level = {1: "no", 2: "mild", 3: "moderate", 4: "severe"}[p.get()]
        verb_level = {1: "no", 2: "minimal", 3: "moderate", 4: "maximal"}[v.get()]
        tac_level = {1: "no", 2: "minimal", 3: "moderate", 4: "maximal"}[t.get()]

        # Insert the text into the main text box
        text.insert(
            END,
            f"The patient was able to complete all interventions with {pain_level} c/o pain, {verb_level} verbal cues, and {tac_level} tactile cues.",
        )
        pain_cueing.destroy()  # Close the window

    submit_pain_cueing_button = Button(pain_cueing_frame, text="Submit", command=submit)
    submit_pain_cueing_button.pack()

    pain_cueing.mainloop()


#Open Justification window function
def open_justification_window(text):
    just_window = Toplevel()
    just_window.title("Justification")
    just_window.geometry("400x300")
    null = ""

    just_label = Label(just_window, text="Select the justification for patient need of skilled intervention: ")
    just_label.pack(anchor=CENTER, pady=5)

    just_lb = Listbox(just_window, selectmode=MULTIPLE)
    just_lb.insert(1, "strength")
    just_lb.insert(2, "endurance")
    just_lb.insert(3, "mobility")
    just_lb.insert(4, "balance")
    just_lb.pack(anchor=CENTER, pady=5)

    def just_submit():
        selected_just_indices = just_lb.curselection()
        selected_just_items = [just_lb.get(i) for i in selected_just_indices]


        if len(selected_just_items) == 1:
            formatted_items = selected_just_items[0]
        elif len(selected_just_items) == 2:
            formatted_items = f"{selected_just_items[0]} and {selected_just_items[1]}"
        elif len(selected_just_items) > 2:
            formatted_items = ", ".join(selected_just_items[:-1]) + f", and {selected_just_items[-1]}"
        else:
            null

        text.insert(END, f" The patient requires skilled intereventions from PT to address {formatted_items} deficits that are impacting their ability to safely and effectively perform functional tasks and activities of daily living.")
        just_window.destroy()
    
    just_button = Button(just_window, text="Submit", command=just_submit)
    just_button.pack(anchor=CENTER, pady=5)

    #S&S functions
