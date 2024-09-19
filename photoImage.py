import tkinter as tk
from tkshadowfy import Shadow

root = tk.Tk()
photo = tk.PhotoImage(file='path_to_image.png')  # Provide a valid image path
label = tk.Label(root, image=photo)
label.pack(pady=20)
shadow_label = Shadow(label, color='#4A86E8', size=5, offset_x=3, offset_y=3)
root.mainloop()