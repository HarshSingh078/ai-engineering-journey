class Person:
    def __init__(self,name,age,city):
        self.name = name 
        self.age = age 
        self.city = city
    def display_details(self) :
        print(f"Name : {self.name}, Age : {self.age}, City : {self.city}")
person1 = Person("Harsh",23,"Noida")
person2 = Person("Rahul",21,"Delhi")
person1.display_details()
person2.display_details()

# Exercise 2
class Calculator:

    def addition(self, number1, number2):
        print(f"Sum: {number1 + number2}")

    def subtraction(self, number1, number2):
        print(f"Difference: {number1 - number2}")

    def multiplication(self, number1, number2):
        print(f"Product: {number1 * number2}")

    def division(self, number1, number2):
        if number2 == 0:
            print("Cannot divide by zero.")
        else:
            print(f"Division: {number1 / number2}")


calculator1 = Calculator()

calculator1.addition(10, 20)
calculator1.subtraction(10, 20)
calculator1.multiplication(10, 20)
calculator1.division(10, 20)

# Exercise 3
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    def update_marks(self, new_marks):
        if new_marks < 0 or new_marks > 100:
            print("Marks must be between 0 and 100.")
        else:
            self.marks = new_marks
            print("Marks updated successfully!")

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"


student1 = Student("Harsh", 85)

student1.display()
print("Grade:", student1.calculate_grade())

student1.update_marks(95)

student1.display()
print("Updated Grade:", student1.calculate_grade())



# Exercise 4
class Employee:

    company = "OpenAI"

    def __init__(self, name, salary, employee_id):
        self.name = name
        self.salary = salary
        self.employee_id = employee_id

    def display(self):
        print("\nEmployee Details")
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Employee ID:", self.employee_id)
        print("Company:", self.company)


employee1 = Employee("Harsh", 50000, 101)
employee2 = Employee("Rahul", 60000, 102)
employee3 = Employee("Priya", 70000, 103)

employee1.display()
employee2.display()
employee3.display()


# Exercise 5
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def show_salary(self):
        print("Salary:", self.salary)


employee1 = Employee("Harsh", 23, 50000)

employee1.introduce()
employee1.show_salary()



# Exercise 6
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.__balance += amount
            print("Amount deposited successfully!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")

        elif amount > self.__balance:
            print("Insufficient balance.")

        else:
            self.__balance -= amount
            print("Withdrawal successful!")

    def get_balance(self):
        return self.__balance


account1 = BankAccount(10000)

account1.deposit(2000)
account1.withdraw(3000)

print("Available balance:", account1.get_balance())


# Exercise 7
class Car:

    def start(self):
        print("Car engine started")


class Bike:

    def start(self):
        print("Bike engine started")


car1 = Car()
bike1 = Bike()

vehicles = [car1, bike1]

for vehicle in vehicles:
    vehicle.start()






# MINI PROJECT

class Student:

    def __init__(self, roll_number, name, age, course, marks):
        self.roll_number = roll_number
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def display(self):
        print("\n-------------------------")
        print("Roll Number:", self.roll_number)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Marks:", self.marks)
        print("-------------------------")


class StudentManagementSystem:

    def __init__(self):
        self.students = []

    def add_student(self):

        roll_number = input("Enter roll number: ")

        # Prevent duplicate roll numbers
        for student in self.students:
            if student.roll_number == roll_number:
                print("Roll number already exists.")
                return

        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        marks = float(input("Enter marks: "))

        if age <= 0:
            print("Age must be positive.")
            return

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

        student = Student(
            roll_number, name, age, course, marks
        )

        self.students.append(student)

        print("Student added successfully!")

    def view_students(self):

        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            student.display()

    def search_student(self):

        roll_number = input("Enter roll number to search: ")

        for student in self.students:

            if student.roll_number == roll_number:
                print("Student found!")
                student.display()
                return

        print("Student not found.")

    def update_marks(self):

        roll_number = input("Enter roll number: ")

        for student in self.students:

            if student.roll_number == roll_number:

                new_marks = float(input("Enter new marks: "))

                if new_marks < 0 or new_marks > 100:
                    print("Marks must be between 0 and 100.")
                    return

                student.marks = new_marks

                print("Marks updated successfully!")
                return

        print("Student not found.")

    def delete_student(self):

        roll_number = input("Enter roll number to delete: ")

        for student in self.students:

            if student.roll_number == roll_number:

                self.students.remove(student)

                print("Student deleted successfully!")
                return

        print("Student not found.")

    def main(self):

        while True:

            print("\n===== STUDENT MANAGEMENT SYSTEM =====")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Update Marks")
            print("5. Delete Student")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.update_marks()

            elif choice == "5":
                self.delete_student()

            elif choice == "6":
                print("Thank you for using the system!")
                break

            else:
                print("Invalid choice. Try again.")


# Create the application object
app = StudentManagementSystem()

# Start the application
app.main()


