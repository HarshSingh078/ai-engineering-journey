name = input("Enter your name : ")
age = int(input("Enter your age : "))
if(age < 0) :
    print("Invalid category")
elif(age < 13 ) :
    print(f"{name}, you are a Child.")
elif(age > 13 and age < 17) :
    print(f"{name} you are a teenager.")
elif(age > 18 and age < 59) :
    print(f"{name}, you have become old." )
elif(age == 60 or age > 60 ) :
    print(f"{name}, you are senior citizen now.") 


# Electricity Bill Calculator

print("========== ELECTRICITY BILL CALCULATOR ==========")

customer_name = input("Enter customer name: ")
units = float(input("Enter electricity units consumed: "))

if units < 0:
    print("Invalid electricity consumption.")

elif units <= 100:
    bill = units * 3

elif units <= 200:
    bill = (100 * 3) + ((units - 100) * 5)

elif units <= 400:
    bill = (100 * 3) + (100 * 5) + ((units - 200) * 7)

else:
    bill = (100 * 3) + (100 * 5) + (200 * 7) + ((units - 400) * 8)

if units >= 0:
    print("\n========== ELECTRICITY BILL ==========")
    print(f"Customer: {customer_name}")
    print(f"Units consumed: {units}")
    print(f"Total electricity bill: Rs. {bill:.2f}")
    print("======================================")



# Exercise 1 
number = int(input("Enter your number : "))
if(number>0) :
    print("Your number was positive")
elif(number<0) :
    print("Your number was negative")
else :
    print("Your number was zero.")


# Exercise 2 
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))
if(num1 > num2 and num1 > num3) :
    print("First number was larget")
elif(num1 > num2 and num1 < num3) :
    print("Third number was largest")
elif(num1 > num2 and num2 > num3) :
    print("First number was largest")
elif(num1 < num2 and num2 > num3 ) :
    print("Second number was largest") 
elif(num1 > num3 and num3 < num2) :
    print("First number was largest")

# Exercise 3 
userName = "TonyStark"
Password = "iloveyou3000"
u_name = input("Enter your name : ")
u_pass = input("Enter your password : ")
if(u_name == userName and u_pass == Password) :
    print("You logged in successfully!") 
else :
    print("Try again later!")


# Exercise 4 
year = int(input("Enter your year : "))
if(year%400) :
    print("Your year is a leap year")
elif(year%100==0 and year%400!=0) :
    print("Your year is not a leap year")
elif(year%4==0) :
    print("Your year is a leap year")

# Exercise 5 
amount = int(input("Enter your amount : "))
if(amount < 1000) :
    print("You have to pay : ", amount)
elif(amount >= 1000 and amount <= 4999) :
    discount = (amount / 100) * 5 
    total_pay = amount - discount 
    print(f"You had {amount} but getting {discount}, now you have to pay {total_pay}")
elif(amount >= 5000 and amount <= 9999) :
    discount = (amount / 100) * 10
    total_pay = amount - discount 
    print(f"You had {amount} but getting {discount}, now you have to pay {total_pay}")
elif(amount >= 10000) :
    discount = (amount / 100) * 15
    total_pay = amount - discount 
    print(f"You had {amount} but getting {discount}, now you have to pay {total_pay}")

 