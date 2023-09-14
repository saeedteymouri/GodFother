import tkinter as tk

class NameEntryForm(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create 11 question boxes for names
        self.name_boxes = []
        for i in range(11):
            self.name_boxes.append(tk.Entry(self))
            self.name_boxes[i].grid(row=i, column=0)

        # Create a submit button
        self.submit_button = tk.Button(self, text="Submit", command=self.submit)
        self.submit_button.grid(row=11, column=0)

    def submit(self):
        # Get the names from the question boxes
        names = []
        for name_box in self.name_boxes:
            names.append(name_box.get())

        # Print the names to the console
        print("The names are:")
        for name in names:
            print(name)

root = tk.Tk()
name_entry_form = NameEntryForm(root)
name_entry_form.pack()
root.mainloop()

