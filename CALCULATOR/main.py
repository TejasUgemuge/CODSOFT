import tkinter as tk

# Main window setup
root = tk.Tk()
root.title('Simple Calculator')
root.configure(bg='#0000FF')
root.resizable(width=False, height=False)

# Entry field
ent_field = tk.Entry(root, bg='#ADD8E6', fg='#000080', font=('Arial', 25), borderwidth=10, justify="right")
ent_field.grid(row=0, columnspan=4, padx=10, pady=10, sticky='nsew')
ent_field.insert(0, '0')

FONT = ('Arial', 10, 'bold')

class SimpleCalculator:
    def __init__(self):
        self.current = ''
        self.inp_value = True
        self.result = False

    def Entry(self, value):
        ent_field.delete(0, 'end')
        ent_field.insert(0, value)

    def Enter_Num(self, num):
        self.result = False
        firstnum = ent_field.get()
        secondnum = str(num)
        if self.inp_value:
            self.current = secondnum
            self.inp_value = False
        else:
            self.current = firstnum + secondnum
        self.Entry(self.current)

    def Standard_Ops(self, val):
        temp_str = ent_field.get()
        try:
            if val == '=':
                ans = str(eval(temp_str))
                self.result = True
                self.Entry(ans)
            else:
                self.Entry(temp_str + val)
            self.inp_value = False
        except (ValueError, SyntaxError):
            self.Entry('Error')

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.Entry(0)
        self.inp_value = True

# Create calculator instance
calc = SimpleCalculator()

# Number buttons
numberpad = "789456123"
i = 0
buttons = []
for j in range(2, 5):
    for k in range(3):
        buttons.append(tk.Button(root, text=numberpad[i], font=FONT, fg="red", width=6, height=2,
                                 highlightbackground='#ADD8E6', highlightthickness=2))
        buttons[i].grid(row=j, column=k, sticky='nsew', padx=10, pady=10)
        buttons[i]["command"] = lambda x=numberpad[i]: calc.Enter_Num(x)
        i += 1

# Additional buttons
tk.Button(root, text='0', command=lambda: calc.Enter_Num('0'), font=FONT, fg="#000000",
          highlightbackground='#ADD8E6', highlightthickness=2).grid(row=5, column=0, columnspan=2, sticky='nsew', padx=10, pady=10)

tk.Button(root, text='.', command=lambda: calc.Standard_Ops('.'), font=FONT, fg="#000000",
          highlightbackground='#ADD8E6', highlightthickness=2).grid(row=5, column=2, sticky='nsew', padx=10, pady=10)

tk.Button(root, text='=', command=lambda: calc.Standard_Ops('='), font=FONT, fg="#000000",
          highlightbackground='#ADD8E6', highlightthickness=2).grid(row=5, column=3, sticky='nsew', padx=10, pady=10)

tk.Button(root, text='CE', command=lambda: calc.Clear_Entry(), font=FONT, fg="#000000",
          highlightbackground='#ADD8E6', highlightthickness=2).grid(row=1, column=0, columnspan=2, sticky='nsew', padx=10, pady=10)

# Operation buttons
ops = ['+', '-', '*', '/']
for idx, op in enumerate(ops):
    tk.Button(root, text=op, command=lambda x=op: calc.Standard_Ops(x), font=FONT, fg="#000000",
              highlightbackground='#ADD8E6', highlightthickness=2).grid(row=1+idx, column=3, sticky='nsew', padx=10, pady=10)

# Start the application
if __name__ == '__main__':
    root.mainloop()
