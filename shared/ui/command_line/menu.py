import sys
from os import system

sys.path.append("/Users/jussisuominen2/Desktop/Ohjelmointi/Python/password-manager/shared")

from shared.action import Action

class MenuItem:
    def __init__(self, title, action: Action):
        self.title = title
        self.action = action

    def show(self):
        print(self.title)

    def choose(self):
        self.action.execute()


class Menu:
    def __init__(self, title):
        self.title = title
        self.menu_items = []

    def add_menu_item(self, menu_item: MenuItem):
        self.menu_items.append(menu_item)

    def make_a_choice(self, prompt_string: str = ": "):
        system("tput reset")
        print(self.title)

        self.show_options()

        selection_index = input(prompt_string)

        if(selection_index == "^C"):
            # User has pressed Ctrl-C (or equivalent). Exit!
            exit()

        try:
            # Try to convert string input to integer.
            selection_index = int(selection_index)
            # Decrement selection index by one because the list starts from 0
            # and users choice starts from 1.
            selection_index -= 1
        except:
            print("Invalid input! Please input a number to select an option.")
            input("Press enter to continue!")
            self.make_a_choice()


        if(selection_index >= 0 and selection_index < len(self.menu_items)):
            self.menu_items[selection_index].choose()
        else:
            print("Invalid choice!")
            input("Press enter to continue!")
            self.make_a_choice()

    def show_options(self):
        i = 1

        for menu_item in self.menu_items:
            print(f"{i}. {menu_item.title}")
            i += 1