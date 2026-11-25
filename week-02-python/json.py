import json

profile = {
    "name" : "Harsh",
    "age" : 23 ,
    "skills" : "Python",
    "city" : "noida" ,
    "e_status" : "unemployed"
}

json_data = json.dumps(profile)
print(json_data) 


# Exercise 2
student = {
    "name": "Harsh",
    "age": 23,
    "city": "Noida",
    "course": "Python"
}
with open("student.json","w") as file : 
    json.dump(student, file, indent=4) 


# Exercise 3
with open("student.json","r") as file :
    student = json.load(file)
print(student["name"])
print(student["age"])
print(student["city"])
print(student["course"]) 


# Exercise 4
product_json = '''
{
    "name": "MacBook",
    "price": 150000,
    "brand": "Apple",
    "available": true
}
'''
product = json.loads(product_json) 
print(product["name"])
print(product["price"])
print(product["brand"])
print(product["available"])



# Exercise 5
import json

employee = {
    "name": "Harsh",
    "skills": ["Python", "SQL", "AI"],
    "address": {
        "city": "Noida",
        "state": "Uttar Pradesh",
        "country": "India"
    }
}

with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)

with open("employee.json", "r") as file:
    e_data = json.load(file)

print(e_data["name"])
print(e_data["skills"][1])
print(e_data["address"]["city"])
print(e_data["address"]["country"])


# Exercise 6
import json

with open("student.json", "r") as file:
    student = json.load(file)

student["age"] = 24
student["learning_goal"] = "Master Python"

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

with open("student.json", "r") as file:
    updated_student = json.load(file)

print(updated_student)


# Exercise 7
import json

products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 75000,
        "quantity": 2
    },
    {
        "id": 2,
        "name": "Mouse",
        "price": 500,
        "quantity": 5
    },
    {
        "id": 3,
        "name": "Keyboard",
        "price": 1200,
        "quantity": 3
    }
]

with open("products.json", "w") as file:
    json.dump(products, file, indent=4)

with open("products.json", "r") as file:
    product_data = json.load(file)

total = 0

for item in product_data:
    print("Product:", item["name"])

    price = item["price"]
    quantity = item["quantity"]

    total += price * quantity

print("Total inventory value:", total)



# JSON Expense Tracker


