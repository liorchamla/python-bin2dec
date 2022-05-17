import re

def ask_binary():
    binary = "111111111"

    while len(binary) > 8:
        binary = input("Quel est le binaire que vous voulez traduire (maximum 8 bits) ?\n")
        result = re.search("[^0-1]+", binary)

        if result != None:
            print("Ne mettez que des 0 et des 1 dans votre réponse !\n")
            binary = "111111111"

    return binary

def bin2dec(binary):
    position = len(binary) - 1;

    accumulator = 0;

    power = 0;

    while position >= 0:
        bit = binary[position];

        if bit == "1":
            accumulator += 2**power;
            

        position -= 1;
        power += 1;
    
    return accumulator