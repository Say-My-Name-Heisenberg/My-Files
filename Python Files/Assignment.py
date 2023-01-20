# while True:

#     name = input("Enter Name:")
#     ph = int(input("Enter Number:"))
#     mail = input("Enter Mail:")
#     break
# cb = dict()
# cb["name"] = name
# cb["phone"] = ph
# cb["email"] = mail
# print(cb)
# li = [cb]
# for i in li:
#     print(i, end="")


names = []
contact_numbers = []
emails = []
count = 1


def Add_contact():
    name = input("Name: ")
    contact_number = int(input("Number: "))
    email = input("Email: ")
    names.append(name)
    contact_numbers.append(contact_number)
    emails.append(email)
    print("\nName\t\tContact Number\t\tEmail\n")
    for i in range(count):
        print(f"{names[i]}\t\t{contact_numbers[i]}\t\t{emails[i]}")
    print("\n\n")


def Edit_contact():
    e_name = input("Name of Edit contact:")
    if e_name in names:
        index = names.index(e_name)
        names[index] = input("Edit name: ")
        contact_numbers[index] = int(input("Edit Number: "))
        emails[index] = input("Edit Mail: ")
        print("\nName\t\tContact Number\t\tEmail\n")
        print(f"{names[index]}\t\t{contact_numbers[index]}\t\t{emails[index]}")
        print("\n\n")
    else:
        print("User not found")
    print("\n\n")


def Search_contact():
    s_name = input("Search Contact: ")
    if s_name in names:
        index = names.index(s_name)
        print(f"{names[index]}\t\t{contact_numbers[index]}\t\t{emails[index]}")
    else:
        print("User not Found")
    print("\n\n")


def Delete_contact():
    d_name = input("Search Contact: ")
    if d_name in names:
        index = names.index(d_name)
        names.pop(index)
        contact_numbers.pop(index)
        emails.pop(index)
        print("Contact Deleted")
    else:
        print("User not found")
    print("\n\n")

def View_contact():
    try:
        if count == 1:
            print("Empty List")
        else:
            print("\nName\t\tContact Number\t\tEmail\n")
            for i in range(count):
                print(f"{names[i]}\t\t{contact_numbers[i]}\t\t{emails[i]}")
                
        
    except:
        print ("........................")
        print("\n\n")

while True:
    num = int(input(
        "1.Create New Contact\n2.Edit Contact\n3.Search Contact\n4.Delete Contact\n5.View Contact List\n\nPress any (other) key to exit\n\nSelect a Option: "))

    if num == 1:
        Add_contact()
        count += 1
    elif num == 2:
        Edit_contact()
    elif num == 3:
        Search_contact()
    elif num == 4:
        Delete_contact()
    elif num == 5:
        View_contact()
    else:
        print("400 - Bad Request")
        break
