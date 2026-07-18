from tkinter import messagebox
from portfolio import add_member, get_members

import tkinter as tk
from tkinter import ttk


# ---------------- MAIN WINDOW ---------------- #

root = tk.Tk()
root.title("Team Portfolio Manager Pro")
root.geometry("1000x650")
root.configure(bg="#EAF4FC")
root.resizable(False, False)


# ---------------- TITLE ---------------- #

title = tk.Label(
    root,
    text="TEAM PORTFOLIO MANAGER",
    font=("Arial", 22, "bold"),
    bg="#1F4E79",
    fg="white",
    pady=15
)

title.pack(fill="x")


# ---------------- INPUT FRAME ---------------- #

input_frame = tk.Frame(root, bg="#EAF4FC")
input_frame.pack(pady=20)


# Labels and Entry Boxes

fields = [
    "Name",
    "Role",
    "Skills",
    "Email",
    "Phone",
    "GitHub",
    "LinkedIn",
    "Projects"
]

entries = {}

for i, field in enumerate(fields):
    label = tk.Label(
        input_frame,
        text=field,
        font=("Arial", 12, "bold"),
        bg="#EAF4FC"
    )

    label.grid(row=i, column=0, padx=15, pady=8, sticky="w")

    entry = tk.Entry(
        input_frame,
        width=45,
        font=("Arial", 11)
    )

    entry.grid(row=i, column=1, padx=10)

    entries[field] = entry


# ---------------- BUTTONS ---------------- #

button_frame = tk.Frame(root, bg="#EAF4FC")
button_frame.pack(pady=15)

buttons = [
    "Add",
    "Search",
    "Update",
    "Delete",
    "Clear"
]

commands = {
    "Add": add_data,
    "Clear": clear_entries
}

for button in buttons:

    tk.Button(
        button_frame,
        text=button,
        width=12,
        bg="#1F4E79",
        fg="white",
        font=("Arial",11,"bold"),
        command=commands.get(button)
    ).pack(side="left", padx=8)
    tk.Button(
        button_frame,
        text=button,
        width=12,
        bg="#1F4E79",
        fg="white",
        font=("Arial", 11, "bold")
    ).pack(side="left", padx=8)


# ---------------- TABLE ---------------- #

table_frame = tk.Frame(root)
table_frame.pack(pady=15)

columns = (
    "Name",
    "Role",
    "Skills",
    "Projects"
)

tree = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=10
)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=200)

tree.pack()


def add_data():

    member = {
        "Name": entries["Name"].get(),
        "Role": entries["Role"].get(),
        "Skills": entries["Skills"].get(),
        "Email": entries["Email"].get(),
        "Phone": entries["Phone"].get(),
        "GitHub": entries["GitHub"].get(),
        "LinkedIn": entries["LinkedIn"].get(),
        "Projects": entries["Projects"].get()
    }

    # Check empty fields
    if member["Name"] == "":
        messagebox.showerror("Error", "Name cannot be empty!")
        return

    add_member(member)

    messagebox.showinfo("Success", "Member Added Successfully!")

    clear_entries()
    load_table()
def clear_entries():

    for entry in entries.values():
        entry.delete(0, "end")
def load_table():

    for row in tree.get_children():
        tree.delete(row)

    members = get_members()

    for member in members:
        tree.insert("", "end", values=(
            member["Name"],
            member["Role"],
            member["Skills"],
            member["Projects"]
        ))

load_table()
root.mainloop()
