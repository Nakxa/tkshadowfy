import tkinter as tk
from tkshadowfy import Shadow

root = tk.Tk()
checkbutton = tk.Checkbutton(root, text="Check me!")
checkbutton.pack(pady=20)
shadow_checkbutton = Shadow(checkbutton, color='#4A86E8', size=5, offset_x=3, offset_y=3)
root.mainloop()