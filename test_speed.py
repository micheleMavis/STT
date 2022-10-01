# typing speed test gui

# importing all libraries 
from tkinter import *
from timeit import default_timer as timer 
import random 

# creating a list of words
words = ['aardvark', 'baboon', 'camel']

# creating a function to get a random word
def get_word():
    word = random.choice(words)
    return word

# creating a function to get the time
def get_time():
    time = timer()
    return time

# creating a function to calculate the typing speed
def calculate_speed():
    global start_time
    global end_time
    global speed
    end_time = get_time()
    speed = round((len(word) / (end_time - start_time)), 2)
    return speed

# creating a function to display the speed
def display_speed():
    global speed
    speed_label.config(text = str(speed) + " words per minute")

# creating a function to start the game
def start_game():
    global start_time
    global word
    word = get_word()
    start_time = get_time()
    word_label.config(text = word)

# creating a function to end the game
def end_game():
    global speed
    calculate_speed()
    display_speed()

# creating a function to reset the game
def reset_game():
    global start_time
    global end_time
    global speed
    global word
    start_time = 0
    end_time = 0
    speed = 0
    word = ""
    word_label.config(text = word)
    speed_label.config(text = speed)

# creating a window
window = Tk()
window.title("Mist")
window.geometry("400x400")

# creating a label for the word
word_label = Label(window, text = "", font = ("Arial", 30))
word_label.pack(pady = 20)

# creating a button to start the game
start_button = Button(window, text = "Start", command = start_game)
start_button.pack(pady = 10)

# creating a button to end the game
end_button = Button(window, text = "End", command = end_game)
end_button.pack(pady = 10)

# creating a button to reset the game
reset_button = Button(window, text = "Reset", command = reset_game)
reset_button.pack(pady = 10)

# creating a label for the speed
speed_label = Label(window, text = "", font = ("Arial", 30))
speed_label.pack(pady = 20)

# running the mainloop
window.mainloop()
