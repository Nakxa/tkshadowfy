import tkinter as tk
from tkshadowfy import Shadow

root = tk.Tk()
frame = tk.Frame(root, width=200, height=100)
frame.pack(pady=20)
shadow_frame = Shadow(frame, color='#4A86E8', size=5, offset_x=3, offset_y=3)
root.mainloop()