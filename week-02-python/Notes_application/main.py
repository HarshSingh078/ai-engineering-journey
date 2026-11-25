
from pathlib import Path

# Create notes directory
notes_folder = Path("notes")
notes_folder.mkdir(exist_ok=True)


# 1. Add a new note
def add_note():
    title = input("Enter note title: ").strip()

    if not title:
        print("Title cannot be empty.")
        return

    file_path = notes_folder / f"{title}.txt"

    if file_path.exists():
        print("A note with this title already exists.")
        return

    content = input("Enter note content: ")

    file_path.write_text(content, encoding="utf-8")

    print("Note saved successfully!")


# 2. View all notes
def view_notes():
    notes = list(notes_folder.glob("*.txt"))

    if not notes:
        print("No notes found.")
        return

    print("\n===== YOUR NOTES =====")

    for index, note in enumerate(notes, start=1):
        print(f"\n{index}. {note.stem}")

        content = note.read_text(encoding="utf-8")
        print(content)


# 3. Search notes
def search_notes():
    keyword = input("Enter keyword to search: ").strip().lower()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    notes = list(notes_folder.glob("*.txt"))
    found = False

    for note in notes:
        content = note.read_text(encoding="utf-8")

        if keyword in note.stem.lower() or keyword in content.lower():
            print(f"\nTitle: {note.stem}")
            print(f"Content: {content}")
            found = True

    if not found:
        print("No matching notes found.")


# 4. Delete a note
def delete_note():
    title = input("Enter note title to delete: ").strip()

    if not title:
        print("Title cannot be empty.")
        return

    file_path = notes_folder / f"{title}.txt"

    if file_path.exists():
        file_path.unlink()
        print("Note deleted successfully!")
    else:
        print("Note not found.")


# 5. Main menu
def main():
    while True:
        print("\n===== NOTES APPLICATION =====")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Search Notes")
        print("4. Delete Note")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_note()

        elif choice == "2":
            view_notes()

        elif choice == "3":
            search_notes()

        elif choice == "4":
            delete_note()

        elif choice == "5":
            print("Thank you for using Notes Application!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start application
if __name__ == "__main__":
    main()

