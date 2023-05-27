from menu import Menu
from shared.ui.command_line.menu import MenuItem
from shared.action import Action


class SelectPasswordMenu(Menu):
    def __init__(self, passwords, selection_function: function):
        super().__init__("Select Password")

        for p in passwords:
            self.add_menu_item(MenuItem(p["name"], Action(selection_function, )))