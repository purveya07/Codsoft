def display_menu():
    """Display the main menu options."""
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact(contacts):
    """Add a new contact to the contact book."""
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print(f"Contact '{name}' added successfully!")

def view_contact_list(contacts):
    """Display all contacts in the contact book."""
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")

def search_contact(contacts):
    """Search for a contact by name or phone number."""
    search_term = input("Enter name or phone number to search: ")
    found = False

    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['phone']:
            print(f"\nName: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            found = True

    if not found:
        print("No matching contacts found.")

def update_contact(contacts):
    """Update an existing contact's details."""
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print(f"Updating contact '{name}':")
        contacts[name]['phone'] = input("Enter new phone number: ")
        contacts[name]['email'] = input("Enter new email: ")
        contacts[name]['address'] = input("Enter new address: ")
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(contacts):
    """Delete a contact from the contact book."""
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found.")

def main():
    """Main function to run the contact book application."""
    contacts = {}  # Dictionary to store contacts

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contact_list(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()