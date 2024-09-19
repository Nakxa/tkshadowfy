import tkinter as tk
from tkshadowfy import Shadow

root = tk.Tk()
listbox = tk.Listbox(root)
listbox.pack(pady=20)
shadow_listbox = Shadow(listbox, color='#4A86E8', size=5, offset_x=3, offset_y=3)
root.mainloop()