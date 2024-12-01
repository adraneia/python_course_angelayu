#--------------------FieNotFound--------------------
# with open("a_file.txt") as file:
#     file.read()

#--------------------KeyError--------------------
# a_dictionary = {"key" : "value"}
# value = a_dictionary["non_existent_key"]

#--------------------IndexError--------------------
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

#--------------------TypeError--------------------
# text = "abc"
# print(text + 5)

#---------------------------------------------------------------------
#FileNotFound
# try:
#     file =  open("a_file.txt")
#     #keyError
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["dsadsa"])
# except:
#     #we want to make sure we succeed !!!
#     print("exception , there was an error!")
#     file =  open("a_file.txt", "w")
#     file.write("something")


# try:
#     file =  open("a_file.txt") # FileNotFound
#     a_dictionary = {"key": "value"} #keyError
#     #print(a_dictionary["dsadsa"])
#     print(a_dictionary["key"])
# except FileNotFoundError:     #we want to make sure we succeed !!!
#     print("FileNotFoundError")
#     file =  open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"the key {error_message} doesnt exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("file was closed!")
#
#     #raise KeyError("made up Key errorrrrr ;pppp")
#     #raise TypeError("made up Type errorrrrr ;pppp")

#---------------------------------------------------------------------

height = float(input("Height: "))
weight = float(input("Weight: "))

if height >3:
    raise ValueError("Human height shouldnt be over 3 meters !! ")


bmi = weight / height **2
print(bmi)



#-----------------coding exercise 20------------------------
# fruits = ["Apple", "Pear", "Orange"]
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
# make_pie(4)

#------------------coding exercise 21-----------------------
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
# def count_likes(posts):
#     total_likes = 0
#     for post in posts:
#         try:
#             total_likes = total_likes + post['Likes']
#         except KeyError as error_message:
#             print(error_message)
#     return total_likes
# count_likes(facebook_posts)