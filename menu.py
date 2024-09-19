import tkinter as tk
from tkshadowfy import Shadow

root = tk.Tk()
menu = tk.Menu(root)
root.config(menu=menu)
shadow_menu = Shadow(menu, color='#4A86E8', size=5, offset_x=3, offset_y=3)
root.mainloop()