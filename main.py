class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact.name}, {contact.phone}")

    def search_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                self.display_contact(contact)
                return contact
        print("Contact not found.")
        return None

    def update_contact(self, old_contact, name, phone, email, address):
        old_contact.name = name
        old_contact.phone = phone
        old_contact.email = email
        old_contact.address = address
        print("Contact updated successfully.")

    def delete_contact(self, contact):
        self.contacts.remove(contact)
        print("Contact deleted successfully.")

    def display_contact(self, contact):
        print(f"Name: {contact.name}")
        print(f"Phone: {contact.phone}")
        print(f"Email: {contact.email}")
        print(f"Address: {contact.address}")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            search_term = input("Enter name or phone number of the contact to update: ")
            contact = contact_book.search_contact(search_term)
            if contact:
                name = input("Enter new name: ")
                phone = input("Enter new phone number: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                contact_book.update_contact(contact, name, phone, email, address)
        elif choice == '5':
            search_term = input("Enter name or phone number of the contact to delete: ")
            contact = contact_book.search_contact(search_term)
            if contact:
                contact_book.delete_contact(contact)
        elif choice == '6':
            print("Exiting the contact book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
