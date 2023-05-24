import sys
import os

import shared.master_password as master_password

from shared.debug import debug_message
from shared.passwords import Passwords
from shared.encryption_helper import EncryptionHelper

sys.path.append("./shared")


# This function shows the menu that is defined in a dictionary. Each key of the dictionary will
# be the title of the menu item and each value of the dictionary will be action performed
# when the menu item is selected. 
# The function also asks user to select a menu item and performs the action that is attached to 
# the menu item.
def show_menu(menu):
    os.system("tput reset")
    print("-" * 50)
    i = 1
    menu_actions = [] # This will contain the menu actions.

    # Show menu items and add their actions to menu_actions.
    for menu_item in menu.keys():
        print(f"{i}. {menu_item}")
        menu_actions.append(menu[menu_item])
        i = i + 1

    print("-" * 50)

    selection = input("Selection: ")

    # Perform action of the selected menu item.
    menu_actions[int(selection)-1]()


def show_password_info(password):
    print("")
    print(password["name"])
    print("-" * 50)
    print("Username: " + password["username"])
    print("Password: " + password["name"])

    input("Press enter to continue!")

    global main_menu

    show_menu(main_menu)

def show_select_password_menu():
    print("")
    print("Select password")
    select_password_menu = {}
    global passwords_model
    
    # Create a menu that has password names as items and show_password_info as action
    # (show_password_info will get the password object).
    for password in passwords_model.passwords:
        password_name = password["name"]
        select_password_menu[password_name] = lambda: show_password_info(password)

    show_menu(select_password_menu)

main_menu = {
    "Show password info": show_select_password_menu,
    "Exit": exit
}

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