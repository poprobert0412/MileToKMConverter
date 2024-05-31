```markdown
# Mile to KM Converter

This is a simple graphical user interface (GUI) application built using Python and Tkinter. The application converts distances in miles to kilometers.

## Features

- User can input a distance in miles.
- The application converts the input distance to kilometers and displays the result.
- Simple and intuitive interface.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Tkinter (usually comes with Python standard library)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/poprobert0412/MileToKMConverter.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd miletokmconverter
    ```

3. **Run the application:**

    ```bash
    python converter.py
    ```

## Usage

1. Enter the distance in miles in the input field.
2. Click the "Calculate" button.
3. The converted distance in kilometers will be displayed.

## Code Overview

### converter.py

```python
from tkinter import *

# Create main window
from tkinter import *

windows = Tk()
windows.title("Mile To KM Converter")
windows.minsize(300, 200)

def calculate_to_km():
    miles = float(input.get())
    km_value = round(miles * 1.6, 2)
    km.config(text=km_value)

#Labels and button
my_label = Label(text="Miles", font=("Arial", 15, "bold"))
my_label.pack()
my_label.place(x=190, y=50)

equal = Label(text="is equal to", font=("Arial", 12, "bold"))
equal.pack()
equal.place(x=40, y=100)

km = Label(text=0, font=("Arial", 12, "bold"))
km.pack()
km.place(x=130, y=100)

button = Button(text="Calculate", command=calculate_to_km)
button.pack()
button.place(x=150, y=140)

input = Entry(width=10)
input.pack()
input.place(x=110, y=55)

km_show = Label(text="KM", font=("Arial", 12, "bold"))
km_show.pack()
km_show.place(x=190, y=100)


windows.mainloop()
```

## Contributing

If you want to contribute to this project, please fork the repository and create a pull request.

## Acknowledgments

- Thanks to the Python and Tkinter documentation for providing useful guides and references.
