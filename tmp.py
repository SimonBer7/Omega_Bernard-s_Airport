import tkinter as tk

def create_window():
    root = tk.Tk()
    root.title("Main Window")

    def hide_window():
        root.withdraw()

    def show_window():
        root.deiconify()

    btn_hide = tk.Button(root, text="Hide Window", command=hide_window)
    btn_hide.pack()

    btn_show = tk.Button(root, text="Show Window", command=show_window)
    btn_show.pack()

    root.mainloop()

create_window()
