import sys

# This is used when hashing the master password.
import bcrypt

sys.path.append("../shared")

from shared.master_password import master_password_file
from shared.load_save_data import save_data
from debug import debug_message

# Ask master password from user
master_password_input = input("Master password: ")

# Hash (encrypt) master password

# Adding the salt to password
salt = bcrypt.gensalt()

# Hashing the password
hashed = bcrypt.hashpw(master_password_input.encode(), salt)
hashed_string = hashed.decode()

debug_message(salt)
debug_message(hashed_string)

master_password_data = hashed_string + "\n" + salt.decode()

debug_message(master_password_data)

# Save hashed master password and salt to file.
save_data(master_password_data, master_password_file)