# writing to a file contains basic steps like:
# 1. Open the file with open() in write mode.
# 2. Write the data using .write() or .writelines().
# 3. Close the file with .close() (or better: use with so it closes automatically).

with open("my_bio", "w") as file:
    file.write("1. My Name is Biswajit!\n")     #creating and writing a single line to a file

lines = ["2. College - IIITA\n","3. Specialization - ML\n","4. Goal - Learn DSA and build projects in 6 months\n"]
with open("my_bio", "a") as file:
    file.writelines(lines)               #appending multiple lines using "a" and writelines

#reading a already created file
with open("my_bio","r") as file:
    print(file.read())                   #reads the whole file in one go

with open("my_bio","r") as file:
    for line in file:
        print(line)                  # reads and prints the lines one by one 
        print(line.strip())         # strip() delets the \n at the end of every line

with open("my_bio","r") as file:
    lines = file.readlines()          #lines becomes a list which contains all the contents of the file
    print(lines)                  

# CSV - Comma Separated Values
# It’s just a plain text file where data is stored in rows and columns, separated by commas.
import csv
data = [
    ["Roll No.","Name","College","Degree","Specialization","Duration"],
    ["018", "Biswajit", "IIITA","MTech","ML","2Years"],
    ["021", "Amrinder", "IIITA","MTech","ML","2Years"],
    ["010", "Rahul", "IIITA","MTech","ML","2Years"],
    ["005", "Gulshan", "IIITA","MTech","MNS","2Years"],
    ["020", "Abhay", "IIITA","MTech-PHD","ML","5Years"]
    ]
with open("students.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
print("The created csv file is:\n")
with open("students.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
with open("students.csv","a") as file:
    writer = csv.writer(file)
    writer.writerow(["015","XYZ","IIITA","MTech","SDE","2Years"])
with open("students.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)