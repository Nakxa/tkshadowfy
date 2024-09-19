import tkinter as tk
from tkshadowfy import Shadow

root = tk.Tk()
label = tk.Label(root, text="Hello, TkShadowfy!", font=('Arial', 24))
label.pack(pady=20)
shadow_label = Shadow(label, color='#4A86E8', size=5, offset_x=3, offset_y=3)
root.mainloop()