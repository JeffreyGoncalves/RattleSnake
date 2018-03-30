def print_message(answer, mode):

	if(mode == 1):
		print("Ｊ４Ｆ４Ｒ－Ｂ0Ｔ >> " + transform_to_vaporwave(answer))
	elif(mode == 2):
		print("Ｄｒ．　ＭｏＧ~Ｂ0Ｔ >> " + transform_to_vaporwave(answer))
	else:
		print("Ｍｅａｎ_Ｂ0Ｔ >> " + transform_to_vaporwave(answer))
	print("")

def transform_to_vaporwave(message):
	vaporwave_lowercase_letters = ['ａ', 'ｂ', 'ｃ', 'ｄ', 'ｅ', 'ｆ', 'ｇ', 'ｈ', 'ｉ', 'ｊ', 'ｋ', 
									'ｌ', 'ｍ', 'ｎ', 'ｏ', 'ｐ', 'ｑ', 'ｒ', 'ｓ', 'ｔ', 'ｕ', 'ｖ', 
									'ｗ', 'ｘ', 'ｙ', 'ｚ']

	vaporwave_upercase_letters = ['Ａ', 'Ｂ', 'Ｃ', 'Ｄ', 'Ｅ', 'Ｆ', 'Ｇ', 'Ｈ', 'Ｉ', 'Ｊ', 'Ｋ', 
									'Ｌ', 'Ｍ', 'Ｎ', 'Ｏ', 'Ｐ', 'Ｑ', 'Ｒ', 'Ｓ', 'Ｔ', 'Ｕ', 'Ｖ', 
									'Ｗ', 'Ｘ', 'Ｙ', 'Ｚ']

	vaporwave_punctuation = ['．', '！', '？', '，', '　']

	new_message = ""
	for letter in message:
		ascii_code = ord(letter)

		if(ascii_code == 32):
			new_message += vaporwave_punctuation[4]
		elif(ascii_code == 33):
			new_message += vaporwave_punctuation[1]
		elif (ascii_code == 44):
			new_message += vaporwave_punctuation[3]
		elif (ascii_code == 46):
			new_message += vaporwave_punctuation[0]
		elif (ascii_code == 63):
			new_message += vaporwave_punctuation[2]
		else:
			if(ascii_code >= 97):
				new_message += vaporwave_lowercase_letters[ascii_code - 97]
			else:
				new_message += vaporwave_upercase_letters[ascii_code - 65]

	return new_message