import tkinter as tk
from tkshadowfy import Shadow

root = tk.Tk()
scale = tk.Scale(root, from_=0, to=100)
scale.pack(pady=20)
shadow_scale = Shadow(scale, color='#4A86E8', size=5, offset_x=3, offset_y=3)
root.mainloop()