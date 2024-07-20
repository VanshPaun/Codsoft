import tkinter as tk

def calculate():
    try:
        result=eval(entry.get())
        show_result(result)
    except Exception as e:
        show_result(f"Error: {str(e)}")

def show_result(result):
    result_window=tk.Toplevel(root)
    result_window.title("Result")

    result_label=tk.Label(result_window,text="Result: "+str(result))
    result_label.pack()

root=tk.Tk()
root.title("Calculator")

entry_label=tk.Label(root, text="Enter the equation:")
entry_label.pack()

entry=tk.Entry(root,width=20)
entry.pack()

calculate_button=tk.Button(root,text="Calculate", command=calculate)
calculate_button.pack()

root.mainloop()
