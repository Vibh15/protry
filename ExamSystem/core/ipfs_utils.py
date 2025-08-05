import ipfshttpclient
from cryptography.fernet import Fernet

KEY = Fernet.generate_key()  # 🔐 You can replace this with a securely stored key
cipher_suite = Fernet(KEY)

def encrypt_and_upload_to_ipfs(file_data):
    encrypted_data = cipher_suite.encrypt(file_data)
    client = ipfshttpclient.connect()
    res = client.add_bytes(encrypted_data)
    return res  # 🧩 This is the IPFS hash (CID)

def download_and_decrypt_from_ipfs(ipfs_hash):
    client = ipfshttpclient.connect()
    encrypted_data = client.cat(ipfs_hash)
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data
