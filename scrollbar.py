import tkinter as tk
from tkinter import ttk
from tkshadowfy import Shadow

root = tk.Tk()
frame = tk.Frame(root)
frame.pack(pady=20)
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
shadow_scrollbar = Shadow(scrollbar, color='#4A86E8', size=5, offset_x=3, offset_y=3)
root.mainloop()