#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3

# Imports
import getpass

from shared.passwords import Passwords
from shared.encryption_helper import EncryptionHelper
from shared.ui.command_line.menu_items import create_main_menu

# This class contains the main functionality of the Password Manager console
# application.
class PasswordManager:
    def __init__(self):
        # Ask user to input the master password which is used to generate an encryption
        # key. Use getpass to ask the password without echoing.
        try:
            master_password = getpass.getpass('Master Password: ')
        except:
            print('Error!')
        # We use encryption helper to encrypt passwords.
        self.encryption_helper = EncryptionHelper(master_password)
        # Passwords model is used to store information about the passwords.
        self.passwords_model = Passwords(self.encryption_helper)
        # create_main_menu will get passwords model because it will make some menu
        # items (in)visible if password list is empty or not. If password list is empty
        # menu items Show Password Info, Change Password and Delete Password will not 
        # be visible. Otherwise they are visible.
        self.main_menu = create_main_menu(self.passwords_model)

    def run(self):
        self.main_menu.make_a_choice()

PasswordManager().run()
# try:
#     PasswordManager().run()
# except Exception as e:
#     print("Error!")
#     print(e)
# except KeyboardInterrupt:
#     pass
