key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',

'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',

'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',

'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',

'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',

'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',

'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

# Menu Function to decided either to encode/decode a message
def menu():
    print("1. Encode a string")
    print("2. Decode a string")
    print("3. Quit")
    choice = input("Enter your choice (1, 2, or 3): ")
    if(choice == '1'):
        encode()
    elif(choice == '2'):
        decode()
    elif(choice == '3'):
        print("Quitting the program...")
    else:
        print("Not a valid choice buddy!")
        menu()


# using the key array above, encrypts the given string in the input
def encode():
    plain = input("Enter (brief) text to encrypt: ")
    cipher = ""
    for letter in plain:
        if letter in key:
            cipher += key[letter]
        else:
            cipher += letter
    print(cipher)
    menu()

# also using the key array this decodes the given input :) 
def decode():
    cipher = input("Enter (brief) text to decrypt: ")
    plain = ""
    for letter in cipher:
        if letter in key:
            plain += key[letter]
        else:
            plain += letter
    print(plain)
    menu()

menu()
