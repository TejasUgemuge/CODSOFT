import random

def get_computer_choice():
    """Randomly select rock, paper, or scissors for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the user's and computer's choices."""
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, computer_choice, winner):
    """Display the result of the round."""
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You win!")
    else:
        print("You lose!")

def play_game():
    """Play the Rock-Paper-Scissors game."""
    user_score = 0
    computer_score = 0
    play_again = True

    while play_again:
        print("\nChoose rock, paper, or scissors:")
        user_choice = input("Your choice: ").lower()
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose again.")
            continue
        
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        
        display_result(user_choice, computer_choice, winner)
        
        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1
        
        print(f"\nScores: You - {user_score}, Computer - {computer_score}")
        
        play_again_input = input("Do you want to play again? (y/n): ").lower()
        play_again = play_again_input == 'y'
    
    print("\nThanks for playing! Final Scores:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")

if __name__ == '__main__':
    play_game()
