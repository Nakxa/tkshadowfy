import tkinter as tk
from tkshadowfy import Shadow

root = tk.Tk()
text = tk.Text(root, height=5, width=30)
text.pack(pady=20)
shadow_text = Shadow(text, color='#4A86E8', size=5, offset_x=3, offset_y=3)
root.mainloop()