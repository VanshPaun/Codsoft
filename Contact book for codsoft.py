import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, master):
        self.master = master
        master.title("Contact Book")

        # Initialize contact list
        self.contacts = {}

        # Create frames
        self.frame_add = tk.Frame(master)
        self.frame_add.pack(pady=10)

        self.frame_view = tk.Frame(master)
        self.frame_view.pack(pady=10)

        self.frame_search = tk.Frame(master)
        self.frame_search.pack(pady=10)

        # Add Contact
        self.label_name = tk.Label(self.frame_add, text="Name:")
        self.label_name.pack(side=tk.LEFT, padx=5)
        self.entry_name = tk.Entry(self.frame_add, width=20)
        self.entry_name.pack(side=tk.LEFT, padx=5)

        self.label_phone = tk.Label(self.frame_add, text="Phone:")
        self.label_phone.pack(side=tk.LEFT, padx=5)
        self.entry_phone = tk.Entry(self.frame_add, width=20)
        self.entry_phone.pack(side=tk.LEFT, padx=5)

        self.label_email = tk.Label(self.frame_add, text="Email:")
        self.label_email.pack(side=tk.LEFT, padx=5)
        self.entry_email = tk.Entry(self.frame_add, width=20)
        self.entry_email.pack(side=tk.LEFT, padx=5)

        self.label_address = tk.Label(self.frame_add, text="Address:")
        self.label_address.pack(side=tk.LEFT, padx=5)
        self.entry_address = tk.Entry(self.frame_add, width=20)
        self.entry_address.pack(side=tk.LEFT, padx=5)

        self.button_add = tk.Button(self.frame_add, text="Add Contact", command=self.add_contact)
        self.button_add.pack(side=tk.LEFT, padx=5)

        # View Contact List
        self.label_contacts = tk.Label(self.frame_view, text="Contacts:")
        self.label_contacts.pack(pady=5)
        self.listbox_contacts = tk.Listbox(self.frame_view, width=40)
        self.listbox_contacts.pack(pady=5)

        # Search Contact
        self.label_search = tk.Label(self.frame_search, text="Search:")
        self.label_search.pack(side=tk.LEFT, padx=5)
        self.entry_search = tk.Entry(self.frame_search, width=20)
        self.entry_search.pack(side=tk.LEFT, padx=5)
        self.button_search = tk.Button(self.frame_search, text="Search", command=self.search_contact)
        self.button_search.pack(side=tk.LEFT, padx=5)

        # Update and Delete Contact
        self.button_update = tk.Button(self.frame_search, text="Update", command=self.update_contact)
        self.button_update.pack(side=tk.LEFT, padx=5)
        self.button_delete = tk.Button(self.frame_search, text="Delete", command=self.delete_contact)
        self.button_delete.pack(side=tk.LEFT, padx=5)

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        if name and phone:
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            self.listbox_contacts.insert(tk.END, f"{name} - {phone}")
            self.entry_name.delete(0, tk.END)
            self.entry_phone.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.entry_address.delete(0, tk.END)
            self.view_contacts()
        else:
            messagebox.showerror("Error", "Please enter name and phone number.")

    def view_contacts(self):
        self.listbox_contacts.delete(0, tk.END)
        for name, details in self.contacts.items():
            self.listbox_contacts.insert(tk.END, f"{name} - {details['phone']}")

    def search_contact(self):
        search_term = self.entry_search.get()
        results = [name for name, details in self.contacts.items() if search_term in name or search_term in details["phone"]]
        self.listbox_contacts.delete(0, tk.END)
        for result in results:
            self.listbox_contacts.insert(tk.END, f"{result} - {self.contacts[result]['phone']}")

    def update_contact(self):
        selected_index = self.listbox_contacts.curselection()
        if selected_index:
            name = self.listbox_contacts.get(selected_index)
            name = name.split(" - ")[0]
            phone = self.entry_phone.get()
            email = self.entry_email.get()
            address = self.entry_address.get()

            if phone:
                self.contacts[name]["phone"] = phone
            if email:
                self.contacts[name]["email"] = email
            if address:
                self.contacts[name]["address"] = address

            self.view_contacts()
        else:
            messagebox.showerror("Error", "Please select a contact to update.")

    def delete_contact(self):
        selected_index = self.listbox_contacts.curselection()
        if selected_index:
            name = self.listbox_contacts.get(selected_index)
            name = name.split(" - ")[0]
            del self.contacts[name]
            self.view_contacts()
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")

root = tk.Tk()
contact_book = ContactBook(root)
root.mainloop()
