# Implement Caesar Cipher
The goal of this project is to develop a Python script capable of encoding and decoding text using the Caesar Cipher algorithm. Users will be able to input a message and a shift value, and the program will handle both encryption and decryption processes effortlessly.

## Explanation of the Project
The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet. For example, with a shift of 1, 'A' would be replaced by 'B', 'B' would become 'C', and so on. The decryption process reverses this shift.

## Key Components of the Project
### Input Handling:

Taking a message (plaintext) and a shift value from the user.
Providing an option to either encrypt or decrypt the message.
Encryption:

Shifting each letter in the plaintext by the given shift value to produce the ciphertext.
Decryption:

Shifting each letter in the ciphertext by the negative of the shift value to retrieve the original plaintext.
User Interface:

## Explanation of the Code
### Caesar Cipher Function:

The caesar_cipher function takes three parameters: text (the message to be processed), shift (the number of places to shift each letter), and mode (either "encrypt" or "decrypt").
The function iterates through each character in the input text, checks if it is an alphabet letter, and then shifts it according to the mode and shift value.
Non-alphabet characters are added to the result without modification.
User Interface:

## The GUI is created using Tkinter.
The user can input the message, shift value, and choose the mode (encrypt or decrypt).
The encrypt_decrypt function is called when the user clicks the "Submit" button, which processes the input using the caesar_cipher function and displays the result.
