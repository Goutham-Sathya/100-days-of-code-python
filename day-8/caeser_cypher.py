# caeser cypher program 


import art  # Import external module (assumes it contains 'logo')
print(art.logo)  

restart = "yes"  # Controls the loop for restarting the program

# List of lowercase alphabets used for shifting
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Caesar cipher function for encoding/decoding
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1  # Reverse shift for decoding

    for letter in original_text:
        # Preserve non-alphabet characters
        if letter not in alphabet:
            output_text += letter  
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)  
            output_text += alphabet[shifted_position]
    
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# Main loop for user input and function execution
while restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    
    restart = input("type yes to restart the process / type no to end the process.\n")
