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
    


    

            



            


