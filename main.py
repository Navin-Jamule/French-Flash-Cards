from tkinter import *
from pandas import *
import random

BACKGROUND_COLOR = "#B1DDC6"
#----- .csv file to dataFrame ---- Stage 2
try:
    data = read_csv("./data/Words_to_learn.csv") #if file is not present
except FileNotFoundError:
    data = read_csv("./data/french_words.csv")  #use this file

dict_data = data.to_dict(orient='records') #converting data to dictionary
Current_word = {}

# ----- Random Selection of French Words ------ Stage 3
# used to generate random words
def word_selection():
    global Current_word, flip_timer

    window.after_cancel(flip_timer)       #cancel the running timer
    Current_word = random.choice(dict_data)  #get the dictionary
    french_word = Current_word['French']      #from current word dictionary access the french word
    canva.itemconfig(title_text, text = 'French',fill = 'black') #title change
    canva.itemconfig(word_text,text=french_word, fill = 'black') #present the french_word
    canva.itemconfig(img_background, image = front_card_img)     #change img
    flip_timer = window.after(3000, func = flip_card)        #restart the 3 sec timer

#--- Flipping logic ---
#onces three seconds is completed show the english meaning by fliping the card
def flip_card():
    canva.itemconfig(title_text, text = 'English',fill='white')   #title change
    canva.itemconfig(word_text,text=Current_word['English'],fill='white') #from the current word dictionary access the english meaning
    canva.itemconfig(img_background, image = back_card_img)  #change the image

#--- word known logic ---
#when word is known
def is_known():
    dict_data.remove(Current_word) #remove that word from main data
    updated_data = DataFrame(dict_data) #update the data
    updated_data.to_csv("./data/Words_to_learn.csv",index = False) #create a new file which contant only word that you dont know
    word_selection()   #new word generation


#------ UI ------ :Stage 1
window = Tk()
window.title('Flash Card')
window.config(padx = 50, pady = 50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func = flip_card) #timer of 3 secs then flip card

canva = Canvas(height=525, width=800)
front_card_img = PhotoImage(file='./images/card_front.png')
back_card_img = PhotoImage(file='./images/card_back.png')
img_background = canva.create_image(5, 5, anchor=NW, image=front_card_img)
canva.config(bg = BACKGROUND_COLOR, highlightthickness = 0)
title_text = canva.create_text(400, 150, text ='French',font=('Arial',40,'italic'))
word_text = canva.create_text(400,263,font=('Arial',60,'bold'))
canva.grid(row=0, column=0, columnspan=2)
word_selection()

#--- buttons ---
#right button logic
right_button_img = PhotoImage(file='./images/right.png')
right_button = Button(image=right_button_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

#wrong button logic
wrong_button_img = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=word_selection)
wrong_button.grid(row=1, column=0)

window.mainloop()
