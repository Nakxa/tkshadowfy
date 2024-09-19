import tkinter as tk
from tkshadowfy import Shadow

root = tk.Tk()
menubutton = tk.Menubutton(root, text="Menu")
menubutton.menu = tk.Menu(menubutton)
menubutton['menu'] = menubutton.menu
menubutton.menu.add_command(label='Option 1')
menubutton.pack(pady=20)
shadow_menubutton = Shadow(menubutton, color='#4A86E8', size=5, offset_x=3, offset_y=3)
root.mainloop()