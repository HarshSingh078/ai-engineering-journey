file = open("my_info.txt","r")
content = file.read() 
print(content) 
file.close()


with open("my_info.txt","w") as file :
    file.write("My name is Harsh\n") 
    file.write("I am learning python.")

with open("my_info.txt","r") as file :
    content = file.read()
    print(content) 
    file.close()



# Exercise 2 
with open("student.txt", "w") as file:
    file.write("Name is: Harsh\n")
    file.write("Age is: 23\n")
    file.write("City is: Noida\n")
    file.write("Learning goal: Python\n")

# Exercise 3 
with open("student.txt", "a") as file:
    file.write("Favourite programming language: C++\n")
    file.write("Learning week: 2nd\n")
    file.write("Career goal: AI Engineer\n")

# Exercise 4 
with open("student.txt","r") as file :
    lines = file.readlines()
    for line in lines:
        print(line.strip())

# Exercise 5
with open("student.txt", "r") as file:
    lines = file.readlines()
    print("Total lines:", len(lines))

# Exercise 6
from pathlib import Path

folder = Path("Python_Practice")
folder.mkdir(exist_ok=True)

file_path = folder / "practice.txt"

file_path.write_text(
    "Learning Python\n"
    "From ChatGPT\n"
    "Day by day"
)

print(file_path.read_text())


# Exercise 7
from pathlib import Path

file_path = Path("student.txt")

print("File exists:", file_path.exists())
print("File name:", file_path.name)
print("File extension:", file_path.suffix)
print("Parent directory:", file_path.parent)


# Notes application 

