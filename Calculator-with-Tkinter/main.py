from calc_factories import make_root, make_display, make_buttons,make_label
from calc_class import Calculator
def main():
    root = make_root()
    display = make_display(root)
    label = make_label(root)
    buttons = make_buttons(root)
    calculator = Calculator(root, label, display, buttons)
    calculator.start()
    
    # root.mainloop() 
if __name__ == '__main__':
    main()