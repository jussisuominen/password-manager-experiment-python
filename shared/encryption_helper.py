from cryptography.fernet import Fernet

from shared.load_save_data import load_data
# Master password for testing: k7PW_

class EncryptionHelper:
    def __init__(self, master_password):
        encryption_key_base = "k7PW_PrNEzCTkvUQou6ZdnZaZUQJAuhyyp9E6ZyavkY="
        encryption_key_end = encryption_key_base[len(master_password):]
        encryption_key_string = master_password + encryption_key_end
        encryption_key = encryption_key_string.encode()
        self.fernet = Fernet(encryption_key)
    
    def encrypt_data(self, data):
        encrypted_data = self.fernet.encrypt(data.encode())
        return encrypted_data
    
    def decrypt_data(self, data):
        decrypted_data = self.fernet.decrypt(data)
        
        return decrypted_data.decode()
    
    def decrypt_file(self, filename):
        encrypted_data = load_data(filename)
        return self.decrypt_data(encrypted_data)
    
# Testing EncryptionHelper
# encryption_helper = EncryptionHelper("SebastianTynkkynen")
#encrypted_data_string = "gAAAAABkW2d_jQ-yvT266WC_0E2AjXU5WUC5WNswR6R1rQWn842lskpLa-t6TELbIfqdCH_uo1zFBAVAPjHyhh2xA2SyqLekzQ=="
#encrypted_data = encrypted_data_string.encode()
#print(encrypted_data)
#print(encryption_helper.decrypt_data(encrypted_data))
# encrypted_data = encryption_helper.encrypt_data("test")
# print(encrypted_data)
# print(encryption_helper.decrypt_data(encrypted_data))