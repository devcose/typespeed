from tkinter import *
from examples import paragraphs
from random import randint, choice
from PIL import Image, ImageTk
import classes
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLUE = '#1663be'
BLACK = '#000000'
FONT_NAME = "Courier"
timer = None
current_text = ""




def start_timer(count):
    global timer
    global current_text
    timer = window.after(20, start_timer, count + 0.02)
    timer_label.config(text="{:.2f}".format(count))

    user_text = text_box.get("1.0", 'end-1c')
    user_text_len = len(user_text)
    print(user_text_len)
    progress = int(user_text_len / len(current_text) * 100)
    progress_label.config(text=f"%{progress}")
    correct = check_correct(user_text, current_text, user_text_len)
    if correct and progress == 100:
        complete(count)

def new_phrase():
    ## Generate new Card
    text_box.delete('1.0', END)
    start_button.config(text='Reset')
    global current_text
    current_text = choice(paragraphs)
    canvas.itemconfig(canvas_paragraph, text=current_text)


    start_timer(0)


def check_correct(u_text, text, length):
    if u_text[:length] == text[:length]:
        window.config(bg=GREEN)
        return True
    else:
        window.config(bg=RED)
        return False


def complete(count):
    global timer
    window.after_cancel(timer)
    words_in_p = len(current_text.split(' '))
    wps = words_in_p / count
    wpm = int(wps * 60)
    progress_label.config(text=f"WPM: {wpm}")








def submit():
    pass


## Creating Window
window = Tk()
window.title('typing speed')
window.geometry("800x600")
window.config(pady=50, padx=50, bg=GREEN)

# e = classes.Sizer(window)
# e.pack(fill=BOTH, expand=YES)


#### Typing Canvas ####
canvas = Canvas(width=700, height=260 , bg=GREEN, highlightthickness=0)
img = Image.open('card_front.png')
## Resize Image ##
resized_img = img.resize((500,205), Image.ANTIALIAS)
card_background = ImageTk.PhotoImage(resized_img)
canvas.create_image(100,10, anchor=NW, image=card_background)
canvas.grid(column=0, row=1, sticky=W, columnspan=2)
canvas_title = canvas.create_text(350, 30, text='Type Me', font=("Arial", 20, "bold"))
canvas_paragraph = canvas.create_text(340,100,justify=CENTER, width=400, text='paragraph here a very long paragraph with lots of test and stuff', font=('Arial', 15, 'normal'))



#### Labels #####

timer_label = Label(text="Typing Speed",pady=10, fg=BLACK, bg=GREEN, font=(FONT_NAME, 50 , "normal"))
timer_label.grid(column=0, row=0, padx=(100,0))
progress_label = Label(text="",pady=10, fg=BLACK, bg=GREEN, font=(FONT_NAME, 50 , "normal"))
progress_label.grid(column=1, row=0, padx=(0,0), sticky=W)

## Buttons ##
start_button = Button(text="start", bg="white", highlightthickness=0, command=new_phrase)
start_button.grid(column=0, row=3, sticky=W, padx=150)
# stop_button = Button(text="reset", bg="white", highlightthickness=0, command=submit)
# stop_button.grid(column=1, row=3, sticky=W, padx=(0,150))

## Text Box
text_box = Text(window, height=5, width=70, pady=20)
text_box.grid(column=0, row=2, sticky=W, padx=100, pady=(0,30), columnspan=2)

window.mainloop()