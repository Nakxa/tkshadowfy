import tkinter as tk
from tkshadowfy import Shadow

root = tk.Tk()
spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.pack(pady=20)
shadow_spinbox = Shadow(spinbox, color='#4A86E8', size=5, offset_x=3, offset_y=3)
root.mainloop()