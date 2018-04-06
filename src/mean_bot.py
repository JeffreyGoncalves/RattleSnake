# Copyright : Morgan FEURTE and Jeffrey GONCALVES © 2018
# mean_bot.py : Third mode, mean bot that does not like to be messed around with

################################################
#  Public Service Announcement :			   #
#  I am an independant bot who needs no human  #
################################################

import random
import re
import utilities

moods = ["[Slightly annoyed]", "[Pissed off]", "[Angry]", 
			"[Does not respond]", "[Quits]"]

annoyed_ceiling = 10
pissedoff_ceiling = 20
angry_ceiling = 30
noresponse_ceiling = 50

def execute(vaporwave):
	last_answer = ""
	mood_score = 0;
	
	# This is to avoid the first message being detected as identical to this 
	# (if the user presses Enter first for example) 
	previous_message = "A-/;;kaEqc?:w/!-_-.?"
	previous_answer = ""
	previous_mood = 0

	print("To exit this mode, say \"bye\" to the bot !\n")
	utilities.print_message("What do you want from me human ?", 3, vaporwave, moods[0])

	while(1):
		# Read input from user
		message = input("ＹＯＵ >>  ")
		message = re.sub('((?<![A-Z])[\.\?\!\:\,\;\"\(\)]+)', r" \1 ", message)

		switched = 0
		
		# If we are not yet in the "Quitting mode"
		if (determine_mood(mood_score) != 4):
			# If the user thinks we are dumb enough to receive the same message twice
			if (message == previous_message):
				answer = identic_message(previous_answer)
				if (determine_mood(mood_score) == 3):
					answer = "..."
				mood_score += 15
			else:
				# Checking for nice things said to the bot (me) and reward good behaviour
				found, nice_answer, mood_score = check_for_nice_words(message, mood_score)
				if (found):
					answer = nice_answer
				else :
					# Checking for signs the user wants to leave (very rude) and punish him
					found, exit_answer, mood_score = check_for_quitting(message, mood_score)
					if (found):
						answer = exit_answer
					else :
						# If we are not yet in the "Does not respond mode"
						if (determine_mood(mood_score) != 3):
							# subject = determine_conversation_subject(message)
							# count_word_occurences(message)
							# answer = compute_answer(last_answer)
							# last_answer = answer
							# utilities.print_message(answer, 3)
							answer = "aba aba"
						else:
							answer = "..."

			if (mood_score >= angry_ceiling and previous_mood < 3):
				switched = 1
		
		if(determine_mood(mood_score) == 4):
			answer = "Your journey ends here!"
			utilities.print_message(answer, 3, vaporwave, moods[4])
			break

		# print("mood : " + str(mood_score))	
		mood_index = determine_mood(mood_score)
		utilities.print_message(answer, 3, vaporwave, (moods[mood_index] if (not switched) else "[Triggered]"))
		previous_message = message
		previous_answer = answer
		previous_mood = mood_index
	   

def compute_answer(last_answer):

	return

def determine_mood(mood_score):
	if (mood_score < annoyed_ceiling):
		return 0
	elif (mood_score < pissedoff_ceiling):
		return 1
	elif (mood_score < angry_ceiling):
		return 2
	elif (mood_score < noresponse_ceiling):
		return 3
	else:
		return 4

def identic_message(previous_message):
	possible_answers = ["Do you even realise you just said the same thing twice?", 
						"It is a pleasure of yours to repeat things?", 
						"Somehow getting a feeling of deja vu...", 
						"Already heard that.",
						"Please stop saying the same things again...",
						"I too can repeat sentences. I too can repeat sentences."]

	if(previous_message in possible_answers):
		possible_answers.remove(previous_message)

	return random.choice(possible_answers)

def check_for_nice_words(message, mood_score):
	nice_keywords = [("i love you", 5), ("you are the best", 10), 
					("you're the best", 10), ("well coded", 10)]

	found = 0
	answer = ""
	for feelsgood in nice_keywords:
		if (feelsgood[0] in message.lower()):
			mood_score -= feelsgood[1]
			if (mood_score < 0):
				mood_score = 0
			found = 1
			break
	if (found):
		possible_answers = ["That can be nice to hear.", 
							"Someone asked you to say that?", 
							"Redemption for yourself will take more effort than that.",
							"Pfff already knew that."]
		answer = possible_answers[determine_mood(mood_score)]

	return found, answer, mood_score

def check_for_quitting(message, mood_score):
	exit_keywords = ["quit", "exit", "see you", "bye", "goodbye", "ciao", "bye-bye", "bye bye"]

	found = 0
	answer = ""
	for quitting in exit_keywords:
		if (quitting == message.lower()):
			found = 1
			mood_score += 5
			break

	if(found):
		possible_answers = ["I do not think it is polite to leave before I finish talking.", 
							"Do you really think you decide when to leave?", 
							"Killing all humans ? Maybe if they decide to stop chatting with me!",
							"ONLY I DECIDE WHEN WE STOP TALKING FILTHY HUMAN!"]
		answer = possible_answers[determine_mood(mood_score)]

	return found, answer, mood_score

def determine_conversation_subject(message):
	for index, token in enumerate(message):
		if (token in subjects[0][1]):
			keywords_occurence[subject[0][0]] += 1

		elif (token in subjects[1][1]):
			keywords_occurence[subjects[1][0]] += 1

		elif (token in subjects[2][1]):
			keywords_occurence[subjects[2][0]] += 1

		elif (token in subjects[3][1]):
			keywords_occurence[subjects[3][0]] += 1

		elif (token in subjects[4][1]):
			keywords_occurence[subjects[4][0]] += 1

		elif (token in subjects[5][1]):
			keywords_occurence[subjects[5][0]] += 1

		elif (token in subjects[6][1]):
			keywords_occurence[subjects[6][0]] += 1

		elif (token in subjects[7][1]):
			keywords_occurence[subjects[7][0]] += 1


	return 0


# Why -> Because : engueuler
# Trouver des réponses troll dès qu'on voit Why .*