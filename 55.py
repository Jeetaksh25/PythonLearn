class BasicDSA:
    def Encryption(self):
        string = input("Enter a string: ")
        encrypted_string = ""
        for elem in string:
            if ord(elem) >= 97 and ord(elem) <= 122:  # Lowercase letters
                encrypted_char = self.EvenOddelem1(elem)
                encrypted_string += encrypted_char
            elif ord(elem) >= 65 and ord(elem) <= 90:  # Uppercase letters
                encrypted_char = self.EvenOddelem2(elem)
                encrypted_string += encrypted_char
            else:
                encrypted_string += elem  # Keep non-alphabetic characters unchanged
        print("Encrypted string:", encrypted_string)
        return encrypted_string
    
    def EvenOddelem1(self, char):
        # Lowercase encryption: add/subtract 7
        if ord(char) % 2 == 0:
            return chr(ord(char) + 7)
        else:
            return chr(ord(char) - 7)
        
    def EvenOddelem2(self, char):
        # Uppercase encryption: add/subtract 5
        if ord(char) % 2 == 0:
            return chr(ord(char) + 5)
        else:
            return chr(ord(char) - 5)
    
    def Decryption(self, string):
        decrypted_string = ""
        for elem in string:
            if ord(elem) >= 97 and ord(elem) <= 122:
                decrypted_string += self.EvenOddelem3(elem)
            elif ord(elem) >= 65 and ord(elem) <= 90:
                decrypted_string += self.EvenOddelem4(elem)
            else:
                decrypted_string += elem  # Keep non-alphabetic characters unchanged
        print("Decrypted string:", decrypted_string)
        return decrypted_string
    
    def EvenOddelem3(self, char):
        if ord(char) % 2 == 0:
            return chr(ord(char) - 7)  # Reverse operation for EvenOddelem1
        else:
            return chr(ord(char) + 7)  # Reverse operation for EvenOddelem1
    
    def EvenOddelem4(self, char):
        if ord(char) % 2 == 0:
            return chr(ord(char) - 5)  # Reverse operation for EvenOddelem2
        else:
            return chr(ord(char) + 5)  # Reverse operation for EvenOddelem2

# Main execution
obj = BasicDSA()
encrypted_text = obj.Encryption()
print("")

c1 = int(input("Enter 1 for decryption: "))
if c1 == 1:
    decrypted_text = obj.Decryption(encrypted_text)
    print("Decrypted string:", decrypted_text)
