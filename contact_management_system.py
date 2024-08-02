contact_list = {}

def main():
    while True:
        print("Welcome to the Contact Management System!\n"
              "Menu:\n"
              "1. Add a new contact\n"
              "2. Edit an existing contact\n"
              "3. Delete a contact\n"
              "4. Search for a contact\n"
              "5. Find all contacts\n"
              "6. Export contacts to a text file\n"
              "7. Import contacts from a text file\n"
              "8. Quit")
        
        user_input = input("Choose an option (1-8): ")
        
        try:
            if user_input == '1':
                add_contact()
            elif user_input == '2':
                edit_contact()
            elif user_input == '3':
                delete_contact()
            elif user_input == '4':
                search_contact()
            elif user_input == '5':
                find_all_contacts()
            elif user_input == '6':
                export_contact()
            elif user_input == '7':
                import_contact()
            elif user_input == '8':
                print("Thanks for using the Contact Management System! Exiting program now.")
                break
            else:
                print("Invalid choice, choose an option between 1 and 8.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            print("Returning to main menu.\n\n")

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone: ")
    contact_list[name] = phone
    print(f"Contact {name} added successfully.")

def edit_contact():
    name = input("Enter the name of the contact you want to edit: ")
    if name in contact_list:
        phone = input(f"Enter new phone number for {name}: ")
        contact_list[name] = phone
        print(f"Contact {name} updated successfully.")
    else:
        print(f"Contact {name} not found.")

def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in contact_list:
        del contact_list[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")

def search_contact():
    name = input("Enter the name of the contact you want to search: ")
    if name in contact_list:
        print(f"Contact found: {name} - {contact_list[name]}")
    else:
        print(f"Contact {name} not found.")

def find_all_contacts():
    if contact_list:
        print("All contacts:")
        for name, phone in contact_list.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")

def export_contact():
    filename = input("Enter the filename to export contacts: ")
    with open(filename, 'w') as file:
        for name, phone in contact_list.items():
            file.write(f"{name}: {phone}\n")
    print(f"Contacts exported to {filename} successfully.")

def import_contact():
    filename = input("Enter the filename to import contacts: ")
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, phone = line.strip().split(': ')
                contact_list[name] = phone
        print(f"Contacts imported from {filename} successfully.")
    except FileNotFoundError:
        print(f"File {filename} not found.")

if __name__ == "__main__":
    main()
