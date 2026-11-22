# shopping_list = []

# while True:

#     print("\n===== SHOPPING LIST MANAGER =====")
#     print("1. Add product")
#     print("2. View shopping list")
#     print("3. Remove product")
#     print("4. Search product")
#     print("5. Sort shopping list")
#     print("6. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":

#         product = input("Enter product name: ")
#         shopping_list.append(product)
#         print("Product added successfully!")

#     elif choice == "2":

#         if len(shopping_list) == 0:
#             print("Your shopping list is empty.")

#         else:
#             for i, product in enumerate(shopping_list, start=1):
#                 print(i, product)

#     elif choice == "3":

#         product = input("Enter product to remove: ")

#         if product in shopping_list:
#             shopping_list.remove(product)
#             print("Product removed!")
#         else:
#             print("Product not found.")

#     elif choice == "4":

#         product = input("Enter product to search: ")

#         if product in shopping_list:
#             print("Product found!")
#         else:
#             print("Product not found.")

#     elif choice == "5":

#         shopping_list.sort()
#         print("Shopping list sorted!")

#     elif choice == "6":

#         print("Thank you!")
#         break

#     else:
#         print("Invalid choice. Try again.")



# Exercise 1 
fruits = ["Apple","Banana","Guava","Kiwi","Litchi"]
fruits.append("Papaya") 
fruits.remove("Banana")
fruits[2] = "Strawberry"
print(fruits) 


# Exercise 2
numbers = [1,2,3,4,5,6,7,8,9,10]
print(max(numbers))
print(min(numbers))
print(sum(numbers))


# Exercise 3 
numbers = [1,1,2,2,3,3,4,4,5,5]
numbers2 = set()
for i in numbers :
    numbers2.add(i)
print(numbers2)

# Exercise 4
profile = ('Harsh','23','Noida')
name = profile[0]
age = profile[1] 
city = profile[2] 
print(f"{name} is of {age} and live in {city}")


# Exercise 5
num = {1, 2, 3}
num2 = {4, 5, 3}

unionop = num | num2
print(unionop)

interop = num & num2
print(interop)

diffop = num - num2
print(diffop)

# Exercise 6
profileinfo = {
    "name": "Harsh",
    "age": 23,
    "marks": 99
}

profileinfo["marks"] = 100
profileinfo["subject"] = "Development"

for key, value in profileinfo.items():
    print(key, ":", value)