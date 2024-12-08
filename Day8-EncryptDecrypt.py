letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

output_string = ""
output_list = []
index_key = 5
index = 0

encrypt_text = ""
encrypt_list = []
encrypt_key = 0
encrypt_index = []
decrypt_list = []
decrypt_text = ""

def decrypt():
    encrypt_text = input('What phrase do you want to decrypt: ')
    encrypt_list = list(encrypt_text)
    encrypt_key = int(input("What is the Key Index: "))
    for i in range(len(encrypt_list)):
        encrypt_index.append(int(letters.index(encrypt_list[i]))-encrypt_key)
        decrypt_list.append(letters[encrypt_index[i]])
    decrypt_text = ''.join(decrypt_list)
    print(f'Your decrypted text is: {decrypt_text}')

def encrypt():
    origin_phrase = input("What is the phrase you would like to encrypt: ")
    list_phrase = list(origin_phrase)
    for i in range(len(list_phrase)):
        index = letters.index(origin_phrase[i])
        output_list.append(letters[(index + index_key) % len(letters)])
    output_string = ''.join(output_list)
    print(f'The phrase has been encrypted to: {output_string}'
          f'\nWith a Key Index of {index_key}')

def process():
    which = input("Would you like to encrypt or decrypt (E/D): ").lower()
    if which == "e":
        encrypt()
        contin = input("Would you like to continue (Y/N): ").lower()
        if contin == 'y':
            process()
        elif contin == 'n':
            exit()
        else:
            exit()
    elif which == "d":
        decrypt()
        contin = input("Would you like to continue (Y/N): ").lower()
        if contin == 'y':
            process()
        elif contin == 'n':
            exit()
        else:
            exit()
    else:
        exit()

process()