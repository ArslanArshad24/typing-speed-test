import random
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

class TypingSpeedTest:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Typing Speed Test")
        self.window.config(padx=20, pady=20, bg=YELLOW)

        # Title
        self.title_label = tk.Label(text="TYPING SPEED TEST", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=RED)
        self.title_label.grid(column=0, row=0, columnspan=2, pady=10)

        # Paragraphs
        self.paragraphs = [
            "apple running dragonfly mystic banana whisper sunlight forest mountain shadow purple twilight serene laughter butterfly rainbow piano emerald ocean breeze delicate harmony enchanted meadow river twilight starlight echo midnight whisper fantasy moonbeam butterfly whisperer glowing stardust dreamlike clouds",
            "clouds journey treasure silent autumn wonderland garden light warmth thunder hidden valley blossom tranquility bird song cascading laughter echoing stream dew sparkling serenity whispers dawn rustling leaves adventure stillness radiance autumn twilight glow fireflies whispers moonlight wings radiant golden",
            "whispering stars journey silent shadows mountain path flowing river breeze moonlit night gentle forest petals dawn horizon whispers ancient echoes timeless dream reflection twilight meadow whispers starlit glow petals wings moonbeam soft melody harmony dreams whispering night starry twilight peaceful",
            "midnight forest echoes enchanted moonlight river cascading dreams shimmering mist breeze twilight whispers starry petals dawn reflection shadows whispers moonlit wings dreamlike melody harmony echoes dawn twilight whispers fireflies enchanted stardust petals moonbeam glow night serenade dreams peaceful starry",
            "radiant golden sunlight autumn serenity valley gentle breeze blossoms whispering petals moonlight cascading stars tranquil night wings melody harmony dawn twilight echoes dreams starlight whispers shadows glowing enchanted forest breeze misty river moonlit reflection dreamlike harmony night peaceful",
            "twilight starlight whispers moonlit forest breeze petals glowing echoes dawn serenity night radiant golden autumn sunlight moonlight shadows fireflies cascading gentle dreams wings harmony melody moonbeam tranquil reflection enchanted stardust shimmering mist flowing river dreamlike whispers night",
            "moonlight whispers starry petals dawn twilight echoes dreams starlight shadows glowing enchanted forest breeze misty river moonlit reflection dreamlike harmony night peaceful radiant golden sunlight autumn serenity valley gentle breeze blossoms whispering petals moonlight cascading stars tranquil",
            "dawn twilight whispers fireflies enchanted stardust petals moonbeam glow night serenade dreams peaceful starry midnight forest echoes enchanted moonlight river cascading dreams shimmering mist breeze twilight whispers starry petals dawn reflection shadows whispers moonlit wings dreamlike melody"
        ]

        # Image
        self.image_1 = Image.open("typingPic.jpeg")
        self.image_1 = self.image_1.resize((300, 114), Image.LANCZOS)
        self.image_1 = ImageTk.PhotoImage(self.image_1)
        self.canvas = tk.Canvas(width=300, height=114, highlightthickness=0, bg=YELLOW)
        self.canvas.create_image(150, 57, image=self.image_1)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=10)

        # Paragraph display
        self.para = self.get_para()
        self.paragraph_label = tk.Label(text=self.para, wraplength=400, height=10, font=(FONT_NAME, 12), bg=YELLOW, fg=GREEN)
        self.paragraph_label.grid(column=0, row=2, columnspan=2, pady=10)

        # Timer
        self.time = 20
        self.timer_running = False
        self.timer_label = tk.Label(text=f"Time Left: {self.time}", font=(FONT_NAME, 12), bg=YELLOW, fg=RED)
        self.timer_label.grid(column=0, row=3, pady=10)

        # Text input
        self.text_input = tk.Text(height=8, width=50, font=(FONT_NAME, 12))
        self.text_input.grid(column=0, row=4, columnspan=2, pady=10)
        self.text_input.config(state='disabled')  # Initially disabled
        self.text_input.focus()

        # Start/Restart button
        self.start_button = tk.Button(text="Start", width=15, bg=RED, fg="white", command=self.start_restart_timer)
        self.start_button.grid(column=0, row=5, pady=10)

        # Result label
        self.result_label = tk.Label(text="", font=(FONT_NAME, 14), bg=YELLOW, fg=GREEN)
        self.result_label.grid(column=0, row=6, columnspan=2, pady=10)

        self.window.mainloop()

    def start_restart_timer(self):
        if self.timer_running:
            self.restart()
        else:
            self.start_timer()

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.text_input.config(state='normal')  # Enable the text input field
            self.start_button.config(text="Restart")
            self.text_input.delete("1.0", tk.END)  # Clear the input data
            self.countdown()

    def countdown(self):
        if self.time > 0:
            self.timer_label.config(text=f"Time Left: {self.time}")
            self.time -= 1
            self.timer = self.window.after(1000, self.countdown)
        else:
            self.timer_running = False
            messagebox.showinfo(title="Timer", message="Your 120 seconds have ended")
            self.text_input.config(state='disabled')  # Disable the text input field
            self.get_text()

    def get_para(self):
        return random.choice(self.paragraphs)

    def get_text(self):
        text = self.text_input.get("1.0", tk.END).strip()
        self.calculate_wpm(text)

    def calculate_wpm(self, text):
        input_words = text.split()
        para_words = self.para.split()
        correct_words = [word for word in input_words if word in para_words]
        wpm = len(correct_words) / 2  # Since the time is 2 minutes (120 seconds)
        self.result_label.config(text=f"Words per minute (WPM): {wpm}")

    def restart(self):
        self.window.after_cancel(self.timer)
        self.timer_running = False
        self.time = 20
        self.timer_label.config(text=f"Time Left: {self.time}")
        self.text_input.delete("1.0", tk.END)
        self.text_input.config(state='normal')  # Enable the text input field
        self.para = self.get_para()
        self.paragraph_label.config(text=self.para)
        self.result_label.config(text="")  # Clear the previous result
        self.start_timer()

if __name__ == "__main__":
    play = TypingSpeedTest()
