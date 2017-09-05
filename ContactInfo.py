#!/usr/bin/python

class ContactInfo:
    #Initialize ContactInfo attributes in constructor
    def __init__(self, name, phone_number, email_address):
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address

    #Returns the full name of the individual
    def getName(self):
        return self.name

    #Returns the phone number of the individual
    def getPhoneNumber(self):
        return self.phone_number

    #Returns the email address of the individual
    def getEmailAddress(self):
        return self.email_address
