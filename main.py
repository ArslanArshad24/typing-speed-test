import random
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

window = tk.Tk()
window.title("Typing Speed")
window.config(padx=5, pady=5, bg=YELLOW,)

title_label = tk.Label(text="TYPING SPEED TEST", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=RED)
title_label.grid(column=0, row=0, columnspan=2, pady=0)

paragraphs = [
    "apple running dragonfly mystic banana whisper sunlight forest mountain shadow purple twilight serene laughter butterfly rainbow piano emerald ocean breeze delicate harmony enchanted meadow river twilight starlight echo midnight whisper fantasy moonbeam butterfly whisperer glowing stardust dreamlike clouds",
    "clouds journey treasure silent autumn wonderland garden light warmth thunder hidden valley blossom tranquility bird song cascading laughter echoing stream dew sparkling serenity whispers dawn rustling leaves adventure stillness radiance autumn twilight glow fireflies whispers moonlight wings radiant golden",
    "whispering stars journey silent shadows mountain path flowing river breeze moonlit night gentle forest petals dawn horizon whispers ancient echoes timeless dream reflection twilight meadow whispers starlit glow petals wings moonbeam soft melody harmony dreams whispering night starry twilight peaceful",
    "midnight forest echoes enchanted moonlight river cascading dreams shimmering mist breeze twilight whispers starry petals dawn reflection shadows whispers moonlit wings dreamlike melody harmony echoes dawn twilight whispers fireflies enchanted stardust petals moonbeam glow night serenade dreams peaceful starry",
    "radiant golden sunlight autumn serenity valley gentle breeze blossoms whispering petals moonlight cascading stars tranquil night wings melody harmony dawn twilight echoes dreams starlight whispers shadows glowing enchanted forest breeze misty river moonlit reflection dreamlike harmony night peaceful",
    "twilight starlight whispers moonlit forest breeze petals glowing echoes dawn serenity night radiant golden autumn sunlight moonlight shadows fireflies cascading gentle dreams wings harmony melody moonbeam tranquil reflection enchanted stardust shimmering mist flowing river dreamlike whispers night",
    "moonlight whispers starry petals dawn twilight echoes dreams starlight shadows glowing enchanted forest breeze misty river moonlit reflection dreamlike harmony night peaceful radiant golden sunlight autumn serenity valley gentle breeze blossoms whispering petals moonlight cascading stars tranquil",
    "dawn twilight whispers fireflies enchanted stardust petals moonbeam glow night serenade dreams peaceful starry midnight forest echoes enchanted moonlight river cascading dreams shimmering mist breeze twilight whispers starry petals dawn reflection shadows whispers moonlit wings dreamlike melody"
]
typing_img = Image.open("typingPic.jpeg")
typing_img = typing_img.resize((300, 114), Image.LANCZOS)
typing_img = ImageTk.PhotoImage(typing_img)
canvas = tk.Canvas(width=300, height=114, highlightthickness=0, bg=YELLOW)
canvas.create_image(150, 57, image=typing_img)
canvas.grid(column=0, row=1, columnspan=2, pady=0)

global time 
time=60

time_label=tk.Label(text=f"You have {time} Seconds", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
time_label.grid(column=0, row=2, columnspan=2, pady=0)

global para
para = random.choice(paragraphs)
paragraph_label = tk.Label(text=para, wraplength=400, height=10, font=(FONT_NAME, 12), bg=YELLOW, fg=RED)
paragraph_label.grid(column=0, row=3, columnspan=2, pady=5)

text_input = tk.Text(height=5, width=40, font=(FONT_NAME, 12))
text_input.grid(column=0, row=4, columnspan=2, pady=10)
text_input.config(state='disabled')
text_input.focus()

global time_running
time_running=False

def start_restart_timer():
    global time_running
    if time_running:
        restart()
    else:
        start_timer()

def start_timer():
    global time_running
    time_running = True
    text_input.config(state='normal')
    text_input.delete("1.0", tk.END)
    start_button.config(text="Restart")
    countdown()

global timer

def restart():
    global time ,time_running,para
    window.after_cancel(timer)
    time = 60
    time_running = False
    time_label.config(text=f"You have {time} Seconds")
    text_input.delete("1.0", tk.END)
    text_input.config(state='normal')
    para = random.choice(paragraphs)
    paragraph_label.config(text=para,wraplength=400, height=10, font=(FONT_NAME, 12), bg=YELLOW, fg=RED)
    paragraph_label.grid(column=0, row=3, columnspan=2, pady=5)
    start_timer()

def countdown():
    global time ,timer
    if time >= 0:
        time_label.config(text=f"You have {time} Seconds")
        time -= 1
        timer = window.after(1000, countdown)
    else:
        timer_running = False
        time_label.config(text=f"Times Up",fg=RED)
        text_input.config(state='disabled')
        text = text_input.get("1.0", tk.END).strip()
        calculate_wpm(text)

def calculate_wpm(text):
    input_words = text.split()
    global para
    para_words = para.split()
    correct_words = [word.lower() for word in input_words if word in para_words]
    wpm = len(correct_words)
    paragraph_label.config(text=f"BOSS!\nYour WPM is {wpm}",wraplength=400, height=5,font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
    paragraph_label.grid(column=0, row=3, columnspan=2, pady=0)

start_button = tk.Button(text="Start", width=15, bg=RED, fg="white", command=start_restart_timer)
start_button.grid(column=0, row=5, pady=10)

def rules():
    messagebox.showinfo(title="Rules/About us", message='''
    Rules:
        \t✔️ Only Correct word will be count
        \t✔️ its Case Sensitive words
        \t✔️ Can write any word from Paragraphs at any place\n
    About us:
        \t🙈 Coding By Arslan Arshad,
        \t\t🔼 A Artificial Intelligence Student
        \t\t🔼 Full Stack Web-Developer
        \t\t🔼 Pyhon Web Scraper
        \t\t🔼 Python Automation

    Coming Soon..
        \t👀 Project Update with classes
        \t👀 New More Projects on GitHub
        \t👀 Stay Connected.......😊
    ''')

rule_button = tk.Button(text="Rules/About us", width=15, bg=GREEN, fg="black", command=rules)
rule_button.grid(column=1, row=5, pady=10)

window.mainloop()