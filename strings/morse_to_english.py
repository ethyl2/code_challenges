eng_to_morse = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '.': '.-.-.-', '?': '..--..', ',': '--..--', ' ': '/'
}

MORSE_CODE = dict(map(reversed, eng_to_morse.items()))


def decodeMorse(morse_code):
    words = morse_code.split('   ')
    output = []
    for word in words:
        translated_word = ''
        for char in word.split(' '):
            if char != '':
                translated_word += MORSE_CODE[char]
        output.append(translated_word)
    output_string = ' '.join(output)
    return output_string.strip().upper()


print(decodeMorse('.... . -.--   .--- ..- -.. .'))
