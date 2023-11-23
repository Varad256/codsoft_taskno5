import tkinter as tk
from tkinter import ttk, messagebox


class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("820x520")
        self.root.resizable(True, True)

        # Initialize variables
        self.contacts = []

        # Styling
        self.style = ttk.Style()
        self.style.configure("TButton", padding=5, font=('Times', 12), background="teal", foreground="black")
        self.style.configure("TLabel", font=('Times', 12))
        self.style.configure("TEntry", font=('Times', 12))
        self.style.configure("Header.TFrame", background="#2c3e50")
        self.style.configure("Title.TLabel", font=('Times', 20, 'bold'), background="#2c3e50", foreground="white")

        # Create a header frame with a title label
        self.header_frame = ttk.Frame(root, padding=(10, 5), style="Header.TFrame")
        self.header_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

        # Title label
        self.title_label = ttk.Label(self.header_frame, text="My Contact Book", style="Title.TLabel")
        self.title_label.grid(row=0, column=3, pady=10, padx=10)

        # Create a contact details frame
        self.details_frame = ttk.Frame(root, padding=(20, 10))
        self.details_frame.grid(row=1, column=0, sticky="nsew")

        # Create GUI elements
        self.name_label = ttk.Label(self.details_frame, text="Name:")
        self.name_entry = ttk.Entry(self.details_frame, font=('Times', 12))

        self.phone_label = ttk.Label(self.details_frame, text="Phone Number:")
        self.phone_entry = ttk.Entry(self.details_frame, font=('Times', 12))

        self.email_label = ttk.Label(self.details_frame, text="Email:")
        self.email_entry = ttk.Entry(self.details_frame, font=('Times', 12))

        self.address_label = ttk.Label(self.details_frame, text="Address:")
        self.address_entry = ttk.Entry(self.details_frame, font=('Times', 12))

        # Create action buttons with styling
        self.add_button = ttk.Button(root, text="Add Contact", command=self.add_contact)
        self.view_button = ttk.Button(root, text="View Contacts", command=self.view_contacts)
        self.search_button = ttk.Button(root, text="Search Contact", command=self.search_contact)
        self.update_button = ttk.Button(root, text="Update Contact", command=self.update_contact)
        self.delete_button = ttk.Button(root, text="Delete Contact", command=self.delete_contact)

        # Place GUI elements on the grid
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10, sticky="ew")
        self.search_button.grid(row=6, column=0, columnspan=2, pady=10, sticky="ew")
        self.update_button.grid(row=7, column=0, columnspan=2, pady=10, sticky="ew")
        self.delete_button.grid(row=8, column=0, columnspan=2, pady=10, sticky="ew")

        # Configure row and column weights for resizing
        for i in range(2):
            self.root.columnconfigure(i, weight=1)
            self.details_frame.columnconfigure(i, weight=1)

        for i in range(9):
            self.root.rowconfigure(i, weight=1)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and Phone Number are required!")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts available.")
        else:
            contact_list = "\n".join(
                [f"{contact['Name']}: {contact['Phone']}: {contact['Email']}: {contact['Address']}" for contact in
                 self.contacts])
            messagebox.showinfo("Contacts", contact_list)

    def search_contact(self):
        search_name = self.name_entry.get()
        search_phone = self.phone_entry.get()

        if not search_name and not search_phone:
            messagebox.showerror("Error", "Enter Name or Phone Number to search.")
            return

        found_contacts = []

        for contact in self.contacts:
            if (search_name and search_name.lower() in contact['Name'].lower()) or \
                    (search_phone and search_phone in contact['Phone']):
                found_contacts.append(contact)

        if found_contacts:
            contact_list = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in found_contacts])
            messagebox.showinfo("Search Results", contact_list)
        else:
            messagebox.showinfo("Search Results", "No matching contacts found.")

    def update_contact(self):
        search_name = self.name_entry.get()

        if not search_name:
            messagebox.showerror("Error", "Enter Name to update.")
            return

        for i, contact in enumerate(self.contacts):
            if search_name.lower() == contact['Name'].lower():
                # Update the contact details
                self.contacts[i]['Phone'] = self.phone_entry.get()
                self.contacts[i]['Email'] = self.email_entry.get()
                self.contacts[i]['Address'] = self.address_entry.get()
                messagebox.showinfo("Success", "Contact updated successfully!")
                self.clear_entries()
                return

        messagebox.showinfo("Error", "Contact not found.")

    def delete_contact(self):
        search_name = self.name_entry.get()

        if not search_name:
            messagebox.showerror("Error", "Enter Name to delete.")
            return

        for i, contact in enumerate(self.contacts):
            if search_name.lower() == contact['Name'].lower():
                del self.contacts[i]
                messagebox.showinfo("Success", "Contact deleted successfully!")
                self.clear_entries()
                return

        messagebox.showinfo("Error", "Contact not found.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    contact_book = ContactBook(root)
    root.mainloop()
