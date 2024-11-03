from Crypto.Cipher import AES
import binascii

def decrypt_aes_ecb(ciphertext_hex: str, key: str) -> str:
    """
    Decifra uma mensagem codificada com AES-128 em modo ECB.

    :param ciphertext_hex: Texto cifrado em hexadecimal.
    :param key: Chave de decodificação de 128 bits (16 caracteres).
    :return: Texto decifrado.
    """
    key_bytes = key.encode('utf-8')
    ciphertext_bytes = binascii.unhexlify(ciphertext_hex)

    cipher = AES.new(key_bytes, AES.MODE_ECB)

    # Decipher the message
    plaintext_bytes = cipher.decrypt(ciphertext_bytes)

    # Attempt to decode, with error handling for invalid UTF-8 sequences
    try:
        plaintext = plaintext_bytes.decode('utf-8').rstrip('\x00\r\n')
    except UnicodeDecodeError:
        raise ValueError("Decryption resulted in non-UTF-8 output, likely due to an incorrect key or corrupted ciphertext.")

    return plaintext


# Teste básico de decodificação
if __name__ == "__main__":
    encrypted_message = "a57fd9725fb53c53d5bd0b56185da50f70ab9baea5a43523b76c03e3eb989a20"
    key = "thisisasecretkey"
    decrypted_message = decrypt_aes_ecb(encrypted_message, key)
    print("Mensagem decifrada:", decrypted_message)