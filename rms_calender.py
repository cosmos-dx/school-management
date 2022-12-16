def get_date():
    import tkinter as tk
    from tkinter import ttk
    from tkcalendar import Calendar, DateEntry

    def cal_done():
        top.withdraw()
        root.quit()

    root = tk.Tk()
    root.withdraw() # keep the root window from appearing

    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1")
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=cal_done).pack()

    selected_date = None
    root.mainloop()
    return cal.selection_get()

selection = get_date()
print(selection)
