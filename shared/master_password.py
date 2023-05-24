import os.path
import sys

import bcrypt
from shared.debug import debug_message
from shared.load_save_data import load_data, save_data

sys.path.append("../shared")

# Location (path) and name of the master password data file.
master_password_file = "/Users/jussisuominen2/Desktop/Ohjelmointi/Python/password-manager/data/master_password"


# This function loads master password data (hashed master password and salt) from the data file
# (location and name defined above). If master password data can be loaded successfully from
# the data file this functions returns master password and salt in a dictionary
# ("hashed_master_password" and "salt" are the dictionary keys). If master
# password data can not be loaded from the file this function returns None.

# If this function returns None the caller knows that the master password is not
# set or there is problem loading the master password data.
def load_master_password_data():
    # Master password dictionary. This will contain hashed master password
    # (the key is "hashed")
    # Set the master password dictionary initially to None.
    master_password_dict = None

    # Try to load master password data from file.
    try:
        # Load master password data from file.
        master_password_data = load_data(master_password_file).split("\n")
        # Extract hashed master password and salt from data.
        saved_hashed_master_password = master_password_data[0]
        salt = master_password_data[1]
        master_password_dict = {
            "hashed_master_password": saved_hashed_master_password,
            "salt": salt}
    except:
        pass

    return master_password_dict


def master_password_is_correct(master_password):
    master_password_data = load_master_password_data()

    stored_hashed_master_password = master_password_data["hashed_master_password"]
    salt = master_password_data["salt"]

    debug_message(master_password_data)
    debug_message(stored_hashed_master_password)
    debug_message(salt)

    # Hash the master password that is given as an argument. hashpw method returns the hashed
    # password as bytes so we must decode it to string.
    hashed_master_password = bcrypt.hashpw(
        master_password.encode(), salt.encode()).decode()

    debug_message(hashed_master_password)

    if (stored_hashed_master_password == hashed_master_password):
        return True
    else:
        return False


# Returns True if master password is set (= master password data file is created)
# and False is it is not set (= master password data file is not created).
def master_password_is_set():
    return os.path.exists(master_password_file)

# This function sets master password. Beware! This function overwrites the
# previously created master password file if the file name and location are
# the same.
def set_master_password(master_password):
    # Hash (encrypt) master password

    # Adding the salt to password
    salt = bcrypt.gensalt()

    # Hashing the password
    hashed = bcrypt.hashpw(master_password.encode(), salt)
    hashed_string = hashed.decode()

    debug_message(salt)
    debug_message(hashed_string)

    master_password_data = hashed_string + "\n" + salt.decode()

    debug_message(master_password_data)

    # Save hashed master password and salt to file.
    save_data(master_password_data, master_password_file)


# Removes the master password data file (thus unsetting the master password)
def unset_master_password():
    os.remove(master_password_file)

# For testing the module functions.
if __name__ == "__main__":
    set_master_password("test")
    #print(master_password_is_correct("test"))
    #print(master_password_is_set())
