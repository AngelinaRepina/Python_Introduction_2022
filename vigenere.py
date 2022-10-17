alphabet_in_lowercase = []
for i in range(97,123):
    alphabet_in_lowercase.append(chr(i))
alphabet = (alphabet_in_lowercase)
alph = ''.join(alphabet)
h = len(alph)
word_to_encrypt = str(input("Enter your word to encrypt: "))
keyword = str(input("Enter your keyword: "))
def encrypt_viegener (a = word_to_encrypt, b = keyword):
    t = len(a)
    c = len(b)
    result = ' '
    if t > c:
        b = b + b 
        c = len(b)
    for i in range(0, t):
        new_place = (alph.find(a[i]) + alph.find(b[i])) % 26
        if a[i] in alph:
            result += alph[new_place]
        else:
            result += a[i]
    print (result)
    return result
print (encrypt_viegener())

word_to_decrypt = str(input("Enter your kode to decrypt: "))
keywordd = str(input("Enter keyword: "))
def decrypt_viegener (r = word_to_decrypt, e = keywordd):
    y = len(r)
    p = len(e)
    result_de = ' '
    if y > p:
        e = e + e 
        p = len(e)
    for i in range(0, y):
        new_place = (alph.find(r[i]) - alph.find(e[i])) % 26
        if r[i] in alph:
            result_de += alph[new_place]
        else:
            result_de += r[i]
    print (result_de)
    return result_de
print (decrypt_viegener())
