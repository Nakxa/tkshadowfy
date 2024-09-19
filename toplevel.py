import tkinter as tk
from tkshadowfy import Shadow

root = tk.Tk()
toplevel = tk.Toplevel(root)
toplevel.title("Toplevel Window")
shadow_toplevel = Shadow(toplevel, color='#4A86E8', size=5, offset_x=3, offset_y=3)
root.mainloop()