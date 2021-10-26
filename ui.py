from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.windows = Tk()
        self.windows.title("Quiz Brain")
        self.windows.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label(text=f"score:0", padx=20, pady=20, fg="white", bg=THEME_COLOR)
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125,
                                text="text",
                                width=250,
                                font=("Arial", 20, "bold"),
                                fill="black"
                                )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.image_true = PhotoImage(file="images/true.png")
        self.button = Button(image=self.image_true, command=self.show_question)
        self.button.grid(row=2, column=0)

        self.image_false = PhotoImage(file="images/false.png")
        self.button = Button(image=self.image_false, command=self.show_question)
        self.button.grid(row=2, column=1)

        self.windows.mainloop()

    def show_question(self, question):
        self.canvas.itemconfigure(self.question, question, fill="black")



