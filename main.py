morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'Ñ': '--.--', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.-', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--'
}


def conversion(input_text):

    morse_sentence = ""
    letters_line = ""

    for letter in input_text:
        if letter == " ":
            morse_sentence += "(space) "
            letters_line += "        "
        else:
            morse_char_code = morse_code.get(letter.upper(), "")
            morse_sentence += morse_char_code + " "
            letters_line += letter.upper() + " " * (len(morse_char_code) - 1) + " "

    dashes_line = ''.join(['_' if char != ' ' else ' ' for char in morse_sentence])

    return morse_sentence.strip(), dashes_line.strip(), letters_line.strip()

text_input = input("Introduzca el texto que desee convertir en Codigo Morse: ")
morse_result, dashes_result, letters_result = conversion(text_input)

print("############################################ MORSE CODE CONVERSION ############################################")
print(morse_result)
print(dashes_result)
print(letters_result)
