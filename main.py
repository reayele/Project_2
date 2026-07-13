"""
Program Name: Contact Manager
Author: Rediet Ayele 
Purpose: Running the main menu for the contact manager
Starter Code: None
Date: 07/12/26
"""

from contact import Contact


def main():

    contacts = [] 

    while True:
        print("--- Contact Manger ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == "6":
            print("\nGoodbye!")
            break

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            new_contact = Contact(name, phone, email)
                
            contacts.append(new_contact)
            print("You have added a contact!")
            print("Total contacts:", len(contacts))
            input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()
