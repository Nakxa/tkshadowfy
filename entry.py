import tkinter as tk
from tkshadowfy import Shadow

root = tk.Tk()
entry = tk.Entry(root)
entry.pack(pady=20)
shadow_entry = Shadow(entry, color='#4A86E8', size=5, offset_x=3, offset_y=3)
root.mainloop()