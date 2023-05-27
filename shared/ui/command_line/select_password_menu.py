from menu import Menu


class SelectPasswordMenu(Menu):
    def __init__(self, passwords_model, selection_action):
        super().__init__("Select Password")
        self.passwords_model = passwords_model
        self.selection_action = selection_action

    def make_a_choice(self, prompt_string: str = ": "):
        