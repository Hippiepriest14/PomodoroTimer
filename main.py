from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
mark = ""
tim = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global rep
    global mark
    window.after_cancel(tim)
    label.config(text="TIMER",fg=GREEN)
    canvas.itemconfig(timer, text="00:00")
    check_mark.config(text="")
    mark = ""
    rep = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep
    global mark
    rep+=1

    if rep == 8:
        count_down(LONG_BREAK_MIN*60)
        label.config(text="BREAK", fg=RED)
        mark += "✔"
        check_mark.config(text=mark)
    elif rep%2==0:
        count_down(SHORT_BREAK_MIN*60)
        label.config(text="BREAK", fg=PINK)
        mark += "✔"
        check_mark.config(text=mark)
    else:
        count_down(WORK_MIN*60)
        label.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global tim
        tim = window.after(1000, count_down, count - 1)

    else:
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

button_start = Button(text="Start", width=5, command=start_timer)
button_start.grid(column=0, row=3)
button_reset = Button(text="Reset", width=5,command=reset)
button_reset.grid(column=3, row=3)

label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
label.grid(column=2, row=0)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=2, row=4)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

window.mainloop()
