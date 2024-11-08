morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'Ñ': '--.--', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.-', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--'
}


def convert_sentence(input_text):
    morse_sentence = ""
    letters_line = ""
    for letter in input_text:
        if letter == " ":
            morse_sentence += "(space) "
            letters_line += "        "
        else:
            morse_code_char = morse_code.get(letter.upper(), "")
            morse_sentence += morse_code_char + " "
            letters_line += letter.upper() + " " * (len(morse_code_char) - 1) + " "

    dashes_line = ''.join(['-' if c != ' ' else ' ' for c in morse_sentence])

    return morse_sentence.strip(), dashes_line.strip(), letters_line.strip()


text_input = input("Introduzca el texto que desea convertir a Codigo Morse: ")
morse_result, dashes_result, letters_result = convert_sentence(text_input)

print(" ######################################## MORSE CODE CONVERSION ##############################################")
print(morse_result)
print(dashes_result)
print(letters_result)
