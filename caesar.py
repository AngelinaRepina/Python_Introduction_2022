move = 3
message = str(input("Enter your message to encrypt (in lowercase): "))
result = ' '
alphabets_in_lowercase=[]
for i in range(97,123):
    alphabets_in_lowercase.append(chr(i))
alphabet = (alphabets_in_lowercase)
alph = ''.join(alphabet)
t = len(alph)
print (alph)
def encrypt_caesar (plaintext = message, shift = move):
    result = ' '
    for i in plaintext: 
        place = alph.find(i)
        new_place = place + shift
        if new_place >= t:
            new_place = new_place - t    
        if i in alph:
            result += alph[new_place]
        else:
            result += i
    print (result)
    return result
print (encrypt_caesar())

message_to_decrypt = str(input("Enter your message to decrypt (in lowercase):"))
def decrypt_caesar (ciphertext = message_to_decrypt, shift = move):
    result_decr = ' '
    for i in ciphnertext:
        place = alph.find(i)
        new_place = place - shift
        if new_place < 0:
            new_place = new_place + t
        if i in alph:
            result_decr += alph[new_place]
        else:
            result_decr += i
    print (result_decr)
    return result_decr
print (decrypt_caesar())
