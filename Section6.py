"""
Created on Sat Dec 29 14:55:23 2018

@author: AsianDelight
"""

"""DICTIONARIES"""

# #keys can be numbers or strings, links can be anything else.

# cart = [{"name": "cat litter", "Quantity" : 3}]

# #2 ways to create a dictionary.
# cat = {'name' : 'blue', 'age' : 3.5, 'iscute' : True}
# print(cat)

# cat2 = dict(name = 'kitty', age = 0.5)
# print(cat2)

# #accessing indiviual values
# #key:value
# instructor = {
#     'name': 'colt',
#     'owns_dog': True,
#     'num_courses': 4,
#     'favorite_lanuage': 'Python'
# }


# #use a key to get the data out.
# print(instructor['name'])
# print(instructor['favorite_lanuage'])

# course = 'num_courses'
# print(instructor[course])

# artist = {
#     'first': 'neil',
#     'last': 'young'
# }

# full_name = f"{artist['first'].capitalize()} {artist['last'].capitalize()}"
# print(full_name)

# #get all values

# #loop through values

# #just values
# for value in instructor.values():
#     print(value)
# #just keys
# for key in instructor.keys():
#     print(key)
# #both keys and values
# for key,value in instructor.items():
#     print(f"Key is: {key} and value is: {value}")

# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

# total_donations = 0
# for v in donations.values():
#     print(str(v))
#     total_donations += v
# print(str(total_donations))

# total_donations2 = sum(donation for donation in donations.values())
# print(str(total_donations2))

# total_donations3 = sum(donations.values())
# print(str(total_donations3))

# #test for the existence for a key or value

# if 4 in instructor.values():
#     print('yes')

# #giving keys a default value
# new_user = {}.fromkeys(['name', 'score', 'email', 'profile bio'], 'unknown')
# print(new_user)

# #retrieves a key in an object an return none instead of error.

# print(instructor.get('name'))
# result = instructor.get('email')
# print(result)

# from random import choice #DON'T CHANGE!
# food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

# #DON'T CHANGE THIS DICTIONARY EITHER!
# bakery_stock = {
#     "almond croissant" : 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }

# print(food)
# if bakery_stock.get(food) != None:
#     print(f"{food}: {bakery_stock[food]} left")
# else:
#     print("We don't make that")


# game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"]

# initial_game_state = dict.fromkeys(game_properties, '0')
# print(initial_game_state)

# person = {'city': 'Auntigua'}
# person.update(instructor)
# print(person)
# person['name'] = "Evalia"
# print(person)


# inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}

# stock_list = inventory.copy()
# print(stock_list)
# stock_list['cookie'] = 18
# print(stock_list)
# stock_list.pop('cake')
# print(stock_list)

#Playlist modeling section 14, lecture 133
#dict with nested list with nested dict in list. {[{}]}

playlist = {
    'Title': 'patagonia bus',
    'author': 'Colt steele',
    'songs': [
        {'song_title': 'Turn It Off', 'artist': ['Blue'], 'duration': 2.5},
        {'song_title': 'song2', 'artist': ['kitty', 'djcat'], 'duration': 5.25},
        {'song_title': 'meowmeow', 'artist': ['garfield'], 'duration': 2.0}
    ]
}

total_length = 0
for song in playlist['songs']:
    total_length += song['duration']

print(total_length)

#Dictionary comperhension (DC)
instructor = {'name':"colt", 'city': 'san fran', 'color': 'purple'}
print(instructor)
yelling_instructor = {k.upper():v.upper() for k,v in instructor.items()}
print(yelling_instructor)

num_list = [1,2,3,4]
{num:('even' if num % 2 == 0 else "odd") for num in num_list}
print({num:('even' if num % 2 == 0 else "odd") for num in range(1,1000)})

yelling_instructor2 = {(k.upper() if k is 'color' else k):v.upper() for k,v in instructor.items()}
print(yelling_instructor2)

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[i]:list2[i] for i in range(0,3)}
print(answer)

answer2 = dict(zip(list1,list2))
print(answer2)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer3 = dict(person)
print(answer3)

answer4 = {}.fromkeys(['a', 'e', 'i', 'o', 'u'], 0)
print(answer4)

answer5 = {count: chr(count) for count in range(65,91)}
print(answer5)

"""LISTS"""

# instructors = []
# instructors.append('Colt')
# instructors.insert(1, "Blue")
# instructors.append('Lisa')
# print(instructors)
# print(instructors.index('Colt'))
# print(instructors.count("Blue"))
# print(instructors.count("noname"))
# if ValueError:
#     print("not in list!")


# #join takes a list and turns it into a string.
# print("I am friends with: ".join(instructors))

# print(instructors[1:])
# #grabs the string at index 1 and reverses the string in that index.
# print(instructors[1][::-1])


# names = ['James', 'Michelle']
# print(names[:])
# #swaps the values at the index ie 0 and 1
# names[0], names[1] = names[1], names[0]
# print(names[:])


# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# # list comperhension (LC)
# numbers = [1,2,3,4,5]
# print(numbers)
# doubles = [num * 2 for num in numbers]
# print(doubles)

# upper_case = [char.upper() for char in sounds]
# print(upper_case)

# strings_list = [str(num) for num in numbers]
# print(strings_list)

# #LC with conditional logic
# evens = [num for num in numbers if num % 2 == 0]
# odds = [num for num in numbers if num % 2 != 0]

# print(evens)
# print(odds)

# with_vowels = 'This is so much fun!'
# print(with_vowels)
# print(''.join(char for char in with_vowels if char not in "aeiou"))


# answer = ['Elie', 'Tim', 'Matt']
# answer2 = [1,2,3,4,5,6]

# print([person[0] for person in ["Elie", "Tim", "Matt"]])
# print([val for val in [1,2,3,4,5,6] if val % 2 == 0])

# #Nested Lists
# nested_lists = [[1,2,3], [4,5,6], [7,8,9]]
# print(nested_lists[-1][1])
# print(nested_lists[-1][-2])

# #outer list
# for l in nested_lists:
#     #inner list
#     for val in l:
#         print(val)


# #nested LC
# #inner list, then outer list; see above.
# [[print(val) for val in l] for l in nested_lists]

# #need more work on LC stuff.








# nums = list(range(1, 100))
# index = 0

# while index < len(nums):
#     print(f"{index}: {nums[index]}")
#     index +=1










# msg = input('say something: ')
# msg.lower()
# while msg != "stop copying me":
#     msg = input(f'{msg}\n')
# print("UGH FINE YOU WIN, BROTHER!")




"""Rock paper scissors"""

# player_1 = input('enter player 1 choice: \n')
# print('no cheating \n' *20)
# player_2 = input('enter player 2 choice: \n')

# if player_1 == 'rock':
#     if player_2 == "scissors":
#         print('player 1 wins!')
#     elif player_2 == 'paper':
#         print('player 2 wins')

# elif player_1 == "paper":
#     if player_2 == 'rock':
#         print('player 1 wins')
#     elif player_2 == "scissors":
#         print('player 2 wins')

# elif player_1 == 'scissors':
#     if player_2 == 'paper':
#         print('player 1 wins')
#     elif player_2 == 'rock':
#         print('player 2 wins')

# elif player_1 == player_2:
#     print('tie')
# else:
#     print('something is wrong')


"""Basic version"""
# if player_1 == "rock" and player_2 == 'paper':
#     print('player 2 wins')
# elif player_1 == 'rock' and player_2 == 'scissors':
#     print('player 1 wins')
# elif player_1 == 'paper' and player_2 == 'rock':
#     print('player 1 wins')
# elif player_1 == 'paper' and player_2 == "scissors":
#     print('player 2 wins')
# elif player_1 == 'scissors' and player_2 == 'rock':
#     print('player 2 wins')
# elif player_1 == 'scissors' and player_2 == 'paper':
#     print('player 1 wins')
# elif player_1 == player_2:
#     print('tie')
# else:
#     print('something is wrong')


# x = 12
# y = 19
# print(type(y))
#
# all, at, once = 5, 10, 55
#
# print(all)
# print(at)
# print(once)
#
# p = 99
# p += 1
# print(p)
#
# p -= 10
# print(p)
#
# p *= 2
# print(p)
#
# guess = 8
# print(f"you guess of {guess} was incorrect!")
# print(f"you guess of {guess + 1} was incorrect!")
#
# name = "chuck"
#
# print(name[3])
#
# print(name[-1])
#
# decimal = 12.56345934534
# integer = int(decimal)
#
# print(decimal)
# print(integer)

# # using truthiness
# age = input('how old are you? \n')
# if age:
#
#     if 18 <= int(age) < 21:
#         print('wristband - No drinks')
#     elif int(age) >= 21:
#         print('can drink!')
#     else:
#         print('no entry')
# else:
#     print('please enter an age')




# milage converter - KM to Miles

# input_message = "How many kilometers did you run today?"
# # print(input_message)
# kms = input(input_message)               #gets input from user and saves it in varable kms
# miles = float(kms)/1.60934
# print(f"OK, your {kms} km ride was {round(miles,2)} miles today!")
#
#
# age = 80
#
# if (age >= 2 and age <= 8) or age < 65:
#     print(str(age) + ' child')
# else:
#     print('senior')

# conditional statements

# number_1 = input('give me a number: \n')
# if 2 < int(number_1) < 10:
#     print('ok')
# else:
#     print('bad answer')
#
# if int(number_1) <= 35 or int(number_1) >100:
#     print('its under 35 or over 100')
# else:
#     print('bad answer')

