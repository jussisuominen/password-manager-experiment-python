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
        i = 1
        for menu_item in self.menu_items:
            print(f"{i}. {menu_item.title}")
            i += 1

        try:
            selection_index = int(input(prompt_string))-1
        except:
            print("Invalid input! Please input a number to select an option.")
            exit()


        if(selection_index >= 0 and selection_index < len(self.menu_items)):
            self.menu_items[selection_index].choose()
        else:
            print("Invalid choice!")