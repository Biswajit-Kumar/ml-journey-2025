import pandas as pd
print("pandas version:", pd.__version__)    #printing version of pandas 

df = pd.read_csv('students.csv')
print(df.head(3))               #prints 1st 3 rows
print(df.shape)                  #prints (#rows,#cols) 
print(df.columns)                 #prints the column names 
print(df.columns.tolist())        #prints the column names as a list
print(df.info())                   #prints the basic info about the csv file like range of index, column names, non-null count, datatypes
#----- DATA ANALYSIS -----
print(df['Specialization'].count())   #no. of rows under specialization column
print(df['Specialization'].value_counts())   #prints the count of students by specialization
ml_specializations = df['ML' == df['Specialization']]         #filters out only ML specialized students into ml_spcializations
print(f"\nML Specialized students ({len(ml_specializations)} total):")        #finds the total no.of ML specialized students are there
print(ml_specializations[['Roll No.','Name']])      #prints only roll no & name column of ml_specialization students
print(ml_specializations)                          #prints every column
#to print all non-ml students just put != in place of ==
df['Year joined'] = 2025
print(df.head())

print("\n=== SAVING RESULTS ===")
ml_students = df[df['Specialization'] == 'ML'] 
ml_students.to_csv('ml_students_only.csv', index=False)
print("saved ml students to ml only csv file")

summary = df['Specialization'].value_counts()
summary.to_csv('Specialization_summary.csv', header=['Count'])
print("saved specialization summary into to specialization summary csv file.")

print("analysis done!")