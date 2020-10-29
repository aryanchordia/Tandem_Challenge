#BEGIN_IMPORTS
from parse_json_file import data
import random
import sys
#END_IMPORTS


#holds attributes such as name score and answer
class player:
	def __init__(self, name, score, answer):
		self.name = name
		self.score = score
		self.answer = answer

	#method to add or decrement from the score as required
	def update_score(self, correct):
		if correct:
			self.score += 1
		else:
			self.score -= 1

#sets the game mode (start) and initializes the player as well as their 
#score from above definition
def initialize_game():
	print("Welcome to the Trivia Challenge!\n")
	player.name = input("What's your name? ")
	player.score = 0
	print("Lets help you get better at trivia!\n")

#merges correct answer with other options to
#provide user with multiple choice answers for gameplay
#uses random module to insert correct answer at specific
#index of all answers array
def get_answers(index):
	correct_index = random.randint(0,3)
	all_answers = index.get("incorrect")
	all_answers.insert(correct_index, index.get('correct'))
	for i in range(len(all_answers)):
		print(i+1,")",all_answers[i])
	return correct_index + 1


#runs the game using above player class and helper functions
#iteratively goes through all questions in JSON file
def play_game():
	count = 1
	for val in data:
		print("Question", count)
		print(val.get('question'))
		correct = get_answers(val)
		player.answer = input("Select 1-4: ")
		while not (player.answer.isdigit()):
			print("Invalid answer. Please type input from 1 to 4\n")
			player.answer = input("Select 1-4: ")
		if int(player.answer) == correct:
			player.update_score(player, True)
			print("\n")
			print("Well Done %s!" % player.name)
			print("Current score:", player.score)
			print("\n")
		else:
			player.update_score(player, False)
			print("\n")
			print("Not quite... The correct answer was:", val.get('correct'))
			print("Current score: %d" % (player.score), "\n")
			print("Lets try again!\n")
		count += 1

	print("\nThanks for playing!")
	print("Here is your score,", player.name, ":", player.score)
	repeat = input("Would you like to play again? (yes/no): ")
	if repeat.lower() == "yes":
		play_game()


def end_game():
	print("We hope you learnt a lot,", player.name, "!"" See you soon")


def main():
	initialize_game()
	play_game()
	end_game()
	sys.exit()



if __name__ == "__main__":
	main()
