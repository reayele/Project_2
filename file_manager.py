"""
Program Name: Contact Manager
Author: Rediet Ayele 
Purpose: Helps with saving and loding the contacts with JSON
Starter Code: None
Date: 07/12/26
"""

import json

def save_contacts(contacts):
    contact_list = []
    for contact in contacts:
        contact_list.append(contact.to_dictionary())

    file = open("contacts.json", "w")
    json.dump(contact_list, file)
    file.close()