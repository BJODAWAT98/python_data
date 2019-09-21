from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import pymysql
from PIL import ImageTk, Image

db = pymysql.connect("localhost", "root", "", "quiz_database")
cursor = db.cursor()
sql = "select question_no,question,option_a,option_b,option_c,option_d,answer from quiz_question_answers ORDER BY RAND() LIMIT 5"
cursor.execute(sql)
question_list = cursor.fetchall()
db.commit()
q = []
options = []
answer = []

for i in range(0, len(question_list)):
    ab = question_list[i]
    option_a = []
    for sub_option in range(2, 6):
        option_a.append(ab[sub_option])
    options.append(option_a)
    q.append(ab[1])
    answer.append(ab[6])
a = []
for element in range(0, len(answer)):
    if answer[element] == 'a':
        a.append(1)
    elif answer[element] == 'b':
        a.append(2)
    elif answer[element] == 'c':
        a.append(3)
    else:
        a.append(4)
print(a)

class Quiz:
    def __init__(self, master):
        self.opt_selected = StringVar()
        self.qn = 0
        self.correct = 0
        self.ques = self.create_q(master, self.qn)
        self.opts = self.create_options(master, 4)
        self.display_q(self.qn)
        self.button = Button(master, text="Next", command=self.next_btn)
        self.button.pack(side=BOTTOM)

    def create_q(self, master, qn):
        w = Label(master, text=q[qn])
        w.pack(side=TOP)
        return w

    def create_options(self, master, n):
        b_val = 0
        opt_selected = 1
        b = []
        while b_val < n:
            btn = Radiobutton(master, text="foo", variable=self.opt_selected, value=b_val + 1, )
            b.append(btn)
            btn.pack(side=TOP, anchor="w")
            b_val = b_val + 1
        return b


    def display_q(self, qn):
        b_val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1

    def check_q(self, qn ):
        if self.opt_selected.get() == str(a[qn]):

            return True
        else:

            return False

    def print_results(self):

        mb.showinfo("marks","your score is %d "%(self.correct))

    def next_btn(self):
        if self.check_q(self.qn):
            print("Correct")
            self.correct += 1
        else:
            print("Wrong")

        self.qn = self.qn + 1
        if self.qn >= len(q):
            self.print_results()
        else:
            self.display_q(self.qn)
    print("X"*15)


if __name__ == "__main__":
    play_screen: Tk = Tk()
    play_screen.geometry("500x300")
    play_screen.title("Play")
    app = Quiz(play_screen)
    play_screen.mainloop()
