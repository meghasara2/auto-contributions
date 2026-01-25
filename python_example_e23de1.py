# Caesar Cipher Decoder - Learning Objective:
# This tutorial will teach you how to decode messages encrypted with the
# Caesar cipher. You'll learn about string manipulation, loops, conditional
# statements, and how to apply mathematical concepts to programming.
# We will focus on creating a function that takes an encrypted message and
# a shift value, and returns the original, decoded message.

def caesar_decode(encrypted_text, shift):
    """
    Decodes a message that has been encrypted using the Caesar cipher.

    The Caesar cipher is a simple substitution cipher where each letter in
    the plaintext is shifted a certain number of places down or up the alphabet.
    For example, with a shift of 3, 'A' would be replaced by 'D', 'B' by 'E', etc.
    To decode, we reverse this process by shifting letters back.

    Args:
        encrypted_text (str): The message that needs to be decoded.
        shift (int): The number of positions each letter was shifted during encryption.
                     This is the key to unlocking the message.

    Returns:
        str: The decoded (original) message.
    """
    decoded_message = ""  # Initialize an empty string to build our decoded message.

    # We need to iterate through each character in the encrypted text.
    # A 'for' loop is perfect for this, allowing us to process one character at a time.
    for char in encrypted_text:
        # First, let's check if the character is an alphabet letter.
        # Punctuation, spaces, and numbers should not be shifted,
        # as they are not part of the Caesar cipher encryption typically.
        if char.isalpha():
            # We need to determine if the letter is uppercase or lowercase,
            # because the shift logic is different for each case.
            # This ensures we preserve the original case of the letters.
            start = ord('A') if char.isupper() else ord('a')
            # ord() is a built-in Python function that returns the Unicode code point
            # of a character. For example, ord('A') is 65, ord('a') is 97.
            # This is crucial because we can perform mathematical operations on these numbers.

            # To decode, we need to shift *backwards*.
            # We find the position of the current character relative to its starting letter ('A' or 'a').
            # char_code = ord(char) - start
            # For decoding, we subtract the shift.
            # (ord(char) - start - shift)
            # However, we need to handle "wrapping around" the alphabet.
            # For example, if we decode 'A' with a shift of 3, we should get 'X', not go past 'A'.
            # The modulo operator (%) is our friend here. It gives us the remainder of a division.
            # By using (26) for the alphabet size, we ensure that if the result goes
            # below 0, it wraps around from the end of the alphabet.
            # For example, -1 % 26 is 25 (which corresponds to 'Z').
            # So, the new position is: (ord(char) - start - shift) % 26
            shifted_code = (ord(char) - start - shift) % 26

            # Now we convert this shifted numerical position back into a character.
            # We add the starting code point back to get the correct ASCII/Unicode value.
            # chr() is the inverse of ord() - it converts a Unicode code point back to a character.
            decoded_char = chr(start + shifted_code)

            # Append the decoded character to our result string.
            decoded_message += decoded_char
        else:
            # If the character is not a letter (e.g., space, punctuation),
            # we simply append it to the decoded message without modification.
            decoded_message += char

    # After processing all characters, return the complete decoded message.
    return decoded_message

# --- Example Usage ---

# Let's say we have a message that was encrypted with a shift of 3.
# This means 'A' became 'D', 'B' became 'E', and so on.
# To decode, we need to shift *back* by 3.

encrypted = "Khoor, Zruog!"
decryption_shift = 3

# Call our decoding function
original_message = caesar_decode(encrypted, decryption_shift)

# Print the results to see if it worked!
print(f"Encrypted message: {encrypted}")
print(f"Shift used for decryption: {decryption_shift}")
print(f"Decoded message: {original_message}")

print("\n--- Another Example ---")

# Let's try a different shift value.
# This message was encrypted by shifting letters forward by 5.
encrypted_2 = "Mjqqt, Btwqi!"
decryption_shift_2 = 5

original_message_2 = caesar_decode(encrypted_2, decryption_shift_2)

print(f"Encrypted message: {encrypted_2}")
print(f"Shift used for decryption: {decryption_shift_2}")
print(f"Decoded message: {original_message_2}")

print("\n--- Example with Wrapping ---")

# This message was encrypted with a shift of 4.
# Notice how 'X' was shifted to 'B', 'Y' to 'C', 'Z' to 'D'.
encrypted_3 = "Bydq, Fdhvdu!"
decryption_shift_3 = 4

original_message_3 = caesar_decode(encrypted_3, decryption_shift_3)

print(f"Encrypted message: {encrypted_3}")
print(f"Shift used for decryption: {decryption_shift_3}")
print(f"Decoded message: {original_message_3}")