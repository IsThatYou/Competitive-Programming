import tkinter as tk

root = tk.Tk()
a = tk.Button(master=root,text='A')
b = tk.Button(master=root,text='B')
c = tk.Button(master=root,text='C')
d = tk.Button(master=root,text='D')
a.grid(row=0, column=2)
b.grid(row=0, column=0, rowspan=2, sticky=tk.E)
c.grid(row=0, column=1, sticky = tk.N)
d.grid(row=1, column=0, columnspan=3, sticky=tk.S+tk.W+tk.N+tk.E)
root.rowconfigure(0, weight=2)
root.rowconfigure(1, weight=1)
root.columnconfigure(0,weight=0)
root.columnconfigure(1,weight=3)
root.columnconfigure(2,weight=0)
root.mainloop()