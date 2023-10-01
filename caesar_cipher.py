"""
    caesar-cipher
    Shift Cipher (k=3)
"""

class EncryptionSchemeInterface:
    """
    Cipher interface
    """
    def encrypt(self, message: str) -> str:
        """
            Cipher should implement encrypt function
        """

    def decrypt(self, encrypted_message: str) -> str:
        """
            Cipher should implement decrypt function
        """

class ShiftCipher(EncryptionSchemeInterface):
    """
    Shift Cipher with k=3, for 26-letter alphabet
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shift_count: int = 0
    def __init__(self, shift_count:int):
        self.shift_count = shift_count

    def shift(self, letter: str, shift:int):
        """
        Shifts a letter by a specified count
        """
        if letter == " ":
            return " "
        if letter.islower():
            shifted = ((ord(letter) - ord('a') + shift)
                       % len(self.alphabet)) + ord('a')
        else:
            shifted = ((ord(letter) - ord('A') + shift)
                       % len(self.alphabet)) + ord('A')
        return chr(shifted)
    def encrypt(self, message: str) -> str:
        """
        Encrypts a message shifting each letter by a given index
        """
        return ''.join([self.shift(letter, self.shift_count)
                        for letter in message])
    def decrypt(self, encrypted_message: str) -> str:
        """
        Decrypts a message shifting each letter back by a given index
        """
        return ''.join([self.shift(letter, -self.shift_count)
                        for letter in encrypted_message])

cipher = ShiftCipher(shift_count=3)
assert cipher.encrypt("ciao") == "fldr", "Should be 'fldr'"
assert cipher.decrypt("fldr") == "ciao", "Should be 'ciao'"
assert cipher.decrypt("BHV BRX PDGH LW"), "Should be 'Yes you made it'"
