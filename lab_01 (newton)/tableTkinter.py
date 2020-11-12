import tkinter as tk
import tkinter.ttk as ttk
  

window = tk.Tk()
style = ttk.Style()
headings=('aaa\nlkn', 'bbb\nlhl', 'ccc\njlkj')
rows=[[123, 456, 789], ['abc', 'def', 'ghk']]
table = ttk.Treeview(window, show="headings", selectmode="browse")
table["columns"]=headings
table["displaycolumns"]=headings

for head in headings:
    table.heading(head, text=head, anchor=tk.CENTER)
    idcol = table.column(head, anchor=tk.CENTER)
    print(idcol)


for row in rows:
    table.insert('', tk.END, values=tuple(row))

scrolltable = tk.Scrollbar(window, command=table.yview)
table.configure(yscrollcommand=scrolltable.set)
scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
table.pack(expand=tk.YES, fill=tk.BOTH)

window.mainloop()
