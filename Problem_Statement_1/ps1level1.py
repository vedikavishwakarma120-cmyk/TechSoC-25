def caesar_cipher(message, shift, mode):
    result = ""
    
    # reverse shift if decrypting
    if mode == "decrypt":
        shift = -shift
    
    for ch in message:
        if ch.isalpha():
            if ch.isupper():
                pos = ord(ch) - ord('A')
                new_pos = (pos + shift) % 26
                result += chr(new_pos + ord('A'))
            else:
                pos = ord(ch) - ord('a')
                new_pos = (pos + shift) % 26
                result += chr(new_pos + ord('a'))
        else:
            # keep non-letters the same
            result += ch
    return result


# main program
text = input("Enter message: ")
s = int(input("Enter shift: "))
m = input("Encrypt or Decrypt? ").lower()

output = caesar_cipher(text, s, m)
print("Result:", output)
