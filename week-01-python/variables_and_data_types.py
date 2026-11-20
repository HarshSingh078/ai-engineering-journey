# Calculator
first_num = float(input("Enter first number : "))
second_num = float(input("Enter second number : "))

addition = first_num + second_num 
subtraction = first_num - second_num
multiplication = first_num * second_num 
division = first_num / second_num

print("Addition of both number is : ", addition)
print("Subtraction of both number is : ", subtraction)
print("Multiplication of both number is : ", multiplication)
print("Division of both number is : ", division) 


# Unit Converter
kilometers = float(input("Enter the value in kg : ")) 
miles = kilometers * 0.621371
print("The value of kilometers in miles is : ", miles) 
Miles = float(input("Enter the value in miles : "))
KM = Miles * 1.60934
print("The value of Miles in KM is : ", KM)
kilog = float(input("Enter the value in kilogram : "))
pounds = kilog * 2.20462
print("The value of kilog in pounds is : ", pounds) 
Pounds = float(input("Enter the value in pounds : "))
KG = Pounds / 2.20462
print("The value of Pounds in KG is : ", KG)
celcius = float(input("Enter the value in celcius : "))
fahrenheit = 	(celcius * 9/5) + 32
print("The value of celcius in fahrenheit is : ", fahrenheit)
F = float(input("Enter the value in f : "))
C = (F-32) * 5/9 
print("The value of F in C is : ", C)

# Exercise 1 
name = input("Enter your name : ")
age = int(input("Enter your age : "))
height = int("Tell your height in centimeters : ")
weight = int(input("What is your weight : "))
height_meter = height / 100 

print("{name} is {age} years old and is {height} meter tall and he is {weight} kg.") 

# Exercise 2 
product = input("Enter your product name : ")
price = int(input("Enter your product's price : "))
quantity = int(input("Enter the quantity : "))
final_price = quantity * price 
print("Your {product} cost {final_price} rupees") 

# Exercise 3 
number = int(input("Enter your number : "))
if(number % 2 == 0) :
    print("Your number is even")
else :
    print("Your number is odd")

# Exercise 4 
subj1 = int(input("Enter marks : "))
subj2 = int(input("Enter marks : "))
subj3 = int(input("Enter marks : "))
subj4 = int(input("Enter marks : "))
subj5 = int(input("Enter marks : "))

total_marks = subj1 + subj2 + subj3 + subj4 + subj5 
maximum_marks = 500 
percentage = (total_marks / maximum_marks) * 100 
print("You got : ", percentage) 

# Exercise 5 
age1 = int(input("Enter your age : "))
age2 = int(input("Enter your age : "))
if(age1 == age2) :
    print("Both are same age")
elif(age1 != age2) :
    print("Both are of different age")
elif(age1>age2) :
    print("First one is older than second.")
elif(age1<age2) :
    print("Second one is older than first.")



# Mini Project 
c_name = input("Enter your name : ")
p_name = input("Enter product name : ")
p_price = int(input("Enter product price : "))
p_quantity = int(input("Enter product's quantity : "))
pfinal_price = p_price * p_quantity
p_gst = (pfinal_price/100)*18
pfinal_pay = pfinal_price + p_gst 

print("*********SHOPPING BILL*********")
print("Customer : ", c_name )
print("Product : ", p_name) 
print("Price per item : ", p_price) 
print("Quantity : ", p_quantity) 
print("Subtotal : ", pfinal_price) 
print("GST(18%) : ", p_gst) 
print("Final amount : ", pfinal_pay) 

print("===============================")
print("Thank you for shopping!")