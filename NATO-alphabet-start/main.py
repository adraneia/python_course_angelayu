import csv

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

print("-----------------------------------------")
#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
#NATO_data_frame = pandas.DataFrame(nato_dict)
#print(NATO_data_frame)
#result = {new_key:new_value for (index, row) in df.iterrows()}
# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data["letter"])
# data_list = data["letter"].to_list()

nato_data_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data_df.iterrows()}
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("write a word: ").upper()
ouput_list = [nato_dict[letter] for letter in user_input]
print(ouput_list)

