def encrypt_vigenere (plaintext: str, keyword: str) -> str:
    ciphertext = ""
    alphabets_in_lowercase = []
    alphabets_in_uppercase = []
    for i in range(65, 91):
        alphabets_in_uppercase.append(chr(i))
    alph_in_uppercase = (alphabets_in_uppercase)
    alph_in_upper = ''.join(alph_in_uppercase)
    t = len(alph_in_upper)
    for i in range(97, 123):
        alphabets_in_lowercase.append(chr(i))
    alph_in_lowercase = (alphabets_in_lowercase)
    alph_in_lower = ''.join(alph_in_lowercase)
    k = len(alph_in_lower)
    place: int = 0
    new_place: int = 0
    g = len(plaintext)
    p = len(keyword)
    if g > p:
        keyword = keyword + keyword
        p = len(keyword)
    for i in range(0, g):
        place = (alph_in_upper.find(plaintext[i]))
        if place in range(0, t):
            new_place = (place + alph_in_upper.find(keyword[i])) % 26
            if new_place > t:
                new_place = new_place - t
            if plaintext[i] in alph_in_upper:
                ciphertext += alph_in_upper[new_place]
        
        else:
            place = (alph_in_lower.find(plaintext[i]))
            if place in range(0, k):
                new_place = (place + alph_in_lower.find(keyword[i])) % 26
                if new_place > k:
                    new_place = new_place - k
                if plaintext[i] in alph_in_lower:
                    ciphertext += alph_in_lower[new_place]
            else:
                ciphertext += plaintext[i]
    print (ciphertext)
    return ciphertext
print (encrypt_vigenere("Hello*", "key"))

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    alphabets_in_lowercase = []
    alphabets_in_uppercase = []
    for i in range(65, 93):
        alphabets_in_uppercase.append(chr(i))
    alph_in_uppercase = (alphabets_in_uppercase)
    alph_in_upper = ''.join(alph_in_uppercase)
    for i in range(97, 123):
        alphabets_in_lowercase.append(chr(i))
    alph_in_lowercase = (alphabets_in_lowercase)
    alph_in_lower = ''.join(alph_in_lowercase)
    t = len(alph_in_upper)
    k = len(alph_in_lower)
    place: int = 0
    new_place: int = 0
    g = len(ciphertext)
    p = len(keyword)
    if g > p:
        keyword = keyword + keyword
        p = len(keyword)
    for i in range(0, g):
        place = (alph_in_upper.find(ciphertext[i]))
        if place in range(0, t):
            new_place = (place - alph_in_upper.find(keyword[i])) % 26
            if new_place < 0:
                new_place = new_place + t
            if ciphertext[i] in alph_in_upper:
                plaintext += alph_in_upper[new_place]
                
        else:
            place = (alph_in_lower.find(ciphertext[i]))
            if place in range(0, k):
                new_place = (place - alph_in_lower.find(keyword[i]))
                if new_place < 0:
                    new_place = new_place + k
                if ciphertext[i] in alph_in_lower:
                    plaintext += alph_in_lower[new_place]
            else:
                plaintext += ciphertext[i]
    print (plaintext)
    return plaintext
print (decrypt_vigenere("Gijvs*", "key"))
