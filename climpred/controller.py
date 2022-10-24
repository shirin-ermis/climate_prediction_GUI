from model import Model
from view import View

class Controller():
    """
    Main controller
    """
    
    def __init__(self):
        self.model = Model()
        self.view = View(self)
        
    def main(self):
        self.view.main()
        
if __name__ == '__main__':
    calculator = Controller()
    calculator.main()