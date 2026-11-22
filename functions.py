# Exercise 1
def greeting(name) :
    print(f"Hello, {name}") 
greeting("Harsh") 


# Exercise 2
def add(a,b) :
   print (a+b) 
add(10,20)
def sub(a,b) :
   print (a-b) 
sub(10,20)
def mul(a,b) :
   print (a*b) 
mul(10,20)
def div(a,b) :
   print (a/b) 
div(10,20)

# Exercise 3
def e_or_o(number) :
   if(number % 2 == 0) :
      print(f"{number} is even")
   else :
      print(f"{number} is odd")
e_or_o(99) 


# Exercise 4
def area(length,breadth) :
   print(f"The area of rectangle is : ", length*breadth)
area(10,15)


# Exercise 5
def introduce(name,country="India") :
   print(f"{name} is from {country}")
introduce("Harsh")


# Exercise 6
def ctof(celsius) :
    F = (celsius * 9/5) + 32.
    print("Value in Fahrenheit is : ", F) 
ctof(100) 


# Contact Manangement System
contacts = [] 
# def add_Contact() :
#    name = input("Tell me your name : ")
#    age = int(input("Tell me your age : ")) 
#    email = input("Tell me your email : ")
#    profile = {} 
#    profile["name"] = name 
#    profile["age"] = age 
#    profile["email"] = email 
#    contacts.append(profile)
#    print("Your contacts has been updated") 

# Corrected Code 
def add_contact():
    name = input("Tell me your name: ")
    age = int(input("Tell me your age: "))
    email = input("Tell me your email: ")

    profile = {
        "name": name,
        "age": age,
        "email": email
    }

    contacts.append(profile)

    print("Your contact has been updated!")

def view_contact() : 
   if len(contacts) == 0 :
      print("Your contact list is empty.")
   else :
      for i in range(len(contacts)) :
         print(contacts[i])


# def search_contacts() :
#     name = input("What contact you want to search : ")
#     if name in contacts : 
#        print(f"His contact details are : {contacts[name]} ",)
#     else :
#        print("Contact Not Found.")

# Corrected Code
def search_contacts():
    name = input("What contact do you want to search: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Contact found:", contact)
            return

    print("Contact not found.")

# def update_contact() :
#     search = input("Enter the name you want to update : ")
#     if search in contacts :
#        print("You can update the contact")
#     else :
#        print("Contact not found.")

# Corrected Code
def update_contact():
    name = input("Enter the contact name: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():

            contact["email"] = input("Enter new email: ")
            contact["age"] = int(input("Enter new age: "))

            print("Contact updated successfully!")
            return

    print("Contact not found.")

# def delete_contact() :
#    name = input("Enter contact name you want to delete : ")
#    if name in contacts :
#       contacts.remove(name) 
#       print("Contact is deleted.")


# Corrected Code
def delete_contact():
    name = input("Enter contact name you want to delete: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():

            contacts.remove(contact)

            print("Contact deleted successfully!")
            return

    print("Contact not found.")


