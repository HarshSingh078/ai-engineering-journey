
import json
from pathlib import Path
from datetime import date

# JSON file location
file_path = Path("expenses.json")


# 1. Load expenses from JSON
def load_expenses():

    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    return []


# 2. Save expenses into JSON
def save_expenses(expenses):

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


# 3. Add a new expense
def add_expense():

    expenses = load_expenses()

    title = input("Enter expense title: ").strip()

    if not title:
        print("Title cannot be empty.")
        return

    amount = float(input("Enter expense amount: "))

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    category = input("Enter expense category: ").strip()

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

    save_expenses(expenses)

    print("Expense added successfully!")


# 4. View all expenses
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


# 5. Search expenses by category
def search_expenses():

    expenses = load_expenses()

    category = input("Enter category to search: ").strip().lower()

    if not category:
        print("Category cannot be empty.")
        return

    found = False

    for expense in expenses:

        if expense["category"].lower() == category:

            print("\nTitle:", expense["title"])
            print("Amount: ₹", expense["amount"])
            print("Category:", expense["category"])
            print("Date:", expense["date"])

            found = True

    if not found:
        print("No expenses found in this category.")


# 6. Calculate total expenses
def calculate_total():

    expenses = load_expenses()

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total expenses: ₹", round(total, 2))


# 7. Delete an expense
def delete_expense():

    expenses = load_expenses()

    if not expenses:
        print("No expenses available to delete.")
        return

    expense_id = int(input("Enter expense ID to delete: "))

    updated_expenses = [
        expense for expense in expenses
        if expense["id"] != expense_id
    ]

    if len(updated_expenses) == len(expenses):
        print("Expense ID not found.")
        return

    save_expenses(updated_expenses)

    print("Expense deleted successfully!")


# 8. Main application menu
def main():

    while True:

        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search by Category")
        print("4. Calculate Total Expenses")
        print("5. Delete Expense")
        print("6. Exit")

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
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
