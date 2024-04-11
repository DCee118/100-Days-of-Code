alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    if direction == 'decode':
            shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet [new_position]
        else:
            end_text += char
    print(f'The {cipher_direction} text is {end_text}') 
    
should_continue = True        
while should_continue:      
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    restart = input('Do you want to restart the cipher program? yes or no\n')
    if restart == 'no':
        should_continue = False
        from art import logo
        print(logo)
        print('Goodbye.')