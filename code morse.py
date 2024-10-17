MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': '/'
}
input_text = input("matn khod ra vared konid : ")
encrypted_text = ''
for char in input_text.upper():
    encrypted_text += MORSE_CODE_DICT[char] + ' '

print("matn shoma be code morse : ", encrypted_text)
morse_code = encrypted_text.strip()
words = morse_code.split(' ')
decipher = ''
for code in words:
    if code == '/':
        decipher += ' '
    elif code in MORSE_CODE_DICT.values():
        decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(code)]
    else:
        decipher += '?'

print("code morse ramz goshayei shode : ", decipher)