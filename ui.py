from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(padx=20, pady=50, background=THEME_COLOR)
        self.window.title("Quizzler")

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, command=self.true_pressed)
        self.true_button.grid(column=0, row=2, pady=10, padx=10)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, command=self.false_pressed)
        self.false_button.grid(column=1, row=2, pady=10, padx=10)

        self.main_canvas = Canvas(width=300, height=250)
        self.main_canvas.grid(column=0, row=1, columnspan=2)
        self.question_text = self.main_canvas.create_text(150, 125,
                                                          width=280,
                                                          text="Answer the question here",
                                                          font=("Arial", 20, "italic"))

        self.score_text = Label(text="Score: 0",
                                font=("Times New Roman", 10,),
                                background=THEME_COLOR,
                                foreground="white")

        self.score_text.grid(row=0, column=1, pady=10, padx=10)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.main_canvas.config(background="white")
        self.score_text.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            self.main_canvas.config(background="white")
            q_text = self.quiz.next_question()
            self.main_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.main_canvas.itemconfig(self.question_text, text="You've got finished the test")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def give_feedback(self, answer_is_right):
        color = "lightgreen" if answer_is_right else "red"
        self.main_canvas.config(background=color)
        self.window.after(ms=500, func=self.get_next_question)

    def button_pressed(self, text_answer: str):
        is_right = self.quiz.check_answer(text_answer)
        self.give_feedback(is_right)

    def false_pressed(self):
        self.button_pressed("False")

    def true_pressed(self):
        self.button_pressed("True")
