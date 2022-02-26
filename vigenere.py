method = input("encrypt/decrypt(e/d): ")
text = input('enter text : ')
key = input('enter key : ')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in key:
    if len(text) != len(key):
        key += i
cipher = []
ciphertext = ''
if method == "e":
    for i in range(len(text)):
        if text[i].isupper():
            cipher.append((alphabet.find(text[i].lower()) + alphabet.find(key[i])) % len(alphabet))
            ciphertext += alphabet[cipher[i]].upper()
        elif text[i].islower():
            cipher.append((alphabet.find(text[i]) + alphabet.find(key[i])) % len(alphabet))
            ciphertext += alphabet[cipher[i]]
        else:
            ciphertext += text[i]
elif method == "d":
    for i in range(len(text)):
        if text[i].isupper():
            cipher.append((alphabet.find(text[i].lower()) - alphabet.find(key[i])) % len(alphabet))
            ciphertext += alphabet[cipher[i]].upper()
        elif text[i].islower():
            cipher.append((alphabet.find(text[i]) - alphabet.find(key[i])) % len(alphabet))
            ciphertext += alphabet[cipher[i]]
        else:
            ciphertext += text[i]
else:
    print("Please enter the correct method")
print("our result is ", ciphertext)
