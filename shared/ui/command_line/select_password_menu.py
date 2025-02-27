from shared.ui.command_line.menu import Menu
from shared.ui.command_line.menu import MenuItem
from shared.action import Action


class SelectPasswordMenu(Menu):
    def __init__(self, passwords_model, select_callback, main_menu):
        super().__init__("Select Password", main_menu.make_a_choice)

        if len(passwords_model.passwords) == 0:
            print("There are no passwords! Please add one!")
            input("Press enter to continue!")
            main_menu.make_a_choice()

        i = 0
        for p in passwords_model.passwords:
            self.add_menu_item(MenuItem(p["name"], Action(select_callback, i)))
            i += 1