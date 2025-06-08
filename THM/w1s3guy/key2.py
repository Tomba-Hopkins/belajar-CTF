import string

def decrypt_flag(prefix_encrypted_hex, suffix_encrypted_hex):
    """
    Decrypts the encryption key used to encrypt the flag based on the given encrypted prefix and suffix.

    Args:
        prefix_encrypted_hex (str): Hexadecimal representation of the encrypted prefix.
        suffix_encrypted_hex (str): Hexadecimal representation of the encrypted suffix.

    Returns:
        str: The decrypted encryption key.
    """
    prefix_encrypted = bytes.fromhex(prefix_encrypted_hex)
    suffix_encrypted = bytes.fromhex(suffix_encrypted_hex)
    
    # Known constants
    prefix = "THM{"
    suffix = "}"
    
    # Length of the encryption key
    key_length = len(prefix)
    
    # Decrypt the prefix of the key
    key_prefix = []
    for i in range(key_length):
        key_prefix.append(prefix_encrypted[i] ^ ord(prefix[i]))
    
    # Decrypt the suffix of the key
    key_suffix = suffix_encrypted[0] ^ ord(suffix)
    
    # Convert to string
    key = ''.join(chr(k) for k in key_prefix) + chr(key_suffix)
    
    return key

if __name__ == "__main__":
    # Prompt for the encrypted hash input
    encrypted_hash = input("Enter the encrypted hash in hexadecimal: ").strip()
    
    # Extract encrypted prefix and suffix
    prefix_encrypted_hex = encrypted_hash[:len("THM{")*2]  # Convert to bytes
    suffix_encrypted_hex = encrypted_hash[-2:]  # Last byte for the suffix
    
    # Decrypt the key
    decrypted_key = decrypt_flag(prefix_encrypted_hex, suffix_encrypted_hex)
    
    print(f"The encryption key is: {decrypted_key}")
