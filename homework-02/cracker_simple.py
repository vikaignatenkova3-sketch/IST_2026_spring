from vigenere import decrypt_vigenere

with open('cipher.txt', 'r', encoding='utf-8') as f:
    encrypted = f.read()

print("Зашифрованный текст (первые 200 символов):")
print(encrypted[:200])
print()

key = "secret"
decrypted = decrypt_vigenere(encrypted, key)

print("Расшифрованный текст (первые 500 символов):")
print(decrypted[:500])
print()

with open('cracked.txt', 'w', encoding='utf-8') as f:
    f.write(decrypted)

print("Готово! Файл cracked.txt создан")