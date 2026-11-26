# Exercise 1
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    divide = num1 / num2

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError as error:
    print(error)

else:
    print("Division result:", divide)


# Exercise 2 
try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

except ValueError as error:
    print("Invalid age:", error)

else:
    print("Your age is:", age)


# Exercise 3
numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index number: "))

    if index < 0 or index >= len(numbers):
        raise IndexError("Index is outside the valid range.")

except ValueError:
    print("Please enter an integer.")

except IndexError as error:
    print(error)

else:
    print("Your value is:", numbers[index])


# Exercise 4
student = {
    "name": "Harsh",
    "age": 23,
    "city": "Noida"
}

key = input("Enter your key: ")

try:
    print("Value:", student[key])

except KeyError:
    print("Key not found in student dictionary.")


# Exercise 5
import json

filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        data = json.load(file)

    print(data)

except FileNotFoundError:
    print("File does not exist.")

except json.JSONDecodeError:
    print("File contains invalid JSON.")

finally:
    print("File operation finished.")

# Exercise 6
def validate_amount(amount):

    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    return amount


try:
    result = validate_amount(10)
    print("Your value is:", result)

except ValueError as error:
    print("Invalid amount:", error)


# Exercise 7 
try:
    with open("data.json", "r") as file:
        data = json.load(file)

    print(data)

except FileNotFoundError:
    print("File not found.")

except json.JSONDecodeError:
    print("File contains invalid JSON.")


# MINI PROJECT

import json
from pathlib import Path
from datetime import date

# File location
FILE_PATH = Path("expenses.json")


# 1. Load expenses safely
def load_expenses():

    if not FILE_PATH.exists():
        return []

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("Invalid data format. Expected a list.")
            return []

        return data

    except json.JSONDecodeError:
        print("Error: JSON file is empty or corrupted.")
        print("Starting with an empty expense list.")
        return []

    except OSError as error:
        print("File reading error:", error)
        return []


# 2. Save expenses safely
def save_expenses(expenses):

    try:
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4)

        return True

    except (OSError, TypeError, ValueError) as error:
        print("Error saving expenses:", error)
        return False


# 3. Validate amount
def validate_amount(amount):

    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    return amount


# 4. Get a valid amount from the user
def get_amount():

    try:
        amount = float(input("Enter expense amount: "))
        return validate_amount(amount)

    except ValueError as error:
        print("Invalid amount:", error)
        return None


# 5. Add expense
def add_expense():

    expenses = load_expenses()

    title = input("Enter expense title: ").strip()

    if not title:
        print("Title cannot be empty.")
        return

    amount = get_amount()

    if amount is None:
        return

    category = input("Enter category: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    expense_id = max(
        (expense["id"] for expense in expenses),
        default=0
    ) + 1

    expense = {
        "id": expense_id,
        "title": title,
        "amount": amount,
        "category": category,
        "date": str(date.today())
    }

    expenses.append(expense)

    if save_expenses(expenses):
        print("Expense added successfully!")


# 6. View all expenses
def view_expenses():

    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print("\n===== ALL EXPENSES =====")

    for expense in expenses:

        print("-----------------------")
        print("ID:", expense["id"])
        print("Title:", expense["title"])
        print("Amount: ₹", expense["amount"])
        print("Category:", expense["category"])
        print("Date:", expense["date"])


# 7. Search expenses
def search_expenses():

    expenses = load_expenses()

    category = input("Enter category: ").strip().lower()

    if not category:
        print("Category cannot be empty.")
        return

    found = False

    for expense in expenses:

        if expense["category"].lower() == category:

            print("-----------------------")
            print("Title:", expense["title"])
            print("Amount: ₹", expense["amount"])
            print("Date:", expense["date"])

            found = True

    if not found:
        print("No matching expenses found.")


# 8. Calculate total expenses
def calculate_total():

    expenses = load_expenses()

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total expenses: ₹", round(total, 2))


# 9. Delete expense
def delete_expense():

    expenses = load_expenses()

    if not expenses:
        print("No expenses available.")
        return

    try:
        expense_id = int(input("Enter expense ID: "))

    except ValueError:
        print("Please enter a valid ID.")
        return

    updated_expenses = [
        expense for expense in expenses
        if expense["id"] != expense_id
    ]

    if len(updated_expenses) == len(expenses):
        print("Expense ID not found.")
        return

    if save_expenses(updated_expenses):
        print("Expense deleted successfully!")


# 10. Edit expense
def edit_expense():

    expenses = load_expenses()

    if not expenses:
        print("No expenses available.")
        return

    try:
        expense_id = int(input("Enter expense ID to edit: "))

    except ValueError:
        print("Invalid expense ID.")
        return

    for expense in expenses:

        if expense["id"] == expense_id:

            print("Current title:", expense["title"])
            new_title = input("Enter new title: ").strip()

            if new_title:
                expense["title"] = new_title

            print("Current amount:", expense["amount"])
            new_amount = input("Enter new amount (press Enter to skip): ").strip()

            if new_amount:
                try:
                    expense["amount"] = validate_amount(float(new_amount))

                except ValueError as error:
                    print("Invalid amount:", error)
                    return

            print("Current category:", expense["category"])
            new_category = input("Enter new category: ").strip()

            if new_category:
                expense["category"] = new_category

            if save_expenses(expenses):
                print("Expense updated successfully!")

            return

    print("Expense ID not found.")


# 11. Category-wise totals
def category_summary():

    expenses = load_expenses()

    if not expenses:
        print("No expenses available.")
        return

    category_totals = {}

    for expense in expenses:

        category = expense["category"]

        if category in category_totals:
            category_totals[category] += expense["amount"]

        else:
            category_totals[category] = expense["amount"]

    print("\n===== CATEGORY SUMMARY =====")

    for category, total in category_totals.items():

        print(category, ": ₹", round(total, 2))


# 12. Main menu
def main():

    while True:

        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expenses")
        print("4. Calculate Total")
        print("5. Delete Expense")
        print("6. Edit Expense")
        print("7. Category Summary")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_expenses()

        elif choice == "4":
            calculate_total()

        elif choice == "5":
            delete_expense()

        elif choice == "6":
            edit_expense()

        elif choice == "7":
            category_summary()

        elif choice == "8":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
