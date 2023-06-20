# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 00:22:32 2021

@author: kkc
"""

def PhoneBook():
    row, col = int(input("Please enter number of contacts: ")), 5

    PhoneBook = []
    print(PhoneBook)
    for i in range(row):
        print("\nEnter contact %d details in the following order (ONLY):" % (i + 1))
        print("NOTE: * indicates mandatory fields")
        print("")
        temp = []
        for j in range(col):

            if j == 0:
                temp.append(str(input("Enter your name = ")))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("Name is a mandatory field. Process exiting due to blank field...")

            if j == 1:
                temp.append(int(input("Enter your number : ")))

            if j == 2:
                temp.append(str(input("Enter your Email Address : ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None

            if j == 3:
                temp.append(str(input("Enter your DOB in (dd/mm/yy) : ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
            if j == 4:
                temp.append(str(input("Enter Category : ")))
                if temp[j] == "" or temp[j] == ' ':
                    temp[j] = None

        PhoneBook.append(temp)

    print(PhoneBook)
    return PhoneBook


def Menu():
    print("")
    print("\t\t\tPHONE DIRECTORY\t\t\t")
    print("")
    print("\tSelect which operation you want to perform from the given menu\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit phonebook")

    choice = int(input("Please Enter your choice = "))

    return choice


def AddContact(pb):
    # Adding a contact is the easiest because all you need to do is:
    # append another list of details into the already existing list
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Enter your name : ")))
        if i == 1:
            dip.append(int(input("Enter your Number : ")))
        if i == 2:
            dip.append(str(input("Enter your Email Address : ")))
        if i == 3:
            dip.append(str(input("Enter your DOB (dd/mm/yy) : ")))
        if i == 4:
            dip.append(str(input("Enter category : ")))
    pb.append(dip)
    return pb


def remove_existing(pb):
    query = str(
        input("Please enter the name of the contact you wish to remove: "))

    temp = 0

    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += 1

            print(pb.pop(i))

            print("This query has now been removed")

            return pb
    if temp == 0:
        print("Sorry, you have entered an invalid query.\n Please recheck and try again later.")

        return pb


def delete_all(pb):
    return pb.clear()


def search_existing(pb):
    choice = int(input("Enter search criteria\n\n\ 1. Name\n2. Number\n3. Email-id\n4. DOB\n5. Category(Family/Friends/Work/Others) \nPlease enter: "))

    temp = []
    check = -1

    if choice == 1:
        query = str(input("Please enter the name of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i])

    elif choice == 2:
        query = int(input("Please enter the number of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][1]:
                check = i
                temp.append(pb[i])

    elif choice == 3:
        query = str(input("Please enter the e-mail ID of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][2]:
                check = i
                temp.append(pb[i])

    elif choice == 4:
        query = str(input("Please enter the DOB (in dd/mm/yyyy format ONLY) of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][3]:
                check = i
                temp.append(pb[i])

    elif choice == 5:
        query = str(
            input("Please enter the category of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][4]:
                check = i
                temp.append(pb[i])

    else:
        print("Invalid search criteria")
        return -1

    if check == -1:
        return -1
    else:
        display_all(temp)
        return check


def display_all(pb):
    if not pb:
        print("List is empty: []")
    else:
        for i in range(len(pb)):
            print(pb[i])


def thanks():
    print("")
    print("\t\tThank you for using our Phone directory system.")
    print("\t\tPlease visit again!")
    print("")


print("")
print("Welcome to Phone Directory")
print("")

ch = 1
pb = PhoneBook()
while ch in (1, 2, 3, 4, 5):
    ch = Menu()
    if ch == 1:
        pb = AddContact(pb)
    elif ch == 2:
        pb = remove_existing(pb)
    elif ch == 3:
        pb = delete_all(pb)
    elif ch == 4:
        d = search_existing(pb)
        if d == -1:
            print("The contact does not exist. Please try again")
    elif ch == 5:
        display_all(pb)
    else:
        thanks()