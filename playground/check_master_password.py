# Master password for testing is "test". Remember to change this password
# for production!

import sys
# This is used when hashing the master password.
import bcrypt

sys.path.append("../shared")

from master_password import master_password_file
from load_save_data import load_data
from debug import debug_message

# Ask master password from user
master_password_input = input("Master password: ")

# Load master password data from file.
master_password_data = load_data(master_password_file).split("\n")
# Extract hashed master password and salt from data. 
saved_hashed_master_password = master_password_data[0]
salt = master_password_data[1]

# Hash the master password input
hashed_master_password_input = bcrypt.hashpw(master_password_input.encode(), salt.encode())
hashed_master_password_input = hashed_master_password_input.decode()

debug_message(saved_hashed_master_password)
debug_message(hashed_master_password_input)

# Check if master password is correct.
if(saved_hashed_master_password == hashed_master_password_input):
    print("The master password is correct!")
else:
    print("The master password is incorrect!")