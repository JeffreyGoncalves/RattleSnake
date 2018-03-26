# Copyright : Morgan FEUTRE and Jeffrey GONCALVES 2018
# Psychiatrist.py : the chatbot adopt a psychiatrist's behaviour

import random
import utilities

verbs = {
        "am" : "are",
        "was" : "were",
        
        
    }


def execute(mode):
	last_backchannel = ""
	while(1):
		# Read input from user
		message = input("YOU :  ")
		
		if(message == "exit"):
			print("Have a nice day !")
			break
		else:
			answer = be_or_not_to_be()
			last_backchannel = answer
			utilities.print_message(answer,mode)
	return


def be_or_not_to_be():

    print("Take a sit and talk me about yourself")
    


