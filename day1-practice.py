 my_Dict = {
 A dictionary in Python stores data as key–value pairs just like a real-life dictionary where a word (key) maps to its meaning (value).
     "1.Name" : "Biswajit",
     "2.College" : "IIITA",
     "3.Degree" : "MTech",
     "4.Specialization" : "ML",
     "5.Year" : 1,
     "6.Semester" : 1,
     "7.Excited to learn" : "Python & DSA",
     "8.GOAL for next 6 months" : "Learn & Build"
 }
 print(my_Dict["1.Name"]);   #printing only one value

 #printing only keys
 for key in my_Dict:
     print(key)

 #printing only values
 for value in my_Dict.values():
     print(value)

 #printing both keys and their respective values
 for key, value in my_Dict.items():
     print(key, ":", value)


 #Creating a calculator function
 def add(a,b):
 # add function
     print("The Sum of a & b is : ",a+b)
 a = int(input("Enter the first value: "))     #to make it to int type
 b = int(input("Enter the second value:"))     #to make it to int type
 add(a,b)

 def subtract(a,b):
 # subtract function
     print("The Difference of a & b is : ",a-b)
 a = int(input("Enter the first value: "))     #to make it to int type
 b = int(input("Enter the second value:"))     #to make it to int type
 subtract(a,b)

 def multipy(a,b):
 # multiply function
     print("The Product of a & b is : ",a*b)
 a = int(input("Enter the first value: "))     #to make it to int type
 b = int(input("Enter the second value:"))     #to make it to int type
 multipy(a,b)

 def divide(a,b):
 # divide function
     if b == 0:
         print("Can't divide by 0")
     else:
         print("The Quotient of a & b is : ",a/b)
 a = int(input("Enter the first value: "))     #to make it to int type
 b = int(input("Enter the second value:"))     #to make it to int type
 divide(a,b)

# A list in Python is an ordered collection of items.
# It an store different data types together (numbers, strings, even other lists).
# It can change (mutable).
my_Subjects = ["Mathematics","ML","Programming Practices","Image & Video Processing","Research Methodology"]
for subject in my_Subjects:
    print(subject)            #prints all the List at once one after the other

my_Subjects.append("Python")      #appends python at the end of the list
my_Subjects.insert(2,"DSA")       #inserts DSA at the index 2
for subject in my_Subjects:
    print(subject)

my_Subjects.remove("ML")          #removes the value "ML"
deleted_subject = my_Subjects.pop(2)  #deletes value at index 2 and returns the value to deleted subject
print(deleted_subject)
for subject in my_Subjects:
    print(subject)

del my_Subjects[0]               #deletes the value at index 0 and doesnt return the value at all
for subject in my_Subjects:
    print(subject)

print(len(my_Subjects))         #prints the no. of items in the list

my_Subjects.sort()                #sorts the list in aplphabetical order

#if we want to sort the list but dont wanna change the original list then use Sorted()
sorted_my_subjects = sorted(my_Subjects)      #here the original list remains the same and one new list is created which is sorted

#if we want to sort in reverse
my_Subjects.sort(reverse=True)        #sorts the list in reverse order



