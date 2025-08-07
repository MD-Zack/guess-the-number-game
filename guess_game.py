# import random 

# print("Welcome its a Guessing game between 1-100 which number is right (O _ O)?\n")
# random_number = random.randint(1 , 100)#generate random number between 0-100

# print("\n")
# print(random_number)
# print("\n")

# user_attempt =int(input(f"how many try do u think need to get the right answer? :"))

# user_input_number =int(input("Enter your First Guess number : "))#get user guessed number


# if user_input_number == random_number :
#     print("You guess right. \n")

  
# while user_input_number != random_number:
    
#     user_attempt = user_attempt 

#     second_chance = int(input(f"You guess Wrong try again ,enter your {user_attempt} guess : \n"))
    
#     print(f"computer number is {random_number}")

#     if user_attempt == 1 and user_input_number != second_chance:

#         print(f"computer number is {random_number} you lose.")

#         break
        


#     elif second_chance > random_number :

#         user_attempt = user_attempt - 1 

#         print(f"your input number is {second_chance} but its too high . you have {user_attempt} attempt left. ")
        
        
#     elif second_chance < random_number :

#         user_attempt = user_attempt -1

#         print(f"your input number is {second_chance} but its too low . you have {user_attempt} attempt left. ")

    
#     elif second_chance == random_number :
#         print(f"your input number is {second_chance} congratulation you guess it right .you have done it in  {user_attempt} try not bad .\n")
#         break
    
#     else:
#         print("u hit it in first try .WOW")   
    
import random 

print("Welcome its a Guessing game between 1-100 which number is right (O _ O)?\n")
random_number = random.randint(1 , 100)#generate random number between 0-100

print(random_number)
print("\n")

user_is_guessed_right = 0

number_of_try = int(input("in how many try you think you can guess the number : "))

while number_of_try > 0 :
    

    user_input_number = int(input("enter your guess number : "))


    if user_input_number == random_number :
        print(f"congratulation the number is {user_input_number}")
        break
    

    elif user_input_number > random_number :
        print(f"your number {user_input_number} is greater than computer number and total {number_of_try-1} try remain.")
        number_of_try -=1
        

    elif user_input_number < random_number:
        print(f"your number {user_input_number} is lesser than computer number and total {number_of_try-1} try remain.")
        number_of_try -=1
    
    else:
        print("Finished")
    
if number_of_try == 0:
        
        print(f"\n You lost! The correct number was {random_number}. Better luck next time!")
    


    

            



            


