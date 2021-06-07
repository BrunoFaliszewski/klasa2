from tkinter import *
import os
from pathlib import Path
from random import randrange

root = Tk()
root.title("Flaszki v0.0.1")
# root.geometry("280x430")


def dir_struct(d_l: list):
    path_home = os.path.abspath(os.getcwd())
    path = Path("./content")

    for p in path.iterdir():
        if p.is_dir():
            print(p)
            d_l.append(p)
            print()
            os.chdir(path_home)


def add_content(path):
    with open(path) as plik:
        tekst = plik.readlines()
        i = 0
        for linia in tekst:
            if(i % 2):
                if(linia[-1] == '\n'):
                    list_eng.append(linia[:-1])
                else:
                    list_eng.append(linia)
            else:
                if(linia[-1] == '\n'):
                    list_pol.append(linia[:-1])
                else:
                    list_pol.append(linia)
            i += 1


def clicked_load_content(value):
    global card_index_max
    list_pol.clear()
    list_eng.clear()
    print(f"{value}")
    path = value + "\slowa.txt"
    if(var_words.get()):
        add_content(path)
    path = value + "\wyrazenia.txt"
    if(var_expressions.get()):
        add_content(path)
    path = value + "\zdania.txt"
    if(var_sentences.get()):
        add_content(path)
    path = value + "\pytania.txt"
    if(var_questions.get()):
        add_content(path)

    card_index_max = len(list_pol) - 1

    update_buttons_state()
    update_cards_text()

    print(f"lista_pol: {list_pol}")
    print(f"lista_eng: {list_eng}")

    print(f"var_slowa.get(): {var_words.get()}")
    print(f"var_wyrazenia.get(): {var_expressions.get()}")

    print(f"card_index_max: {card_index_max}")


def clicked_next():
    global card_index
    global card_index_max
    if(card_index < card_index_max):
        card_index += 1

    update_buttons_state()
    update_cards_text()

    print(f"card_index: {card_index}")


def update_buttons_state():
    global card_index
    global card_index_max

    if (card_index_max >= 1):
        b_random['state'] = NORMAL
        b_place['state'] = NORMAL
        if(card_index == 0):
            b_previous['state'] = DISABLED  # tkinter.DISABLED
            b_next['state'] = NORMAL  # tkinter.DISABLED
        elif(card_index == card_index_max):
            b_previous['state'] = NORMAL
            b_next['state'] = DISABLED
        else:
            b_previous['state'] = NORMAL
            b_next['state'] = NORMAL
    else:
        b_random['state'] = DISABLED
        b_previous['state'] = DISABLED
        b_next['state'] = DISABLED
        if(len(list_pol) == 0):
            b_place['state'] = DISABLED
        else:
            b_place['state'] = NORMAL

    if var_single_side.get() and len(list_pol) > 0:
        b_change_side['state'] = NORMAL
    else:
        b_change_side['state'] = DISABLED

    print(f"card_index: {card_index}")
    print(f"card_index_max: {card_index_max}")


def update_cards_text():
    global card_index

    if len(list_pol) > 0 and var_single_side.get() == 0:
        text_pol.set(list_pol[card_index])
        text_eng.set(list_eng[card_index])
        text_status.set(f"Card {card_index + 1} of {card_index_max + 1}")
    elif len(list_pol) > 0 and var_single_side.get() == 1:
        if (var_side_pol_neng.get() == 1):
            text_pol.set("")
            text_eng.set(list_eng[card_index])
        else:
            text_pol.set(list_pol[card_index])
            text_eng.set("")
        text_status.set(f"Card {card_index + 1} of {card_index_max + 1}")
    else:
        text_pol.set("Gratuluję!")
        text_eng.set("Congratulations!")
        text_status.set(f"Card {card_index} of {card_index_max}")


def clicked_previous():
    global card_index
    global card_index_max
    if(card_index > 0):
        card_index -= 1

    update_buttons_state()
    update_cards_text()

    print(f"card_index: {card_index}")


def clicked_random():
    global card_index
    global card_index_max

    card_index = randrange(card_index_max + 1)

    var_side_pol_neng.set(randrange(2))
    update_buttons_state()
    update_cards_text()

    print(f"card_index: {card_index}")


def clicked_change_side():
    if var_side_pol_neng.get():
        var_side_pol_neng.set(0)
    else:
        var_side_pol_neng.set(1)

    update_buttons_state()
    update_cards_text()


def clicked_place():
    global card_index
    global card_index_max

    if len(list_pol) > 0:
        del list_pol[card_index]
        del list_eng[card_index]

    if len(list_pol) > 0:
        card_index_max = len(list_pol) - 1
        card_index = randrange(card_index_max + 1)
    else:
        card_index_max = 0
        card_index = 0

    update_buttons_state()
    update_cards_text()

    print(f"card_index: {card_index}")


list_pol = []
list_eng = []
card_index = 0
card_index_max = 0
text_pol = StringVar()
text_pol.set("Polish Text")
text_eng = StringVar()
text_eng.set("English Text")
text_status = StringVar()
text_status.set(f"Card {card_index + 1} of {card_index_max + 1}")


# Drop Down Boxes
dir_val = StringVar()
dir_val.set("Wybierz rozdział")

drop_list = []
dir_struct(drop_list)

drop = OptionMenu(root, dir_val, *drop_list)
drop.grid(row=0, column=2)


frame = LabelFrame(root, text="Co chcesz ćwiczyć?", padx=5, pady=5)
frame.grid(row=1, column=2, padx=10, pady=10)  # .pack(padx=10, pady=10)

var_words = IntVar()
var_expressions = IntVar()
var_sentences = IntVar()
var_questions = IntVar()

var_words.set(1)
var_expressions.set(1)
var_sentences.set(1)
var_questions.set(1)

c_words = Checkbutton(frame, text="słowa", variable=var_words)
c_expressions = Checkbutton(frame, text="wyrażenia", variable=var_expressions)
c_sentences = Checkbutton(frame, text="zdania", variable=var_sentences)
c_questions = Checkbutton(frame, text="pytania", variable=var_questions)

c_words.grid(row=1, column=2)  # .pack()
c_expressions.grid(row=2, column=2)
c_sentences.grid(row=3, column=2)
c_questions.grid(row=4, column=2)

var_single_side = IntVar()
var_side_pol_neng = IntVar()
var_single_side.set(0)
var_side_pol_neng.set(1)
c_single_side = Checkbutton(
    root, text="Widoczna jedna strona", variable=var_single_side,
    command=lambda: clicked_change_side())
c_single_side.grid(row=5, column=2)


b_load_content = Button(root, text="Wczytaj zawartosc!",
                        command=lambda: clicked_load_content(dir_val.get()))
b_load_content.grid(row=6, column=2)


b_next = Button(root, text=">>",
                command=lambda: clicked_next(), pady=5)
b_next.grid(row=7, column=4)


b_previous = Button(root, text="<<",
                    command=lambda: clicked_previous(), pady=5)
b_previous.grid(row=7, column=0)

# Creating a Label Widget
l_pol = Label(root, textvariable=text_pol,
              font=('bold', 14), pady=10, width=20)
l_eng = Label(root, textvariable=text_eng,
              font=('bold', 14), pady=10, width=20)

# Showing it onto the screen
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=0)
l_pol.grid(row=11, column=2)
l_eng.grid(row=12, column=2)

status = Label(root, textvariable=text_status)
status.grid(row=13, column=2)


b_change_side = Button(root, text="Odwróć kartę",
                       command=lambda: clicked_change_side())
b_change_side.grid(row=10, column=2)


b_random = Button(root, text="Losowa",
                  command=lambda: clicked_random())
b_random.grid(row=7, column=2)


b_place = Button(root, text="Odłóż kartę",
                 command=lambda: clicked_place())
b_place.grid(row=9, column=2)

root.mainloop()
