a = str(input("Enter your word to encrypt: "))
b = str(input("Enter your keyword: "))
t = len(a)
c = len(b)
result = ' '
if t > c:
    b = b + b 
    c = len(b)
alphabet_in_lowercase = []
for i in range(97,123):
    alphabet_in_lowercase.append(chr(i))
alphabet = (alphabet_in_lowercase)
alph = ''.join(alphabet)
h = len(alph)
for i in range(0, t):
    new_place = (alph.find(a[i]) + alph.find(b[i])) % 26
    if a[i] in alph:
        result += alph[new_place]
    else:
        result += a[i]
print (result)

r = str(input("Enter your kode to decrypt: "))
f = str(input("Enter keyword: "))
y = len(r)
p = len(f)
result_de = ' '
if y > p:
    f = f + f 
    p = len(f)
for i in range(0, y):
    new_place = (alph.find(r[i]) - alph.find(f[i])) % 26
    if r[i] in alph:
        result_de += alph[new_place]
    else:
        result_de += r[i]
print (result_de)