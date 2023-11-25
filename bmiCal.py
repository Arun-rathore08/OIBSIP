import tkinter as tk

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())

    bmi = weight / (height ** 2)

    interpretation = ""
    if bmi < 18.5:
        interpretation = "Underweight"
    elif bmi < 25:
        interpretation = "Normal weight"
    elif bmi < 30:
        interpretation = "Overweight"
    else:
        interpretation = "Obese"

    bmi_label.config(text="Your BMI: {:.2f}".format(bmi))
    interpretation_label.config(text="Interpretation: " + interpretation)

# Create the main window
window = tk.Tk()
window.title("BMI Calculator")

# Create the weight label and entry
weight_label = tk.Label(window, text="Weight (in kg):")
weight_label.pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

# Create the height label and entry
height_label = tk.Label(window, text="Height (in meters):")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()

# Create the calculate button
calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

# Create the BMI label
bmi_label = tk.Label(window, text="Your BMI: ")
bmi_label.pack()

# Create the interpretation label
interpretation_label = tk.Label(window, text="Interpretation: ")
interpretation_label.pack()

# Start the GUI event loop
window.mainloop()
