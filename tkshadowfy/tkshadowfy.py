import tkinter as tk

class Shadow:
    def __init__(self, widget, color='#4A86E8', size=5, offset_x=2, offset_y=2,
                 opacity=0.3, onhover={}, onclick={}):
        self.widget = widget
        self.master = widget.master
       
        # Shadow parameters
        self.normal = {'size': size, 'color': color, 'offset_x': offset_x, 'offset_y': offset_y, 'opacity': opacity}
        self.onhover = {**self.normal, **onhover}
        self.onclick = {**self.normal, **onclick}
       
        self.current = self.normal
        self.shadow_canvas = None
       
        # Bind events
        self.widget.bind("<Enter>", self.on_enter, add='+')
        self.widget.bind("<Leave>", self.on_leave, add='+')
        self.widget.bind("<ButtonPress-1>", self.on_click, add='+')
        self.widget.bind("<ButtonRelease-1>", self.on_release, add='+')
       
        # Initial render
        self.render_shadow()
       
        # Update shadow on widget changes
        self.widget.bind("<Configure>", self.render_shadow, add='+')

    def render_shadow(self, event=None):
        if self.shadow_canvas:
            self.shadow_canvas.destroy()
       
        x, y = self.widget.winfo_x(), self.widget.winfo_y()
        w, h = self.widget.winfo_width(), self.widget.winfo_height()
       
        size = self.current['size']
        offset_x, offset_y = self.current['offset_x'], self.current['offset_y']
        max_opacity = self.current['opacity']
       
        self.shadow_canvas = tk.Canvas(self.master, highlightthickness=0)
        self.shadow_canvas.place(x=x + offset_x, y=y + offset_y,
                                 width=w + size, height=h + size)
       
        shadow_color = self.hex_to_rgb(self.current['color'])
        
        # Create rectangles for bottom and right shadow
        for i in range(size):
            opacity = max_opacity * (1 - i / size)
            shadow_color_with_opacity = self.adjust_color_brightness(shadow_color, opacity)
            
            # Bottom shadow
            self.shadow_canvas.create_rectangle(0, h + i, w + size, h + i + 1,
                                                fill=shadow_color_with_opacity, outline='')
            # Right shadow
            self.shadow_canvas.create_rectangle(w + i, 0, w + i + 1, h + size,
                                                fill=shadow_color_with_opacity, outline='')
       
        self.widget.lift()

    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def adjust_color_brightness(self, rgb_color, factor):
        return f'#{int(255 - (255-rgb_color[0])*factor):02x}{int(255 - (255-rgb_color[1])*factor):02x}{int(255 - (255-rgb_color[2])*factor):02x}'

    def on_enter(self, event):
        self.current = self.onhover
        self.render_shadow()

    def on_leave(self, event):
        self.current = self.normal
        self.render_shadow()

    def on_click(self, event):
        self.current = self.onclick
        self.render_shadow()

    def on_release(self, event):
        self.current = self.normal
        self.render_shadow()
