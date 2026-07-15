"""
Program Name: Contact Manager
Author: Rediet Ayele 
Purpose: Helps to define the contact class 
Starter Code: None
Date: 07/12/26
"""

class Contact:
    def __init__(self, name, phone, email):
        self.name = name 
        self.phone = phone
        self.email = email

    def contact_update(self, phone, email):
        self.phone = phone
        self.email = email

    def to_dictionary(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }