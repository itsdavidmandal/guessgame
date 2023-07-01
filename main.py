import random

def generate_random_number():
  """
  This function generates a random number between 1 and 100.

  Returns:
    The random number.
  """

  return random.randint(1, 100)

def get_guess_from_user():
  """
  This function gets a guess from the user.

  Returns:
    The user's guess.
  """

  guess = int(input("Enter your guess: "))
  return guess

def check_guess(guess, random_number):
  """
  This function checks if the user's guess is correct.

  Args:
    guess: The user's guess.
    random_number: The random number.

  Returns:
    A boolean value indicating whether the guess is correct.
  """

  if guess == random_number:
    return True
  else:
    return False

def main():
  """
  This function is the main function of the game.
  """

  random_number = generate_random_number()
  while True:
    guess = get_guess_from_user()
    if check_guess(guess, random_number):
      print("You guessed the correct number!")
      break
    else:
      print("Incorrect guess. Try again.")

if __name__ == "__main__":
  main()
