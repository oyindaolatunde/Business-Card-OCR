#!/usr/bin/python
import re
from ContactInfo import ContactInfo

#function to parse business car
def getContactInfo(document):
    buff = document.split('\n')
    name = ""
    phone_number = ""
    email_address = ""

    file = open('name.txt', 'r')
    start = file.tell()

    for line in buff:
        searchObj = re.search(r'[0-9]{10}|([+][0-9]+[\s])?[(]?([ 0-9]{3,}[)\s-]?){3,}', line, re.I)
        if searchObj:
            if re.match(r'fax', line, re.M|re.I):
                continue
            else:
                phone_number = searchObj.group()
                phone_number = re.sub(r'\D', "", phone_number)
                continue

        searchObj = re.search(r'[a-zA-Z0-9]+[a-zA-Z\W]+@[a-zA-z]+\.[a-zA-Z]+', line, re.M|re.I)
        if searchObj:
            email_address = searchObj.group()
            continue

        if not name:
            file.seek(start)
            temp = line.split()
            for x in file.readlines():
                if re.search(temp[0], x, re.I):
                    name = line
                    break

    return ContactInfo(name, phone_number, email_address)


#Prompt user for name of business card file
filename = raw_input("Enter business card file: ")

#Read file into string
with open(filename, "r") as myfile:
    data = myfile.read()

card = getContactInfo(data)

#Print contact information
print "Name: ", card.name
print "Phone: ", card.phone_number
print "Email: ", card.email_address

raw_input("Press Enter to Close")