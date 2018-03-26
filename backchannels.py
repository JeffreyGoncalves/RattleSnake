# Copyright : Morgan FEURTE and Jeffrey GONCALVES © 2018
# backchannels.py : First mode, responding with random keywords

import random
import utilities

def execute():
	last_backchannel = ""
	while(1):
		# Read input from user
		message = input("YOU :  ")
		
		if(message == "exit"):
			print("Goodby my fren")
			break
		else:
			answer = compute_answer(last_backchannel)
			last_backchannel = answer
			utilities.print_message(answer, 1)
	return


def compute_answer(last_backchannel):
	backchannels = ["Hmm ?", "I agree", "Oh ...", "Interesting !", "Tell me more about it"]
	# TODO : Find more backchannels  ?

	if(last_backchannel != ""):
		backchannels.remove(last_backchannel)

	return choose_random_backchannel(backchannels)


def choose_random_backchannel(backchannels_list):
	list_length = len(backchannels_list)

	position = random.randint(0, list_length - 1)

	return backchannels_list[position]