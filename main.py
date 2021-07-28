# Flash Card Learning Game French-English
# Author >>> Yago Alexandre

import pandas as pd
from tkinter import *
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ('Arial', 40, 'italic')
TEXT_FONT = ('Arial', 60, 'bold')

french_words = pd.read_csv('./data/french_words.csv')
words_dict = french_words.to_dict(orient='records')
current_card = {}


# ---------------------------- FUNCTION SETUP ---------------------------- #
def change_word():
    global current_card

    current_card = choice(words_dict)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(title_label, text='French', fill='Black')
    canvas.itemconfig(text_label, text=current_card['French'], fill='Black')
    root.after(2000, flip_card)


def flip_card():
    english_word = choice(words_dict)
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title_label, text='English', fill='White')
    canvas.itemconfig(text_label, text=english_word['English'], fill='White')


def press_checkmark():
    global current_card
    words_dict.remove(current_card)
    change_word()


# ---------------------------- UI SETUP ---------------------------- #
root = Tk()
root.title("Flashy")
root.minsize(width=900, height=650)
root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
root.resizable(False, False)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_back = PhotoImage(file='images/card_back.png')
card_front = PhotoImage(file='images/card_front.png')
canvas_image = canvas.create_image(400, 264, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

right_button_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_button_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=press_checkmark)
right_button.grid(row=1, column=1, padx=50, pady=20)

wrong_button_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_button_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=change_word)
wrong_button.grid(row=1, column=0, padx=50, pady=20)

title_label = canvas.create_text(400, 150, text="", font=TITLE_FONT)
text_label = canvas.create_text(400, 270, text=f"", font=TEXT_FONT)

# -------------- First Card -------------- #
root.after(500, change_word)
root.mainloop()
