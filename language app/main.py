BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random




countdown_active = False

try:
    words_data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    words_data = pandas.read_csv("data.csv")
finally:
    norsk = words_data.norwegian
    english = words_data.english


norsk_list_learn = []
english_list_learn = []

norsk_word = ""
english_word = ""




norsk_list = norsk.to_list()
english_list = english.to_list()
NUMBERS = len(norsk_list)
word_number = random.randint(0,NUMBERS-1)
def button_work_wrong():
    global countdown_active, timer
    generate_word()
    count_down(3)


def button_work_right():
    global NUMBERS, word_number, norsk_list_learn, english_list_learn, timer, countdown_active
    del norsk_list[word_number]
    del english_list[word_number]
    norsk_list_learn = norsk_list
    english_list_learn = english_list
    data_frame = pandas.DataFrame({"norwegian": norsk_list_learn, "english": english_list_learn})
    data_frame.to_csv("words_to_learn.csv")
    NUMBERS -= 1
    generate_word()
    count_down(3)



def generate_word():
    global word_number
    canvas.itemconfig(language_text, text="Norwegian", fill="black")
    canvas.itemconfig(page, image=card_front_img)
    global english_word, norsk_word, word
    word_number = random.randint(0,NUMBERS-1)
    norsk_word = norsk_list[word_number]
    english_word = english_list[word_number]
    canvas.itemconfig(word, text=norsk_word, fill="black")
def count_down(count):
    global timer
    timer = window.after(1000, count_down, count - 1)
    if count == 0:
        change_page()
        canvas.itemconfig(language_text, text="English", fill="white")
        canvas.itemconfig(word, text=english_list[word_number], fill="white")




def change_page():
    global card_back_img
    canvas.itemconfig(page, image=card_back_img)

window = Tk()
window.title("Flashy Language app")
window.config(padx=50, pady = 50, bg=BACKGROUND_COLOR)



canvas = Canvas(width=800, height=526)
card_front_img= PhotoImage(file="images\card_front.png")
page = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, columnspan=2, row=0)

wrong_image = PhotoImage(file="images\\wrong.png")
no_button = Button(image=wrong_image, highlightthickness=0, command=button_work_wrong)
no_button.grid(column=0, row=1)

right_image = PhotoImage(file="images\\right.png")
yes_button = Button(image=right_image, highlightthickness=0, command=button_work_right)
yes_button.grid(column=1, row=1)

card_back_img = PhotoImage(file="images\\card_back.png")

language_text = canvas.create_text(400, 150, text="Norwegian", fill="black", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text=norsk_list[word_number], fill="black", font=("Arial", 60, "bold"))





if NUMBERS == 0:
    print("That's all the numbers!")

window.mainloop()