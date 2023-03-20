import csv
import random
import tkinter as tk
from tkinter import messagebox

class Quiz:
    def __init__(self, root, input_file):
        self.root = root
        self.input_file = input_file
        self.questions = []
        self.current_question = 0
        self.score = 0
        self.load_questions()
        self.create_widgets()
    #parses question and answers in from .csv file and the answer/decoys
    def load_questions(self):
        with open(self.input_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                question = row["question"]
                answer = row["answer"]
                decoys = [row["decoy1"], row["decoy2"], row["decoy3"]]
                self.questions.append((question, answer, decoys))
        random.shuffle(self.questions)

    #creates and customizes GUI buttons a text
    def create_widgets(self):
        # Add a close button to the top right corner of the window
        close_button = tk.Button(self.root, text="X", font=("Helvetica", 12, "bold italic"), width=2, height=1, command=self.root.destroy, bg="red", fg="white")
        close_button.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=10)

        # Rest of the code for creating the quiz interface
        self.question_label = tk.Label(self.root, text="", font=("Helvetica",18, "bold italic"), bg="#454545")
        self.question_label.pack(pady=10)
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", font=("Helvetica", 12, "bold italic"), width=50, height=1, bg="#A9A9A9", command=lambda i=i: self.check_answer(i))
            self.option_buttons.append(button)
            button.pack(pady=5)
        self.submit_button = tk.Button(self.root, text="Submit", font=("Helvetica", 12, "bold italic"), width=20, height=1, command=self.check_answer, bg="#A9A9A9")
        self.submit_button.pack(pady=10)
        self.feedback_frame = tk.Frame(self.root)
        self.feedback_label = tk.Label(self.feedback_frame, text="", font=("Verdana", 20, "bold italic"), bg="#454545")
        self.feedback_label.pack(pady=10)
        self.feedback_score_label = tk.Label(self.feedback_frame, text="", font=("Verdana", 15, "bold italic"), bg="#454545")
        self.feedback_score_label.pack(pady=10)
        self.feedback_retry_button = tk.Button(self.feedback_frame, text="Retry Test", font=("Helvetica", 12, "bold italic"), width=30, height=1, bg="#A9A9A9", command=self.retake)
        self.feedback_retry_button.pack(pady=10)
        self.feedback_close_button = tk.Button(self.feedback_frame, text="Close", font=("Helvetica", 12, "bold italic"), width=30, height=1, bg="#A9A9A9", command=self.close)
        self.feedback_close_button.pack(pady=10)


        # Bind hover effects to buttons
        self.submit_button.bind("<Enter>", lambda event: self.submit_button.config(bg="dark green"))
        self.submit_button.bind("<Leave>", lambda event: self.submit_button.config(bg="#A9A9A9"))
        self.feedback_retry_button.bind("<Enter>", lambda event: self.feedback_retry_button.config(bg="dark green"))
        self.feedback_retry_button.bind("<Leave>", lambda event: self.feedback_retry_button.config(bg="#A9A9A9"))
        self.feedback_close_button.bind("<Enter>", lambda event: self.feedback_close_button.config(bg="dark red"))
        self.feedback_close_button.bind("<Leave>", lambda event: self.feedback_close_button.config(bg="#A9A9A9"))



    #shuffles the decoys and answers around 
    def show_question(self):
        question, answer, decoys = self.questions[self.current_question]
        random.shuffle(decoys)
        self.question_label.config(text=question)
        answer_button_index = random.randint(0, 3)
        for i in range(4):
            if i == answer_button_index:
                text = answer
            else:
                text = decoys.pop()
            self.option_buttons[i].config(text=text)

    #runs through user selctions and calculated the results
    def check_answer(self, selected=None):
        if selected is not None:
            selected_option = selected
        else:
            selected_option = 0
        question, answer, decoys = self.questions[self.current_question]
        if self.option_buttons[selected_option].cget("text") == answer:
            self.score += 1
            self.feedback_label.config(text="Congratulations you finished the quiz!!")
        else:
            self.feedback_label.config(text="Congratulations you finished the quiz!!")
        self.feedback_score_label.config(text="You Scored: {}% ({}/{})".format(round(self.score/len(self.questions)*100), self.score, len(self.questions)))
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.show_feedback()

    def show_feedback(self):
        self.question_label.pack_forget()
        for button in self.option_buttons:
            button.pack_forget()
        self.submit_button.pack_forget()
        self.feedback_frame.pack(pady=50)
        self.feedback_label.pack(pady=10)
        self.feedback_score_label.pack(pady=10)
        self.feedback_retry_button.pack(pady=10)
        self.feedback_close_button.pack(pady=10)
        self.feedback_frame.configure(bg="#454545")
    #button that allows for users to retake the test/survey if needed
    def retake(self):
        self.current_question = 0
        self.score = 0
        random.shuffle(self.questions)
        self.root.destroy()
        new_root = tk.Tk()
        new_root.title("Trivia Quiz")
        new_root.geometry("500x500")
        new_root.configure(bg="#454545")
        new_quiz = Quiz(new_root, self.input_file)
        new_quiz.show_question()
        new_root.mainloop()

    #closes the GUI app
    def close(self):
        self.root.destroy()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python quiz.py input_file.csv")
        sys.exit(1)
    root = tk.Tk()
    root.title("Trivia Quiz")
    root.geometry("2000x700")
    root.configure(bg="#454545")
    quiz = Quiz(root, sys.argv[1])
    quiz.show_question()
    root.mainloop()