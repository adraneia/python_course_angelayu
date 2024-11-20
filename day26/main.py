names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
import random
student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)
#passed_students = {new_key:new_value for (key, value) in dictionary.items()}
passed_students = {student:score for (student, score) in student_scores.items() if score >=60}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
print(sentence.split())
result = {letters:len(letters) for letters in sentence.split() }
print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {days:int(weather_c[days])*9/5+32 for days in weather_c }
print(weather_f)



import pandas
student_dict = {
    "student2": ["Angela", "James", "Lily"],
    "score2": [56, 76, 98]
}
print("-------------Looping through dictionaries-------------------")
for (key,value) in student_dict.items():
  print(value)

student2_data_frame = pandas.DataFrame(student_dict)
print(student2_data_frame)

print("-------------loop through a data frame-------------------")
#loop through a data frame
for (key, value) in student2_data_frame.items():
    #the titles of each column
    print(key)
    #the data in each of the columns (its loopin through the name and then the scores in each column)
    print(value)

#pandas has an in built loop , its a method called itter rows , it allows us to loop through each of the rows rather than each of the columsn
print("-------------loop through a row of a data frame-------------------")
#loop through a row of a data frame
#index = number of each row
#row = we get hold of the data in a row
for (index, row) in student2_data_frame.iterrows():
    #each row has a student and a score
    #each row is a panda series object , that means we can tap into the row and then get hold of the value under particular column with . notaiton
    print(f"index:  {index}")
    print(f"row.student2:  {row.student2}" )
    print(f"row.score2: {row.score2}" )
    # if row.student2 == "Angela":
    #     print(row.score2)


#{new_key:new_value for (key,value) in dict.items()}
#{new_key:new_value for (index,row2) in df.iterrows()}

