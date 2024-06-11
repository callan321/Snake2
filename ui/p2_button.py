from ui.p1_button import P1Button

class P2Button(P1Button):   
    def get_id(self):
        return 'p2'
    
    def get_attr(self):
        return self.config.p2


    def get_text(self, controller : str):
        return f"P2 Controller: {controller}"
