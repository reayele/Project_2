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

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            new_contact = Contact(name, phone, email)
                
            contacts.append(new_contact)
            print("You have added a contact!")
            print("Total contacts:", len(contacts))
            input("\nPress Enter to return to the menu...")
        
        elif choice == "2":
            for contact in contacts:
                print("Name:", contact.name)
                print("Phone:", contact.phone)
                print("Email:", contact.email)
                input("\nPress Enter to return to the menu...")
            
            if len(contacts) == 0:
                print("No contacts were found!")
        
        elif choice == "3":
            print("Hi, You are now asking to search up a contact")
            print("Please enter a contact name below:")
            name = input("Enter the contact name:")
            Contactn = False

            for contact in contacts:
                if contact.name.lower() == name.lower():
                    print("Name:", contact.name)
                    print("Phone:", contact.phone)
                    print("Email:", contact.email)
                    Contactn = True
            
            if Contactn == False: 
                print("The Contact is Not found. ")
            input("\nPress Enter to return to the menu...")
        

        elif choice == "4":
            for contact in contacts:
                print("Name:", contact.name)
                print("Phone:", contact.phone)
                print("Email:", contact.email)
                input("\nPress Enter to return to the menu...")


        elif choice == "6":
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
