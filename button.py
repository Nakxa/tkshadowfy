import tkinter as tk
from tkshadowfy import Shadow

root = tk.Tk()
button = tk.Button(root, text="Click Me!")
button.pack(pady=20)
shadow_button = Shadow(button, color='#4A86E8', size=8, offset_x=4, offset_y=4)
root.mainloop()