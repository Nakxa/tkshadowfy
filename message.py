import tkinter as tk
from tkshadowfy import Shadow

root = tk.Tk()
message = tk.Message(root, text="This is a message with shadow.")
message.pack(pady=20)
shadow_message = Shadow(message, color='#4A86E8', size=5, offset_x=3, offset_y=3)
root.mainloop()