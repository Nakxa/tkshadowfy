# TkShadowfy

TkShadowfy is a Python library that enables you to easily add shadow effects to Tkinter widgets, enhancing the visual appeal of your GUI applications.

## Features

- Add customizable shadows to various Tkinter widgets
- Control shadow color, size, and offset
- Compatible with most common Tkinter widgets

## Installation

```
pip install tkshadowfy
```

## Usage

Here's a simple example of how to use TkShadowfy:

```python
import tkinter as tk
from tkshadowfy import Shadow

root = tk.Tk()
label = tk.Label(root, text="Hello, TkShadowfy!", font=('Arial', 24))
label.pack(pady=20)
shadow_label = Shadow(label, color='#4A86E8', size=5, offset_x=3, offset_y=3)
root.mainloop()
```

## Supported Widgets

TkShadowfy supports a wide range of Tkinter widgets, including:

- Label
- Button
- Entry
- Text
- Frame
- Canvas
- Listbox
- Scrollbar
- Checkbutton
- Radiobutton
- Scale
- Spinbox
- Menu
- MenuButton
- Message
- PhotoImage
- Toplevel

## Customization

You can customize the shadow effect using the following parameters:

- `color`: Shadow color (hex code)
- `size`: Shadow size
- `offset_x`: Horizontal offset
- `offset_y`: Vertical offset

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.