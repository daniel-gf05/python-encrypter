from cryptography.fernet import Fernet

def generate_key() -> Fernet:
    key = Fernet.generate_key()
    print("key generated -> ", key)
    fKey = Fernet(key)
    save_key(key)
    return fKey

def encrypt_message(message, fKey: Fernet) -> bytes:
    token = fKey.encrypt(bytes(message.encode()))
    print("Message encrypted using key and stored in 'token' variable ->", token)
    return token
    
def decrypt_message(token: bytes) -> str:
    key = load_key()
    fKey = Fernet(key)
    return fKey.decrypt(token).decode()

def ask_user_message() -> any:
    message = input("Introduce the message to encrypt and decrypt: ")
    return message

# EXECUTE
def execute():
   fernetKey = generate_key()
   token = encrypt_message(ask_user_message(), fernetKey)
   message = decrypt_message(token)
   print("The decrypted message is:", message)
    
    
    
def save_key(key):
    key_file = open('secret.key', 'wb')
    if(key_file.write(key) <= 0):
        print("Error writing the file")
        return
        
    key_file.close()
    print("Key file has been generated successfully")
    
def load_key(file_loc="./"): 
    key_file = open('secret.key', 'rb')
    key = key_file.read()
    key_len = len(key)
    if(key_len <= 0):
        print("Error reading the file")
        return
    
    key_file.close()
    return key