def encrypt_caesar (plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    alphabets_in_lowercase = []
    alphabets_in_uppercase = []
    for i in range(65, 91):
        alphabets_in_uppercase.append(chr(i))
    alph_in_uppercase = (alphabets_in_uppercase)
    alph_in_upper = ''.join(alph_in_uppercase)
    t = len(alph_in_upper)
    print (alph_in_upper)
    for i in range(97, 123):
        alphabets_in_lowercase.append(chr(i))
    alph_in_lowercase = (alphabets_in_lowercase)
    alph_in_lower = ''.join(alph_in_lowercase)
    k = len(alph_in_lower)
    print (alph_in_lower)
    new_place: int = 0
    place: int = 0
    for i in plaintext:
        place = (alph_in_upper.find(i))
        if place in range(0, t):
            new_place = place + shift
            if new_place >= t:
                new_place = new_place - t
            if i in alph_in_upper:
                ciphertext += alph_in_upper[new_place]
    
        else: 
            place = (alph_in_lower.find(i))
            if place in range(0, k):
                new_place = place + shift
                if new_place >= k:
                    new_place = new_place - k
                if i in alph_in_lower:
                    ciphertext += alph_in_lower[new_place]
    print (ciphertext)
    return ciphertext
print (encrypt_caesar("Hello*"))
                        
def decrypt_caesar (ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    alphabets_in_lowercase = []
    alphabets_in_uppercase = []
    for i in range(65, 91):
        alphabets_in_uppercase.append(chr(i))
    alph_in_uppercase = (alphabets_in_uppercase)
    alph_in_upper = ''.join(alph_in_uppercase)
    t = len(alph_in_upper)
    print (alph_in_upper)
    for i in range (97, 123):
        alphabets_in_lowercase.append(chr(i))
    alph_in_lowercase = (alphabets_in_lowercase)
    alph_in_lower = ''.join(alph_in_lowercase)
    k = len(alph_in_lower)
    print (alph_in_lower)
    place: int = 0
    new_place: int = 0
    for i in ciphertext:
        place = (alph_in_upper.find(i))
        if place in range(0, t):
            new_place = place - shift
            if new_place < 0:
                new_place = new_place + t
            if i in alph_in_upper:
                plaintext += alph_in_upper[new_place]
                
        else:
            place = (alph_in_lower.find(i))
            if place in range(0, k):
                new_place = place - shift
                if new_place < 0:
                    new_place = new_place + k
                if i in alph_in_lower:
                    plaintext += alph_in_lower[new_place]
    print (plaintext)
    return plaintext
print (decrypt_caesar("Khoor*"))
