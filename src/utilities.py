# Copyright : Morgan FEURTE and Jeffrey GONCALVES © 2018
# utilities.py : Utility functions used in all files

def print_message(answer, mode, vaporwave, mood = ""):
	if(vaporwave == "1"):
		if(mode == 1):
			print("Ｊ４Ｆ４Ｒ－Ｂ0Ｔ >> " + transform_to_vaporwave(answer))
		elif(mode == 2):
			print("Ｄｒ．ＭｏＧ~Ｂ0Ｔ >> " + transform_to_vaporwave(answer))
		else:
			print("Ｍｅ４ｎ_Ｂ0Ｔ " + mood + " >> " + transform_to_vaporwave(answer))
		print("")
	else:
		if(mode == 1):
			print("Ｊ４Ｆ４Ｒ－Ｂ0Ｔ >> " + answer)
		elif(mode == 2):
			print("Ｄｒ．ＭｏＧ~Ｂ0Ｔ >> " + answer)
		else:
			print("Ｍｅ４ｎ_Ｂ0Ｔ " + mood + " >> " + answer)
		print("")

def transform_to_vaporwave(message):
	vaporwave_lowercase_letters = ['ａ', 'ｂ', 'ｃ', 'ｄ', 'ｅ', 'ｆ', 'ｇ', 'ｈ', 'ｉ', 'ｊ', 'ｋ', 
									'ｌ', 'ｍ', 'ｎ', 'ｏ', 'ｐ', 'ｑ', 'ｒ', 'ｓ', 'ｔ', 'ｕ', 'ｖ', 
									'ｗ', 'ｘ', 'ｙ', 'ｚ']

	vaporwave_upercase_letters = ['Ａ', 'Ｂ', 'Ｃ', 'Ｄ', 'Ｅ', 'Ｆ', 'Ｇ', 'Ｈ', 'Ｉ', 'Ｊ', 'Ｋ', 
									'Ｌ', 'Ｍ', 'Ｎ', 'Ｏ', 'Ｐ', 'Ｑ', 'Ｒ', 'Ｓ', 'Ｔ', 'Ｕ', 'Ｖ', 
									'Ｗ', 'Ｘ', 'Ｙ', 'Ｚ']

	vaporwave_figures = ['０', '１', '２', '３', '４', '５', '６', '７', '８', '９']

	vaporwave_punctuation = ['．', '！', '？', '，', '　','"','（', '）', '－',
								"'", '：', '[', ']']

	new_message = ""
	for letter in message:
		ascii_code = ord(letter)

		if(ascii_code == 32):
			new_message += vaporwave_punctuation[4]
		elif(ascii_code == 33):
			new_message += vaporwave_punctuation[1]
		elif(ascii_code == 34):
			new_message += vaporwave_punctuation[5]
		elif(ascii_code == 39):
			new_message += vaporwave_punctuation[9]
		elif(ascii_code == 40):
			new_message += vaporwave_punctuation[6]
		elif(ascii_code == 41):
			new_message += vaporwave_punctuation[7]
		elif (ascii_code == 44):
			new_message += vaporwave_punctuation[3]
		elif (ascii_code == 45):
			new_message += vaporwave_punctuation[8]
		elif (ascii_code == 46):
			new_message += vaporwave_punctuation[0]
		elif (ascii_code == 58):
			new_message += vaporwave_punctuation[10]
		elif (ascii_code == 63):
			new_message += vaporwave_punctuation[2]
		elif (ascii_code == 91):
			new_message += vaporwave_punctuation[11]
		elif (ascii_code == 93):
			new_message += vaporwave_punctuation[12]
		else:
			if(ascii_code >= 97):
				new_message += vaporwave_lowercase_letters[ascii_code - 97]
			elif(ascii_code >= 65):
				new_message += vaporwave_upercase_letters[ascii_code - 65]
			elif(ascii_code <= 57 and ascii_code >= 48):
				new_message += vaporwave_figures[ascii_code - 58]

	return new_message


def getIndex(sub, psyOrMean):
# Gets the index of the subject given as parameter
    default = 5
    if(psyOrMean == "psychiatrist"):
    	subjects = ["family", "depression", "like", "dislike", "dream", "misunderstanding", 
    				"animals"]
    elif(psyOrMean == "mean"):
    	subjects = ["family", "depression", "animals", "dream",  "misunderstanding", 
    	  			"weather", "pain", "fruit", "vegetable", "bot"]
    i = 0
    for subject in subjects:
        if(subject == sub):
            return i
        i += 1

    return default  # should never happen