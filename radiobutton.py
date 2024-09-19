import tkinter as tk
from tkshadowfy import Shadow

root = tk.Tk()
radiobutton = tk.Radiobutton(root, text="Select me!")
radiobutton.pack(pady=20)
shadow_radiobutton = Shadow(radiobutton, color='#4A86E8', size=5, offset_x=3, offset_y=3)
root.mainloop()