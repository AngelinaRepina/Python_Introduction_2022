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
for i in message: 
    place = alph.find(i)
    new_place = place + move
    if new_place >= t:
        new_place = new_place - t    
    if i in alph:
        result += alph[new_place]
    else:
        result += i
print (result)

message_to_decrypt = str(input("Enter your message to decrypt (in lowercase):"))
result_decr = ' '
for i in message_to_decrypt:
    place = alph.find(i)
    new_place = place - move
    if new_place < 0:
        new_place = new_place + t
    if i in alph:
        result_decr += alph[new_place]
    else:
        result_decr += i
print (result_decr)