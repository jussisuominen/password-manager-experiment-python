#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3

# Imports
import time

from shared.passwords import Passwords
from shared.encryption_helper import EncryptionHelper
from shared.ui.command_line.menu import Menu, MenuItem, Action


class PasswordManager:
    def __init__(self):
        self.encryption_helper = EncryptionHelper("test")
        self.passwords_model = Passwords(self.encryption_helper)

        # Create menus.
        self.main_menu = Menu("Password Manager: Main Menu")
        self.show_passwords_info_menu = Menu("Select password")
        self.change_password_menu = Menu("Select password to change")
        self.delete_password_menu = Menu("Select password to delete")

        i = 0
        for password in self.passwords_model.passwords:
            self.show_passwords_info_menu.add_menu_item(MenuItem(password["name"], 
                                                       Action(self.show_password_info, password)))
            self.change_password_menu.add_menu_item(MenuItem(password["name"], 
                                            Action(self.change_password, i)))
            self.delete_password_menu.add_menu_item(MenuItem(password["name"], 
                                            Action(self.delete_password, i)))
            i += 1

        self.main_menu.add_menu_item(MenuItem("Show password info", 
                                              Action(self.show_passwords_info_menu.make_a_choice)))
        self.main_menu.add_menu_item(MenuItem("Add Password", 
                                              Action(self.add_password)))
        self.main_menu.add_menu_item(MenuItem("Change Password", 
                                              Action(self.change_password_menu.make_a_choice)))
        self.main_menu.add_menu_item(MenuItem("Delete Password", 
                                              Action(self.delete_password_menu.make_a_choice)))
        self.main_menu.add_menu_item(MenuItem("Exit", 
                                              Action(self.close_app)))

    def add_password(self):
        name, username, password = self.ask_password_information()

        if name == "" or username == "" or password == "":
            self.main_menu.make_a_choice()

        password_dict = { "name": name, "username": username, "password": password }

        self.show_passwords_info_menu.add_menu_item(MenuItem(password_dict["name"], 
                                                   Action(self.show_password_info, password_dict)))

        self.passwords_model.add_password(name, username, password)

        self.main_menu.make_a_choice()

    def ask_password_information(self):
        name = input("Password name: ")
        username = input("Username: ")
        password = input("Password")

        return (name, username, password)
    
    def change_password(self, password_index):
        print(f"Changing password {password_index}")

        new_password = input("Password")

        if new_password != "":
            print("Empty password! Returning to main menu!")
            time.sleep(1)

            try:
                self.passwords_model.change_password(password_index, new_password)
            except:
                print("Could not change password! ")
        else:
            print("Empty password! Returning to main menu!")

        self.main_menu.make_a_choice()

    def close_app(self):
        exit()

    def delete_password(self, password_index):
        self.passwords_model.delete_password(password_index)
        del self.show_passwords_info_menu.menu_items[password_index]
        del self.change_password_menu.menu_items[password_index]
        del self.delete_password_menu.menu_items[password_index]

        self.main_menu.make_a_choice()
    
    def show_password_info(self, password):
        name, username, password_string = password.values()
        print(name)
        print(f"Username: {username}")
        print(f"Password: {password_string}")

        input("\nPress enter to continue!")

        self.main_menu.make_a_choice()

    def run(self):
        self.main_menu.make_a_choice()

try:
    PasswordManager().run()
except:
    pass