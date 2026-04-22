import tkinter as tk

# ================= LOGIC =================
def press(key):
    global expression
    
    if key == "=":
        try:
            result = str(eval(expression))
            entry_var.set(result)
            expression = result
        except:
            entry_var.set("Error")
            expression = ""
            
    elif key == "C":
        expression = ""
        entry_var.set("")
        
    elif key == "⌫":
        expression = expression[:-1]
        entry_var.set(expression)
        
    else:
        expression += str(key)
        entry_var.set(expression)


# ============== KEYBOARD SUPPORT ==============
def key_press(event):
    key = event.keysym

    if key == "Return":
        press("=")
    elif key == "BackSpace":
        press("⌫")
    elif key == "Escape":
        press("C")
    elif event.char in "0123456789+-*/.":
        press(event.char)


# ================= UI =================
root = tk.Tk()
root.title("Premium Calculator")
root.geometry("340x500")
root.resizable(False, False)

expression = ""
entry_var = tk.StringVar()

# ===== Gradient Background (Canvas) =====
canvas = tk.Canvas(root, width=340, height=500, highlightthickness=0)
canvas.pack(fill="both", expand=True)

def draw_gradient():
    for i in range(0, 500):
        color = f'#{20+i//5:02x}{20+i//6:02x}{40+i//4:02x}'
        canvas.create_line(0, i, 340, i, fill=color)

draw_gradient()

# Frame ustiga joylashtiramiz
frame = tk.Frame(canvas, bg="#000000", bd=0)
canvas.create_window(0, 0, anchor="nw", window=frame, width=340, height=500)

# ===== Display =====
entry = tk.Entry(frame, textvar=entry_var, font=("Arial", 24),
                 bd=0, bg="#111111", fg="white", justify="right")
entry.grid(row=0, column=0, columnspan=4,
           sticky="nsew", padx=15, pady=20, ipady=15)

# ===== Shadow Button =====
def create_button(text, row, col, color="#2e2e2e"):
    # Shadow
    shadow = tk.Label(frame, bg="#000000")
    shadow.grid(row=row, column=col, padx=6, pady=6, sticky="nsew")
    
    btn = tk.Button(frame, text=text, font=("Arial", 16),
                    bg=color, fg="white", bd=0,
                    activebackground="#555555",
                    command=lambda: press(text))
    
    btn.place(in_=shadow, relx=0, rely=0, relwidth=1, relheight=1)

# ===== Buttons =====
buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3),
]

for (text, row, col) in buttons:
    create_button(text, row, col)

# Backspace
create_button("⌫", 5, 0, "#ff9800")
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)
frame.grid_columnconfigure(3, weight=1)

# Clear
create_button("C", 5, 2, "#e53935")

# Grid config
for i in range(6):
    frame.grid_rowconfigure(i, weight=1)

# Keyboard binding
root.bind("<Key>", key_press)

root.mainloop()