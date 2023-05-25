from os import system


class Action:
    def __init__(self, call_back_function, payload = None):
        self.call_back_function = call_back_function
        self.payload = payload

    def execute(self):
        print("Action.execute")
        print(self.call_back_function)
        print("payload: ")
        print(self.payload)

        if(self.payload == None):
            self.call_back_function()
        else:
            self.call_back_function(self.payload)


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

        selection_index = int(input(prompt_string))-1

        if(selection_index >= 0):
            try:
                self.menu_items[selection_index].choose()
            except:
                print("Invalid choice!")
        else:
            print("Invalid choice!")