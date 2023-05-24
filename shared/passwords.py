import json

from shared.load_save_data import save_data


# Location (path) and name of the passwords data file.
passwords_file = "/Users/jussisuominen2/Desktop/Ohjelmointi/Python/password-manager/data/passwords"


class Passwords:
    def __init__(self, encryption_helper):
        self.encryption_helper = encryption_helper
        # Load passwords from file. Password data is stored in encrypted JSON format so
        # it needs to be decrypted first. After decrypted it needs to be parsed with
        # json.loads method.
        self.passwords = json.loads(self.encryption_helper.decrypt_file(passwords_file))

    def add_password(self, name: str, username: str, password: str):
        new_password = { "name": name, "username": username, "password": password }

        self.passwords.append(new_password)

        passwords_json = json.dumps(self.passwords)

        encrypted_passwords = self.encryption_helper.encrypt_data(passwords_json).decode()

        save_data(encrypted_passwords, passwords_file)