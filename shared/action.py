class Action:
    def __init__(self, call_back_function, payload = None):
        self.call_back_function = call_back_function
        self.payload = payload

    def execute(self):
        if(self.payload == None):
            self.call_back_function()
        else:
            self.call_back_function(self.payload)