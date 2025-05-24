import unittest
from main import DataEncryptionStandard

class TestDataEncryptionStandard(unittest.TestCase):
    def setUp(self):
        self.des = DataEncryptionStandard()
        self.key = "abcdefgh"  # 8 chars = 64 bits
        self.plaintext = "testtest"  # 8 chars = 64 bits

    def test_encrypt_decrypt(self):
        # Encrypt the plaintext
        ciphertext = self.des.encrypt(self.plaintext, self.key)
        self.assertIsInstance(ciphertext, str)
        # Decrypt the ciphertext
        decrypted = self.des.decrypt(ciphertext)
        self.assertEqual(decrypted, self.plaintext)

    def test_encrypt_not_plaintext(self):
        ciphertext = self.des.encrypt(self.plaintext, self.key)
        self.assertNotEqual(ciphertext, self.plaintext)

    def test_different_keys(self):
        ciphertext1 = self.des.encrypt(self.plaintext, self.key)
        des2 = DataEncryptionStandard()
        ciphertext2 = des2.encrypt(self.plaintext, "12345678")
        self.assertNotEqual(ciphertext1, ciphertext2)

if __name__ == "__main__":
    unittest.main()
