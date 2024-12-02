def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)
previous_numbers = [1, 1]  
while True:
    random_number = sum(previous_numbers)  
    correct_answer = fizz_buzz(random_number)
    
    user_guess = input(f"What do you think the output for {random_number} is? (Fizz, Buzz, Fizz Buzz, or the number): ").lower()
    if user_guess == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect! The correct answer was {correct_answer}.")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break
    previous_numbers = [previous_numbers[1], random_number]
