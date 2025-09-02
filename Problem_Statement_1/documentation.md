Problem Understanding

Level 1:
Build an encryption system using a Keyword Caesar Cipher (where shifts are based on letters of a keyword) and then add Base64 encoding for extra security.

Level 2:
Break a Caesar cipher message when the shift is unknown by using letter frequency analysis and automatically finding the most likely decryption.

Key Concepts Involved

Caesar Cipher & Keyword Caesar Cipher

Base64 encoding/decoding

Letter frequency in English

Chi-squared statistical test

Brute-force search

My Approach

Level 1:

Converted each keyword letter to a shift value.

Repeated keyword shifts over the message for encryption/decryption.

Added Base64 to disguise the output further.

Level 2:

Tried all 25 possible shifts.

Counted letter frequencies in each result.

Used chi-squared scoring to check how close the text was to English.

Picked the result with the lowest score as the best decryption.

Conceptual Learning

New Concepts I Discovered

Keyword Caesar Cipher: Stronger than a normal Caesar cipher since shifts vary with a keyword.

Base64 Encoding: Converts text into ASCII format, often used in emails and web data transfer.

Chi-Squared Test: A way to compare observed vs expected data distributions.

Letter Frequency Analysis: Exploiting the natural distribution of English letters to break ciphers.

How I Applied These Concepts

Used keyword-based shifting with Base64 for encryption/decryption (Level 1).

Applied chi-squared + letter frequency matching to detect the correct Caesar shift (Level 2).

Real-World Connections

Encryption: Shows how combining methods (like Caesar + Base64) makes text harder to decode.

Cryptanalysis: Demonstrates why frequency analysis can easily break simple classical ciphers.

Cybersecurity Awareness: Explains why modern cryptography is needed instead of weak ciphers.

Data Handling: Base64 is still widely used for safe transmission of text, images, and files.
