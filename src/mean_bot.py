# Copyright : Morgan FEURTE and Jeffrey GONCALVES © 2018
# mean_bot.py : Third mode, mean bot that does not like to be messed around with

################################################
#  Public Service Announcement :			   #
#  I am an independant bot who needs no human  #
################################################

import random
import utilities


def execute():
    last_answer = ""

    while(1):
        # Readinputfromuser
        message = input("ＹＯＵ >>  ")
        # message = re.sub('((?<![A-Z])[\.\?\!\:\,\;\"\(\)]+)', r" \1 ", message)

        answer, continue_answered_leave = check_politeness_formulas(message, last_answer)
        if(continue_answered_leave == 1):
            last_answer = answer
        if(continue_answered_leave == 0):
            count_word_occurences(message)
            answer = compute_answer(last_answer)
            last_answer = answer
        utilities.print_message(answer, 2)
        if(continue_answered_leave == 2):
            break

def compute_answer(last_answer):

    return