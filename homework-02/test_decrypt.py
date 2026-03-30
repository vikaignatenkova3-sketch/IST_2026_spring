from vigenere import decrypt_vigenere

# Простой тест
test_text = "LXFOPVEFRNHR"
key = "LEMON"
result = decrypt_vigenere(test_text, key)
print(f"Тест: {test_text} + ключ {key} = {result}")

# Читаем cipher.txt
with open('cipher.txt', 'r', encoding='utf-8') as f:
    encrypted = f.read()

# Пробуем расшифровать ключом "secret"
decrypted = decrypt_vigenere(encrypted, "secret")
print("\nПервые 200 символов расшифровки:")
print(decrypted[:200])