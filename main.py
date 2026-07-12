"""
Program Name: Contact Manager
Author: Rediet Ayele 
Purpose: Running the main menu for the contact manager
Starter Code: None
Date: 07/12/26
"""

from contact import Contact

def main():
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

        else:
            print("\nFeature coming soon.")
            input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()
