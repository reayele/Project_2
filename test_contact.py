"""
Program Name: Contact Manager
Author: Rediet Ayele 
Purpose: Helps with Testing the contact class and the function.  
Starter Code: None
Date: 07/12/26
"""

import unittest

from contact import Contact

class TestContact(unittest.TestCase):
    
    def test_create_contact(self):
        contact = Contact("John", "6141234567", "john@email.com")
        self.assertEqual(contact.name, "John")
        self.assertEqual(contact.phone,"6141234567")
        self.assertEqual(contact.email,"john@email.com")

    def test_update_contact(self):
        contact = Contact("John", "6141234567", "john@email.com")
        contact.contact_update("7409876543", "new123@email.com")
        self.assertEqual(contact.phone, "7409876543")
        self.assertEqual(contact.email, "new123@email.com")

    def test_to_dictionary(self):
        contact = Contact("John", "6141234567", "john@email.com")
        dictionary = contact.to_dictionary()
        self.assertEqual(dictionary["name"], "John")
        self.assertEqual(dictionary["phone"], "6141234567")
        self.assertEqual(dictionary["email"], "john@email.com")

if __name__ == "__main__":
    unittest.main()