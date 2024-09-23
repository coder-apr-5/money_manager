import tkinter as tk
from tkinter import messagebox

# Function to calculate the distribution
def calculate_distribution():
    try:
        salary = float(entry_salary.get())
        expenses = salary * 0.50
        savings = salary * 0.20
        investments = salary * 0.20
        discretionary_spending = salary * 0.10

        result.set(f"Expenses: ${expenses:.2f}\n\n"
                   f"Savings: ${savings:.2f}\n\n"
                   f"Investments: ${investments:.2f}\n\n"
                   f"Discretionary Spending: ${discretionary_spending:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the salary.")


# Create the main window
root = tk.Tk()
root.title("Money Manager")
root.geometry("400x600")
root.resizable(False, False)
root.configure(bg='#E7CEFF')

#Logo
logo =tk.PhotoImage(file="logo.png")
tk.Label(root,image=logo,bg="#E7CEFF").place(x=115,y=2)

#heading
heading=tk.Label(root,text="Money Manager",
              font='arial 20 bold',fg="#9B50DE",
              bg="#E7CEFF")
heading.place(x=100,y=195)

# Create and place the widgets
label_salary = tk.Label(root, text="Enter your salary:",
                        bg='#E7CEFF',
                        font='arial 12 bold')
label_salary.place(x=130, y=260)

entry_salary = tk.Entry(root,width=17,font='arial 11 bold')
entry_salary.place(x=130, y=290)

button_organize = tk.Button(root, text="Organize",
                            command=calculate_distribution,
                            width=11,
                            cursor='hand2', bg="#FFAA00", bd=0,
                            activebackground='#ED8051',
                            font='arial 14 bold')
button_organize.place(x=132, y=340)

result = tk.StringVar()
label_result = tk.Label(root, textvariable=result, justify="left",
                        font='arial 11 bold',bg="#E7CEFF",fg='#9B50DE')
label_result.place(x=120, y=400)

insta_page=tk.Label(root,text="@pythonagham",bg='#E7CEFF',
              fg='black',font='arial 10 bold italic')
insta_page.place(x=155,y=560)

# Run the application
root.mainloop()