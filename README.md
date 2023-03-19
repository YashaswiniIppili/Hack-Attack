# Hack-Attack
Chat Encryption Decryption Tool </br>

## Python  Implementation

Implementing on the same system : </br>
1. Git Clone the python_implementation folder (consists of 5 files) and install "pip install pycryptodome". </br>
2. Run encrypt.py, enter the user input. </br>
3. All 4 values (nonce, encryption key, tag and ciphertext) are copied onto a input.txt file. </br>
4. Run decrypt.py, you'll get the final decrypted plain text of the encrypted texts. </br>

Implementing on two systems (server & client) : </br>
1. Run encrypt.py on server side, enter the user input and then the corresponding 4 values are copied into input.txt
2. Run server.py, this sends the input.txt to the client side but make sure you put in the right port and ip address.
3. Run client.py on the server side to receive "input.txt", check your downloads section.
4. Run decrypt.py on the client side to get the plain text from the encrypted text.

## CPP Implementation 

1. Git Clone the python_implementation folder (consists of 5 files). </br>
2. Put all files into same directory for easiest running. </br>
3. Run encrypt.py and run server.cpp afterwards.</br>
4. Receive in a separate terminal or system by running client.py and after file which it will automatically come into directory and run decrypt.cpp </br>
