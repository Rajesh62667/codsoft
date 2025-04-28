contact_list = []

def contact_add():
    name = input("Enter the contact name: ")
    phone_number = input("Enter the phone number: ")
    contact_list.append([name, phone_number])
    print("Contact added successfully.")

def contact_view():
    if not contact_list:
        print("Contact list is empty.")
        return
    for i, contact in enumerate(contact_list, start=1):
        name, phone_number = contact
        print(f"{i}. Name: {name}\n   Phone Number: {phone_number}")

def contact_search(search_name):
    found_contacts = []
    for contact in contact_list:
        name, phone_number = contact
        if search_name.lower() in name.lower():
            found_contacts.append(contact)
    if found_contacts:
        print("Search Results:")
        for i, contact in enumerate(found_contacts, start=1):
            name, phone_number = contact
            print(f"{i}. Name: {name}\n   Phone Number: {phone_number}")
    else:
        print("No contact found with this name.")

def contact_update():
    search_name = input("Enter the contact name to update: ")
    found_contact = None
    for contact in contact_list:
        name, phone_number = contact
        if search_name.lower() in name.lower():
            found_contact = contact
            break
    if found_contact:
        print("Enter updated details:")
        name = input("New Name: ")
        phone_number = input("New Phone Number: ")
        index = contact_list.index(found_contact)
        contact_list[index] = [name, phone_number]
        print("Contact updated successfully.")
    else:
        print("No contact found with this name.")

def contact_delete():
    search_name = input("Enter the name of the contact to delete: ")
    found_contact = None
    for contact in contact_list:
        name, phone_number = contact
        if search_name.lower() == name.lower():
            found_contact = contact
            break
    if found_contact:
        contact_list.remove(found_contact)
        print(f"Contact '{search_name}' deleted successfully.")
    else:
        print("No contact found with this name.")

def main():
    while True:
        print("\n===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Quit Contact App")

        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            contact_add()
        elif choice == "2":
            contact_view()
        elif choice == "3":
            search_name = input("Enter the name to search: ")
            contact_search(search_name)
        elif choice == "4":
            contact_delete()
        elif choice == "5":
            contact_update()
        elif choice == "6":
            print("Exiting Contact App.")
            break
        else:
            print("Invalid input. Please choose a valid option.")

if __name__ == "__main__":
    main()
