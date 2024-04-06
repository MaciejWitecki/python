alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

def encrypt(plain_text, shift_amount):
    cipher_text = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position > 25:
            new_position = new_position % 26
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")


def decode(plain_text, shift_amount):
    cipher_text = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        if new_position < 0:
            new_position = 26 + new_position
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The decode text is {cipher_text}")

still = True
while still:
    
    if direction == 'encode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))  
        encrypt(plain_text=text, shift_amount=shift)
        still = False
    elif direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decode(plain_text=text, shift_amount=shift)
        still = False
    else:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
