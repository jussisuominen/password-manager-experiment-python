import sys
import os

import shared.master_password as master_password

from shared.debug import debug_message
from shared.passwords import Passwords
from shared.encryption_helper import EncryptionHelper

sys.path.append("./shared")

# Check if master password has been set
# if(master_password.master_password_is_set()):
#     # Master password has been set.
#     debug_message("Master password has been set!")

#     # Ask master password from user
#     master_password_input = input("Master password: ")

#     if(master_password.master_password_is_correct(master_password_input)):
#         print("Master password is correct!")
#     else:
#         print("Master password is incorrect!")
#         exit()
# else:
#     print("Master password has not been set!")
#     print("Please enter master password that you want to use!")

#     # Ask master password from user
#     master_password_input = input("Master password: ")

#     master_password.set_master_password(master_password_input)

# encryption_helper = EncryptionHelper(master_password_input)
encryption_helper = EncryptionHelper("test")
passwords_model = Passwords(encryption_helper)

show_menu(main_menu)