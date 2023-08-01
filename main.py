from tkinter import *

ekran = Tk()
ekran.title("BMI Calculator")
ekran.minsize(width=400,height=180)
ekran.config(padx=30,pady=30)

weight_label=Label(text="Enter Your Weight(kg)")
weight_label.pack(side="top")

weight_entry=Entry(width=13)
weight_entry.pack(side="top")

height_label=Label(text="Enter Your Height(cm)")
height_label.pack(side="top")

height_entry=Entry(width=13)
height_entry.pack(side="top")

def bmi_calculator():
    kg = weight_entry.get()
    boy = height_entry.get()
    if kg == "" or boy == "":
        result_label.config(text="Enter both weight and height")
    else:
        try:
            bmi = float(kg) / ((float(boy) / 100) ** 2)
            result_string = bmi_index(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter a valid number!")
def bmi_index(bmi):
    if bmi < 18.5:
        result_string = f"Your BMI is {round(bmi,2)}. You are Underweight"
    elif bmi > 18.5 and bmi<=24.9:
        result_string = f"Your BMI is {round(bmi,2)}. You are Normal weight"
    elif bmi > 24.9 and bmi<=29.9:
        result_string = f"Your BMI is {round(bmi,2)}. You are Pre-obesity"
    elif bmi > 29.9 and bmi<=34.9:
        result_string = f"Your BMI is {round(bmi,2)}. You are Obesity class |"
    elif bmi > 34.9 and bmi<=39.9:
        result_string = f"Your BMI is {round(bmi,2)}. You are Obesity class ||"
    else:
        result_string = f"Your BMI is {round(bmi,2)}. You are Obesity class |||"

    return result_string


button = Button(text="Calculate",bg="white",command=bmi_calculator)
button.pack()

result_label=Label()
result_label.pack()

ekran.mainloop()