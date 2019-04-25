# guessing game

import random

number = random.randint(1,10)

# while true keeps going forever until we quite
while True:
    user = int(input('What is your number: '))
       
    if user < number:
        print('too low')
    elif user > number:
        print('too high')
    else:
        print('YOU WIN!')
        play_again = input("do you want to play again? (y/n)? ")
        if play_again == 'y':
            number = random.randint(1,10)
            user = None
        else:
            print("Thank you for playing!")
            break









# 
# while True:
#     command = input('Type "exit" to exit: ')
#     if command == "exit":
#         break



# for x in range(1,10):
#     print(x)
#     print(x*x)
#
# for letter in 'coffee':
#     print(letter)
#     print(letter*10)

# x=0
# for num in range(11,20,2):
#     print(num)
#     x += num
#
# print(x)
#
# times = input("how many times do I have to tell you? ")
# message = "Clean your room!"
#
# for time in range(int(times)):
#     print(message)

# for num in range(1,21):
#     if num == 4 or num == 13:
#         print(f"{num} is unlucky")
#     elif num % 2 == 0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")

# for num in range(1, 21):
#     if num == 4 or num == 13:
#         state = "unlucky"
#     elif num % 2 == 0:
#         state = "even"
#     else:
#         state = "odd"
#     print(f"{num} is {state}")

# # for num in range(0,11):
# #     print("\u0001f600" * num)

# # row = 1
# # while row < 11:
# #     print("\u0001f600" * row)
# #     row += 1

# # for x in range(4):
# #     for num in range(0, 11):
# #         print("\u0001f600" * num)