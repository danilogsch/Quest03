import binascii
import unittest
from crackme import decrypt_aes_ecb


class TestAESDecryption(unittest.TestCase):

    def setUp(self):
        # Dados de teste padrão
        self.encrypted_message = (
            "a57fd9725fb53c53d5bd0b56185da50f70ab9baea5a43523b76c03e3eb989a20"
        )
        self.key = "thisisasecretkey"
        self.expected_message = (
            "Sistemas Embarcados"  # Obtido através do script "crackme.py"
        )

    def test_decrypt_aes_ecb_valid(self):
        """Teste básico de decodificação com chave e mensagem corretas."""
        decrypted_message = decrypt_aes_ecb(self.encrypted_message, self.key)
        self.assertEqual(
            decrypted_message,
            self.expected_message,
            "A mensagem decifrada não corresponde ao esperado.",
        )

    def test_decrypt_aes_ecb_with_incorrect_key(self):
        """Teste de decodificação com chave incorreta."""
        incorrect_key = "wrongsecretkeyyy"
        with self.assertRaises(
            ValueError, msg="A função deve lançar uma exceção para chave incorreta."
        ):
            decrypt_aes_ecb(self.encrypted_message, incorrect_key)

    def test_empty_ciphertext(self):
        """Teste com texto cifrado vazio."""
        decrypted_message = decrypt_aes_ecb("", self.key)
        self.assertEqual(
            decrypted_message,
            "",
            "A mensagem decifrada de um texto cifrado vazio deve ser vazia.",
        )

    def test_invalid_ciphertext_length(self):
        """Teste com comprimento inválido de texto cifrado (não múltiplo de 16)."""
        invalid_ciphertext = "a57fd9725f"  # Apenas 10 caracteres hexadecimais (5 bytes)
        with self.assertRaises(
            ValueError,
            msg="A função deve lançar uma exceção para texto cifrado com comprimento inválido.",
        ):
            decrypt_aes_ecb(invalid_ciphertext, self.key)

    def test_key_with_invalid_characters(self):
        """Teste com chave contendo caracteres inválidos."""
        key_with_special_chars = "thisis@secretkey"
        with self.assertRaises(
            ValueError,
            msg="A função deve lançar uma exceção para chave com caracteres inválidos.",
        ):
            decrypt_aes_ecb(self.encrypted_message, key_with_special_chars)

    def test_ciphertext_with_padding(self):
        """Teste de decodificação onde o texto decifrado possui padding no final."""
        # Supomos que o ciphertext_hex abaixo resulte em uma saída inválida de UTF-8
        encrypted_with_padding = "4a5c3d39b6d4e4e8b3f73f69f76e0b6f"  # Exemplo fictício
        with self.assertRaises(
            ValueError,
            msg="A função deve lançar uma exceção ao encontrar uma saída inválida de UTF-8.",
        ):
            decrypt_aes_ecb(encrypted_with_padding, self.key)

    def test_invalid_key_length(self):
        """Teste com chave de comprimento inválido."""
        with self.assertRaises(
            ValueError,
            msg="A função deve lançar uma exceção para chave de comprimento incorreto.",
        ):
            decrypt_aes_ecb(self.encrypted_message, "shortkey")  # Chave muito curta

    def test_invalid_ciphertext_format(self):
        """Teste com texto cifrado que não é hexadecimal."""
        with self.assertRaises(
            binascii.Error,
            msg="A função deve lançar uma exceção para texto cifrado com formato inválido.",
        ):
            decrypt_aes_ecb("nothexstring", self.key)  # Texto que não é hexadecimal


if __name__ == "__main__":
    unittest.main()
