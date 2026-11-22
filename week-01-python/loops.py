# Exercise 1
for i in range(1,101) :
    print(i) 

# Exercise 2 
for i in range(1, 51) :
    if(i % 2 == 0) :
        print("Even numbers between 1 and 50 are : ", i)

# Exercise 3 
number = int(input("Enter your number : "))
for i in range(1,11) :
    print(f"{number}*{i} : ", number * i)

# Exercise 4
last = int(input("Enter your number : "))
sum = 0 
for i in range(1, last+1) :
    sum = sum + i 
print(sum)

# Exercise 5 
num = int(input("Enter the number : "))
fact = 1
while(num>0) :
    fact = fact * num 
    num = num - 1 
print(f"Factorial of {num} is : ", fact)

# Exercise 6
num = 10 
while(num >= 0) :
    print(num) 
    num = num - 1
print("Go")

# Mini Project 
balance = 10000

while True:
    print("\nCurrent balance:", balance)

    withd = int(input("How much do you want to withdraw? "))

    if withd <= 0:
        print("Enter a valid amount.")

    elif withd > balance:
        print("Insufficient balance.")

    elif withd % 100 != 0:
        print("Amount must be a multiple of 100.")

    else:
        balance -= withd
        print(f"You have withdrawn ₹{withd}.")
        print("Remaining balance:", balance)

    choice = input("Do you want to continue? (yes/no): ")

    if choice.lower() != "yes":
        print("Thank you for using our ATM.")
        break



        
    




