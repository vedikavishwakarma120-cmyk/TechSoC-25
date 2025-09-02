import string
from collections import Counter

# English letter frequencies (%)
ENGLISH_FREQ = {
    'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75,
    'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78,
    'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
    'P': 1.93, 'B': 1.49, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15,
    'Q': 0.10, 'Z': 0.07
}

def caesar_decrypt(text, shift):
    """Decrypt text using a Caesar cipher shift."""
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base - shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

def chi_squared_score(text):
    """Compare text letter frequencies with English using chi-squared test."""
    text = text.upper()
    counter = Counter(c for c in text if c in string.ascii_uppercase)
    total = sum(counter.values()) or 1
    
    score = 0
    for letter in string.ascii_uppercase:
        observed = (counter[letter] / total) * 100
        expected = ENGLISH_FREQ[letter]
        score += ((observed - expected) ** 2) / expected
    return score

def break_cipher(ciphertext):
    """Find the most likely shift and return decrypted text."""
    best_shift = None
    best_score = float('inf')
    best_text = ""
    
    for shift in range(1, 26):
        decrypted = caesar_decrypt(ciphertext, shift)
        score = chi_squared_score(decrypted)
        
        if score < best_score:
            best_score = score
            best_shift = shift
            best_text = decrypted
    
    return best_shift, best_text

# -------- Main Program --------
if __name__ == "__main__":
    cipher = input("Enter the encoded message: ")
    shift, decoded = break_cipher(cipher)
    
    print("\nMost likely result:")
    print(f"  Shift   : {shift}")
    print(f"  Message : {decoded}")
