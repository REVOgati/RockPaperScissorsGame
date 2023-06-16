import random #This helps the computer select pseudorandom choices as you play against it

#Game description and definition

    #Rock smashes scissors.
    #Paper covers rock.
    #Scissors cut paper.
while True: #Use of while to create a loop to ensdure user plays severally unless they want to exit game
    
    print("To exit game ; input 'stop' , to continue; input 'continue': \n")
    user_decision = input('contnue or stop?').lower()

    if user_decision == 'stop':
        print("Goodbye!")
        break

#First, define the choices
    possible_options= ['rock','paper','scissors'] #possible options to select from

    user_option= input("Select and enter pick one option from: 'rock', 'paper','scissors': ").lower()

    computer_option = random.choice(possible_options) #The computer selects a random choice

    #Use of elif statements to determine winner

    if user_option == computer_option:
        print(f'Both have picked{user_option} ,It is a draw!')
    elif user_option == 'rock':
        if computer_option == 'scissors':
            print(f"\n User_option = {user_option}, computer_option= {computer_option}.\n")
            print('rock smashes scissors, you win!')

        else:
            print(f"\n User_option = {user_option}, computer_option= {computer_option}.\n")
            print("You loose!")

    elif user_option == "scissors":
        if computer_option == "paper":
            print(f"\n User_option = {user_option}, computer_option= {computer_option}.\n")
            print('Scissors cut paper, you win!')
            
        else:
            print(f"\n User_option = {user_option}, computer_option= {computer_option}.\n")
            print("You loose!")

    elif user_option == "paper":
        if computer_option == "rock":
            print(f"\n User_option = {user_option}, computer_option= {computer_option}.\n")
            print('paper covers rock, you win!')

        else:
            print(f"\n User_option = {user_option}, computer_option= {computer_option}.\n")
            print("You loose!")

    else:
        print("please select an option from the choces given in the list",possible_options)





