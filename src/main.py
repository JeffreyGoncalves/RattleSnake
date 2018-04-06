# Copyright : Morgan FEURTE and Jeffrey GONCALVES © 2018
# main.py : Super chatbot with 3 modes

import backchannels
import psychiatrist as psy
import mean_bot

def analyseMessage(message):
	print("Henlo, y did u say dis : " + message)
	return "action"

def psychiatrist():
	print("Psychiatrist !")
	return

def free_mode():
	print("Free mode !")

	while(1):
		# Read input from user
		message = input("Talk 2 m e!\n")
		
		if(message == "exit"):
			print("Goodby my fren")
			break
		else:
			action = analyseMessage(message)
			if (action == "TALK"):
				print("I talked !")

if __name__=="__main__":

	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('chatbot_mode')
	parser.add_argument('vaporwave_or_not')
	args = parser.parse_args()

	mode = args.chatbot_mode
	if(not (mode == '1' or mode == '2' or mode == '3')):
		print("Error : wrong mode, choose between 1 and 3 !")
	else:
		print("Mode : " + mode)

		if(mode == '1'):
			backchannels.execute()
		elif(mode == '2'):
			psy.execute()
		else:
			mean_bot.execute(args.vaporwave_or_not)
		
