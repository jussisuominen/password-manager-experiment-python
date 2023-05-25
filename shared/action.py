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