from shared.ui.command_line.menu import Menu, MenuItem
from shared.action import Action
from shared.ui.command_line.select_password_menu import SelectPasswordMenu

def create_main_menu(passwords_model):
    main_menu = Menu("Password Manager: Main Menu")

    show_password_details_menu_item = ShowPasswordDetailsMenuItem(
            passwords_model, main_menu)
    change_password_menu_item = ChangePasswordMenuItem(passwords_model, 
                                                           main_menu)
    delete_password_menu_item = DeletePasswordMenuItem(passwords_model, 
                                                        main_menu)
        
    # If there are no passwords hide Show Password Info, Change Password
    # and Delete Password menu items because if there are no passwords
    # you can't show password info or change/delete a password.
    if len(passwords_model.passwords) == 0:
        show_password_details_menu_item.visible = False
        change_password_menu_item.visible = False
        delete_password_menu_item.visible = False

    main_menu.add_menu_item(show_password_details_menu_item)
    main_menu.add_menu_item(AddPasswordMenuItem(passwords_model, 
                                                         main_menu))
    main_menu.add_menu_item(change_password_menu_item)
    main_menu.add_menu_item(delete_password_menu_item)
    main_menu.add_menu_item(MenuItem("Exit", Action(exit)))

    return main_menu


class ShowPasswordDetailsMenuItem(MenuItem):
    def __init__(self, passwords_model, main_menu):
        super().__init__("Show password details", Action(self.show_password_info))
        self.passwords_model = passwords_model
        self.main_menu = main_menu
    def choose(self):
        select_password_menu = SelectPasswordMenu(self.passwords_model, 
                                                  self.show_password_info,
                                                  self.main_menu)
        select_password_menu.title = "Show password info\nSelect password"
        select_password_menu.make_a_choice()
    def show_password_info(self, password_index):
        print(self.passwords_model.passwords[password_index])
        input("\nPress enter to continue!")
        self.main_menu.make_a_choice()
        
    
class AddPasswordMenuItem(MenuItem):
    def __init__(self, passwords_model, main_menu):
        super().__init__("Add password", Action(self.choose))
        self.passwords_model = passwords_model
        self.main_menu = main_menu
    def choose(self):
        print("Please provide password information. If you want to cancel " +
              "adding a password, leave any input empty (press Enter after the prompt).\n")

        name = input("Password name: ")

        if(name == ""): 
            print("Empty input. Returning back to main menu...")
            self.main_menu.make_a_choice(False)

        username = input("Username: ")

        if(username == ""): 
            print("Empty input. Returning back to main menu...")
            self.main_menu.make_a_choice(False)

        password = input("Password: ")

        if(password == ""): 
            print("Empty input. Returning back to main menu...")
            self.main_menu.make_a_choice(False)

        self.passwords_model.add_password(name, username, password)

        self.main_menu = create_main_menu(self.passwords_model)

        self.main_menu.make_a_choice()


class ChangePasswordMenuItem(MenuItem):
    def __init__(self, passwords_model, main_menu):
        super().__init__("Change Password", Action(self.choose))
        self.passwords_model = passwords_model
        self.main_menu = main_menu
    def choose(self):
        select_password_menu = SelectPasswordMenu(self.passwords_model, 
                                                  self.change_password,
                                                  self.main_menu)
        select_password_menu.title = "Change password info\nSelect password"
        select_password_menu.make_a_choice()
    def change_password(self, password_index):
        new_password = input("New Password: ")

        if new_password == "":
            pass
        else:
            self.passwords_model.change_password(password_index, new_password)

        self.main_menu.make_a_choice()

    
class DeletePasswordMenuItem(MenuItem):
    def __init__(self, passwords_model, main_menu):
        super().__init__("Delete Password", Action(self.choose))
        self.passwords_model = passwords_model
        self.main_menu = main_menu
    def choose(self):
        select_password_menu = SelectPasswordMenu(self.passwords_model, 
                                                  self.delete_password,
                                                  self.main_menu)
        select_password_menu.title = "Delete password"
        select_password_menu.make_a_choice()
    def delete_password(self, password_index):
        answer = input('Are you sure you want to delete this password? (y/N)')

        if(answer.lower() == 'y'):
            self.passwords_model.delete_password(password_index)
            
        self.main_menu = create_main_menu(self.passwords_model)

        self.main_menu.make_a_choice()