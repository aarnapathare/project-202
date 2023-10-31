from tkinter import * 
window = Tk()

window.title('Simple Interest Calculator')
window.geometry("380x400")
window.configure(bg='white')

def calculate_int():
    p = float(principle.get())
    r = float(rate.get())
    t = float(time.get())
    i = (p*r*t)/100
    interest = round(i,2)

    msg=""
    output_message = Label(result_frame, text=", your answer is "+str(int)+"and"+msg,bg="lightcyan",font=("Calibri", 12), width=42)
    output_message.place(x=20, y=40)
    output_message.pack()

app_label=Label(window, text="Simple Interest Calculator", fg="black", bg="lightcyan", font=("Calibri", 20), bd=5)
app_label.place(x=50, y=20)

window_label=Label(window, text="Write Here", fg="black", bg="lightcyan", font=("Calibri", 12), bd=1)
window_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

calculate_button=Button(window, text="CALCULATE", fg="black", bg="cyan", bd=4, command=calculate_int)
calculate_button.place(x=20, y=250)

result_frame = LabelFrame(window, text="Result", bg="lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20, y=300)

result_label = Label(result_frame,text=" ", bg="lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20, y=20)
result_label.pack()

window.mainloop()