import tkinter as tk

window = tk.Tk()

cur = 0
ctrldown = False
def getanchor(cur):
    width, height = 0, 0
    if cur % 2 == 0:
        width = window.winfo_screenwidth() - window.winfo_reqwidth()
    if cur // 2 == 0:
        height = window.winfo_screenheight() - window.winfo_reqheight()
    return f"+{width}+{height}"

def MouseEnter(event):
    if not ctrldown:
        global cur
        cur  = (cur + 1)%4
        window.geometry(getanchor(cur))

def keydown(e: tk.Event):
    global ctrldown
    if not ctrldown:
        ctrldown = True

def keyup(e: tk.Event):
    global ctrldown
    if ctrldown:
        ctrldown = False

window.bind ("<Enter>", MouseEnter)
window.bind("<Control_L>", keydown)
window.bind("<KeyRelease-Control_L>", keyup)
window.mainloop()