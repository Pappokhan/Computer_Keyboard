import tkinter as tk

class ComputerKeyboard(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.text_area = tk.Text(self, wrap='word', height=10)
        self.text_area.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        self.keyboard_frame = tk.Frame(self)
        self.keyboard_frame.grid(row=1, column=0)

        self.keys = [
            ['~', '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backspace'],
            ['Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\', 'Del'],
            ['Caps Lock', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'Enter'],
            ['Shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'Shift'],
            ['Ctrl', 'Win', 'Alt', ' ', 'Alt', 'Ctrl']
        ]

        for row, key_row in enumerate(self.keys):
            for col, key in enumerate(key_row):
                key_button = tk.Button(self.keyboard_frame, text=key, width=5, height=2)
                key_button.grid(row=row, column=col, padx=2, pady=2, sticky='nsew')

root = tk.Tk()
root.title('Computer Keyboard')
computer_keyboard = ComputerKeyboard(root)
computer_keyboard.pack(fill='both', expand=True)
root.mainloop()
