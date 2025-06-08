import string

# Function to simulate sending a message to the server
def send_message(message):
    print(message)

# Function to decrypt the XOR-encoded hash
def decrypt(hex_encoded, key):
    xored_bytes = bytes.fromhex(hex_encoded)
    decrypted_flag = ""
    for i in range(len(xored_bytes)):
        decrypted_flag += chr(xored_bytes[i] ^ ord(key[i % len(key)]))
    return decrypted_flag

# Main function to start the decoding process
def decode_hash():
    # Receive the encrypted hash from the user
    hex_encoded = input("Enter the encrypted hash (in hexadecimal): ").strip()

    # Receive the decryption key from the user
    key = input("Enter the decryption key: ").strip()

    # Decrypt the XOR-encoded hash using the provided key
    try:
        decrypted_flag = decrypt(hex_encoded, key)
        send_message("Decoded Flag: " + decrypted_flag)
    except Exception as e:
        send_message("Error during decryption: " + str(e))

# Execute the main function to start the decoding process
if __name__ == '__main__':
    decode_hash()
