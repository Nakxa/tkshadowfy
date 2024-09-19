import tkinter as tk
from tkshadowfy import Shadow

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=100)
canvas.pack(pady=20)
shadow_canvas = Shadow(canvas, color='#4A86E8', size=5, offset_x=3, offset_y=3)
root.mainloop()