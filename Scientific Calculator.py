import math
from tkinter import *

# Window configuration
root = Tk()
root.title("Scientific Calculator")  # Set the title of the window
root.configure(bg="light grey")  # Set background color
root.geometry("500x630")  # Set the size of the window

# Variables
eq = ""  # String to hold the current equation
mode = "Deg"  # Default mode is Degrees
mode_display = StringVar()  # To display 'R' or 'D' for radians or degrees

# Function to update the display
def update_display():
    mode_display.set("D" if mode == "Deg" else "R")  # Update the mode display
    textbox.delete('1.0', END)  # Clear the textbox
    if eq == "Error":
        textbox.insert(END, "Invalid Input\n")  # Show error message
    else:
        textbox.insert(END, f"{eq}\n")  # Insert the current equation

# Functions for calculator operations
def btnclick(num):
    global eq
    eq += str(num)  # Append the clicked number to the equation
    update_display()

def result():
    global eq
    try:
        total = str(eval(eq))  # Evaluate the current equation
        eq = f"{float(total):.6g}"  # Format to 6 significant digits
        update_display()
    except Exception:
        eq = "Error"  # Set error state if evaluation fails
        update_display()

def clear():
    global eq
    eq = ""  # Clear the equation
    update_display()

def toggle_mode():
    global mode
    mode = "Rad" if mode == "Deg" else "Deg"  # Toggle between Degrees and Radians
    update_display()

def safe_inverse_trig(func, val):
    try:
        if -1 <= val <= 1:
            return func(val)  # Ensure input is within valid range for inverse trig
        else:
            return "Error"
    except Exception:
        return "Error"

# Display screen for equation
textbox = Text(root, relief=RIDGE, bd=10, bg="black", insertwidth=4, fg="white", width=30, height=3, font=("Helvetica", 20))
textbox.grid(row=1, column=0, columnspan=5, padx=20, pady=10)  # Position the display

# Mode Display ('D' for Degrees or 'R' for Radians) at the top-right of the display
mode_label = Label(root, textvariable=mode_display, font=("Helvetica", 18), bg="black", fg="white")
mode_label.place(x=450, y=20)  # Position the mode label at the top-right
update_display()  # Initial display update

# Scientific calculations
def calculate_trig(func):
    global eq
    try:
        val = float(eq)
        if mode == "Deg":
            result_value = func(math.radians(val))  # Convert to radians if in degree mode
        else:
            result_value = func(val)
        eq = f"{result_value:.6g}"  # Format to 6 significant digits
        update_display()
    except ValueError:
        eq = "Error"
        update_display()

def calculate_inverse_trig(func):
    global eq
    try:
        val = float(eq)
        result_value = safe_inverse_trig(func, val)  # Safely calculate inverse trig
        if isinstance(result_value, float):
            if mode == "Deg":
                result_value = math.degrees(result_value)  # Convert to degrees if necessary
        eq = f"{result_value:.6g}"  # Format to 6 significant digits
        update_display()
    except ValueError:
        eq = "Error"
        update_display()

def calculate_log():
    global eq
    try:
        val = float(eq)
        result_value = math.log10(val)  # Calculate logarithm (base 10)
        eq = f"{result_value:.6g}"  # Format to 6 significant digits
        update_display()
    except ValueError:
        eq = "Error"
        update_display()

def calculate_ln():
    global eq
    try:
        val = float(eq)
        result_value = math.log(val)  # Calculate natural logarithm
        eq = f"{result_value:.6g}"  # Format to 6 significant digits
        update_display()
    except ValueError:
        eq = "Error"
        update_display()

def calculate_sqrt():
    global eq
    try:
        val = float(eq)
        result_value = math.sqrt(val)  # Calculate square root
        eq = f"{result_value:.6g}"  # Format to 6 significant digits
        update_display()
    except ValueError:
        eq = "Error"
        update_display()

def calculate_factorial():
    global eq
    try:
        val = int(eq)
        if val < 0:
            raise ValueError  # Factorial is not defined for negative numbers
        result_value = math.factorial(val)  # Calculate factorial
        eq = f"{result_value:.6g}"  # Format to 6 significant digits
        update_display()
    except ValueError:
        eq = "Error"
        update_display()

def calculate_exp():
    global eq
    try:
        val = float(eq)
        result_value = math.exp(val)  # Calculate exponential
        eq = f"{result_value:.6g}"  # Format to 6 significant digits
        update_display()
    except ValueError:
        eq = "Error"
        update_display()

# Creating buttons
Button(root, text="7", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black", command=lambda: btnclick(7)).grid(row=2, column=0, padx=5, pady=5)
Button(root, text="8", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=lambda: btnclick(8)).grid(row=2, column=1, padx=5, pady=5)
Button(root, text="9", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=lambda: btnclick(9)).grid(row=2, column=2, padx=5, pady=5)
Button(root, text="/", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=lambda: btnclick('/')).grid(row=2, column=3, padx=5, pady=5)
Button(root, text="C", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=clear).grid(row=2, column=4, padx=5, pady=5)

Button(root, text="4", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=lambda: btnclick(4)).grid(row=3, column=0, padx=5, pady=5)
Button(root, text="5", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=lambda: btnclick(5)).grid(row=3, column=1, padx=5, pady=5)
Button(root, text="6", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=lambda: btnclick(6)).grid(row=3, column=2, padx=5, pady=5)
Button(root, text="*", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=lambda: btnclick('*')).grid(row=3, column=3, padx=5, pady=5)
Button(root, text="(", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=lambda: btnclick('(')).grid(row=3, column=4, padx=5, pady=5)

Button(root, text="1", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=lambda: btnclick(1)).grid(row=4, column=0, padx=5, pady=5)
Button(root, text="2", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=lambda: btnclick(2)).grid(row=4, column=1, padx=5, pady=5)
Button(root, text="3", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=lambda: btnclick(3)).grid(row=4, column=2, padx=5, pady=5)
Button(root, text="-", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=lambda: btnclick('-')).grid(row=4, column=3, padx=5, pady=5)
Button(root, text=")", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=lambda: btnclick(')')).grid(row=4, column=4, padx=5, pady=5)

Button(root, text="0", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=lambda: btnclick(0)).grid(row=5, column=0, padx=5, pady=5)
Button(root, text=".", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=lambda: btnclick('.')).grid(row=5, column=1, padx=5, pady=5)
Button(root, text="=", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=result).grid(row=5, column=2, padx=5, pady=5)
Button(root, text="+", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=lambda: btnclick('+')).grid(row=5, column=3, padx=5, pady=5)
Button(root, text="^", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=lambda: btnclick("**")).grid(row=5, column=4, padx=5, pady=5)

# Scientific function buttons
Button(root, text="sin", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=lambda: calculate_trig(math.sin)).grid(row=6, column=0, padx=5, pady=5)
Button(root, text="cos", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=lambda: calculate_trig(math.cos)).grid(row=6, column=1, padx=5, pady=5)
Button(root, text="tan", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=lambda: calculate_trig(math.tan)).grid(row=6, column=2, padx=5, pady=5)
Button(root, text="log", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=calculate_log).grid(row=6, column=3, padx=5, pady=5)
Button(root, text="ln", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=calculate_ln).grid(row=6, column=4, padx=5, pady=5)

Button(root, text="asin", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=lambda: calculate_inverse_trig(math.asin)).grid(row=7, column=0, padx=5, pady=5)
Button(root, text="acos", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=lambda: calculate_inverse_trig(math.acos)).grid(row=7, column=1, padx=5, pady=5)
Button(root, text="atan", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=lambda: calculate_inverse_trig(math.atan)).grid(row=7, column=2, padx=5, pady=5)

Button(root, text="sqrt", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=calculate_sqrt).grid(row=8, column=0, padx=5, pady=5)
Button(root, text="!", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=calculate_factorial).grid(row=8, column=1, padx=5, pady=5)
Button(root, text="exp", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=calculate_exp).grid(row=8, column=2, padx=5, pady=5)

# Toggle between degrees and radians
Button(root, text="Mode", font=("Arial", 14), width=4, height=2, borderwidth=1, relief=SOLID, fg="white", bg="black",command=toggle_mode).grid(row=7, column=3, padx=5, pady=5)

# Start the main loop of the application
root.mainloop()
