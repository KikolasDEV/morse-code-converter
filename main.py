'''
You will use what you've learnt to create a text-based (command line) program that takes any String input and converts it into Morse Code.
https://en.wikipedia.org/wiki/Morse_code
'''

morse_code = {'A': '.-', 'B': '-...', 'C': '–.–.', 'D': '–..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'Ñ': '--.--', 'O': '---',
              'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.-', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
              '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--'}

def convert_sentence(input_text):

    morse_sentence = ""
    for letter in input_text:
        if letter.upper() in morse_code:
            morse_sentence += morse_code[letter.upper()]
        elif letter == " ":
            morse_sentence += " "

    return morse_sentence


text_input = input("Introduzca el texto que desea convertir a Codigo Morse: ")
final_result = convert_sentence(text_input)
print(f"El texto traducido a Codigo Morse es el siguiente: {final_result}")