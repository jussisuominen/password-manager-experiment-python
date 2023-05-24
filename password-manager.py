# Imports
from shared.passwords import Passwords
from shared.encryption_helper import EncryptionHelper
from shared.menu import Menu, MenuItem, Action


class PasswordManager:
    def __init__(self):
        self.encryption_helper = EncryptionHelper("test")
        self.passwords_model = Passwords(self.encryption_helper)

        # Create menus.
        self.main_menu = Menu("Password Manager: Main Menu")
        self.passwords_menu = Menu("Select password")

        self.main_menu.add_menu_item(MenuItem("Show password info", 
                                              Action(self.passwords_menu.make_a_choice)))
        self.main_menu.add_menu_item(MenuItem("Add Password", 
                                              Action(self.add_password)))
        self.main_menu.add_menu_item(MenuItem("Exit", 
                                              Action(exit)))

        for password in self.passwords_model.passwords:
            self.passwords_menu.add_menu_item(MenuItem(password["name"], Action(self.show_password_info, password)))

    def add_password(self):
        name = input("Password name: ")
        username = input("Username: ")
        password = input("Password")

        password_dict = { "name": name, "username": username, "password": password }

        self.passwords_menu.add_menu_item(MenuItem(password_dict["name"], 
                                                   Action(self.show_password_info, password_dict)))

        self.passwords_model.add_password(name, username, password)

        self.main_menu.make_a_choice()
    
    def show_password_info(self, password):
        name, username, password_string = password.values()
        print(f"Password name: {name}")
        print(f"Username: {username}")
        print(f"Password: {password_string}")

        input("\nPress enter to continue!")

        self.main_menu.make_a_choice()

    def run(self):
        self.main_menu.make_a_choice()

    
PasswordManager().run()