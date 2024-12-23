from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#ffb7c5"

#days 17->23


# self -> turns this in a property which can be accessed anywhere in the class
#tue  ,false  dn xreiazetai ekei to self giati mono edw tha ine i eikona
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Riddler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="black", bg = THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(150,125, text="", fill=THEME_COLOR, font=("Arial", 13, "italic"), width = 230)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        false_png = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_png, highlightthickness=0, command=self.true_pressed, bd=0)
        self.false_button.grid(column=0, row=2)

        true_png = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_png, highlightthickness=0, command=self.false_pressed, bd=0)
        self.true_button.grid(column=1, row=2)


        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text= "u reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        #is_right = self.quiz.check_answer("True")
        self.give_feedback(self.quiz.check_answer("True"))
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        #we cant mess with time bcause of windowloop -> window.after
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

