import tkinter as tk
from typing import List

class Calculator:
    """teste"""
    def __init__(self, root: tk.Tk, label: tk.Label, display: tk.Entry,buttons: List[List[tk.Button]]):
        self.root = root
        self.label = label
        self.display = display
        self.buttons = buttons
    def start(self):
        self._config_buttons()
        self._config_display()
        self.root.mainloop()
        
    def _config_buttons(self):
        buttons = self.buttons
        for row_values in buttons:
            for button in row_values:
                button_text  = button['text']
                if button_text == 'C': 
                    button.bind('<Button-1>', self.clear)
                if button_text == '0123456789.+-/*^()':
                    button.bind('<Button-2', self.add_text_to_display)
                
                
    def _config_display(self):
        ...
        
    def clear(self, event=None):
        self.display.delete(0,'end')
        
    def add_text_to_display(self, event=None):
        self.display.insert('end', event.widget['text'])