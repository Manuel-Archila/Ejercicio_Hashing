import hashlib

def sha1_hash(text):
    return hashlib.sha1(text.encode()).hexdigest()

with open('target_hashes.txt', 'r') as file:
    target_hashes = set(file.read().splitlines())

with open('words.txt', 'r') as file:
    dictionary_words = file.read().splitlines()

with open('realhuman_phill.txt', 'r', encoding='latin-1') as file:
    dictionary_words2 = file.read().splitlines()

cracked_passwords = {}

def try_decrypt(words):
    for word in words:
        for mutation in [word, word.capitalize(), word + '123', word.replace('a', '4').replace('e', '3')]:
            word_hash = sha1_hash(mutation)
            if word_hash in target_hashes and word_hash not in cracked_passwords:
                cracked_passwords[word_hash] = mutation
                print(f'Hash: {word_hash} - Password: {mutation}')

try_decrypt(dictionary_words)
try_decrypt(dictionary_words2)

if cracked_passwords:
    print("Contraseñas descifradas:")
    for hash, password in cracked_passwords.items():
        print(f'Hash: {hash} - Password: {password}')
else:
    print("No se descifraron contraseñas.")
