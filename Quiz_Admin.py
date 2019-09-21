from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import pymysql
from PIL import ImageTk, Image



root = Tk()
root.title("Student Registration Form")
root.geometry("500x500")
root.configure(bg="azure")
root.resizable(0,0)


def playmodule():
    pass
def mainpage():   # After successfully login quiz main page of menu

    main_page = Tk()
    main_page.title("welcome page")
    #main_page.resizable(0, 0)
    main_page.geometry("500x500")
    main_page.configure(bg="azure")


    def Insertquestion():
        def insert_question():
            enterd_question = question_text.get("1.0", "end-1c")
            enterd_option_A = option_a_text.get("1.0", "end-1c")
            enterd_option_B = option_b_text.get("1.0", "end-1c")
            enterd_option_C = option_c_text.get("1.0", "end-1c")
            enterd_option_D = option_d_text.get("1.0", "end-1c")
            enterd_answer = qanswer_entry.get()

            if enterd_answer == "a" or enterd_answer == "b" or enterd_answer == "c" or enterd_answer == "d":
                db = pymysql.connect("localhost", "root", "", "quiz_database")

                cursor = db.cursor()
                sql = "insert into quiz_question_answers(question,option_a,option_b,option_c,option_d, answer) values ('%s','%s','%s','%s','%s','%s') " \
                      % (enterd_question, enterd_option_A, enterd_option_B, enterd_option_C, enterd_option_D,
                         enterd_answer)
                r = cursor.execute(sql)
                if r > 0:
                    mb.showinfo("", "Question inserted successfully.")
                else:
                    mb.showinfo("", "Question not inserted .")
                db.commit()
            else:
                mb.showerror("", "enter data properly.")

        tk = Tk()
        Question_insertion = tk
        Question_insertion.title("welcome page")
        Question_insertion.geometry("500x500")
        Question_insertion.configure(bg="azure")

        question_header = Label(Question_insertion, text="   ENTER QUESTION DETAIL     ", bg="sky blue",
                                fg="black", font=('Arial Black', 17, "bold", "italic"))
        question_header.place(x=70, y=20)

        question_text = Text(Question_insertion)
        question_text.place(x=20, y=80, width=460, height=70)
        question_text.insert(END, "Enter the question")


        option_a_text = Text(Question_insertion)
        option_a_text.place(x=30, y=170, width=200, height=40)
        option_a_text.insert(END, 'Option A')

        option_b_text = Text(Question_insertion)
        option_b_text.place(x=250, y=170, width=200, height=40)
        option_b_text.insert(END, 'Option b')

        option_c_text = Text(Question_insertion)
        option_c_text.place(x=30, y=250, width=200, height=40)
        option_c_text.insert(END, 'Option c')

        option_d_text = Text(Question_insertion)
        option_d_text.place(x=250, y=250, width=200, height=40)
        option_d_text.insert(END, 'Option D')

        qanswer_entry = Entry(Question_insertion)
        qanswer_entry.place(x=180, y=320, )
        qanswer_entry.insert(0, 'answer')
        comment_label = Label(Question_insertion, text="only a,b,c and d is allowed",
                              font=('Arial Black', 9, "bold", "italic"))
        comment_label.place(x=300, y=320)

        question_submit_button = Button(Question_insertion, text="SUBMIT", font=(10), command=insert_question)
        question_submit_button.place(x=200, y=350)
        Question_insertion.mainloop()



    def main_update_question():
        def find_question():
            db = pymysql.connect("localhost", "root", "", "quiz_database")
            cursor = db.cursor()
            def update_question_in_database():

                get_question_detail = int(update_question_entry.get())
                enterd_question = question_text.get("1.0", "end-1c")
                enterd_option_A = option_a_text.get("1.0", "end-1c")
                enterd_option_B = option_b_text.get("1.0", "end-1c")
                enterd_option_C = option_c_text.get("1.0", "end-1c")
                enterd_option_D = option_d_text.get("1.0", "end-1c")
                enterd_answer = qanswer_entry.get()

                if enterd_answer == "a" or enterd_answer == "b" or enterd_answer == "c" or enterd_answer == "d":
                    db = pymysql.connect("localhost", "root", "", "quiz_database")

                    cursor = db.cursor()

                    spl = "delete from quiz_question_answers where question_no='%d'" % get_question_detail
                    sql = "insert into quiz_question_answers(question_no,question,option_a,option_b,option_c,option_d, answer) values (%d,'%s','%s','%s','%s','%s','%s') " \
                          % (get_question_detail, enterd_question, enterd_option_A, enterd_option_B, enterd_option_C,
                             enterd_option_D,
                             enterd_answer)
                    cursor.execute(spl)
                    r = cursor.execute(sql)
                    if r > 0:
                        mb.showinfo("", "Question updated successfully.")
                    else:
                        mb.showinfo("", "Question not not updated .")
                    db.commit()
            try:
                get_question_detail = int(update_question_entry.get())

                sql = "select * from quiz_question_answers where question_no=%d" % get_question_detail
                cursor.execute(sql)
                r = (cursor.fetchall())
                if len(r) < 1:
                    mb.showerror("", "question is not in database")
                else:

                    q_tuple = r[0]

                    enterd_question_frame = Frame(update_question_page, width=768, height=576)

                    question_header = Label(enterd_question_frame, text="        UPDATE DETAILS         ", bg="sky blue",
                                            fg="black", font=('Arial Black', 13, "italic"))
                    question_header.place(x=100, y=30)

                    question_text = Text(enterd_question_frame)
                    question_text.place(x=20, y=100, width=460, height=70)
                    question_text.insert(END, q_tuple[1])

                    option_a_text = Text(enterd_question_frame)
                    option_a_text.place(x=30, y=175, width=200, height=40)
                    option_a_text.insert(END, q_tuple[2])

                    option_b_text = Text(enterd_question_frame)
                    option_b_text.place(x=250, y=175, width=200, height=40)
                    option_b_text.insert(END, q_tuple[3])

                    option_c_text = Text(enterd_question_frame)
                    option_c_text.place(x=30, y=235, width=200, height=40)
                    option_c_text.insert(END, q_tuple[4])

                    option_d_text = Text(enterd_question_frame)
                    option_d_text.place(x=250, y=235, width=200, height=40)
                    option_d_text.insert(END, q_tuple[5])

                    qanswer_text = Label(enterd_question_frame, text="answer")
                    qanswer_text.place(x=100, y=300)
                    qanswer_entry = Entry(enterd_question_frame)
                    qanswer_entry.place(x=180, y=300)
                    qanswer_entry.insert(0, q_tuple[6])

                    question_submit_button = Button(enterd_question_frame, text="SUBMIT", command=update_question_in_database,
                                                    height=1, width=17)
                    question_submit_button.place(x=150, y=330)

                    enterd_question_frame.place(x=0, y=130)
            except ValueError:
                mb.showerror("", "enter numaric value")

                mainpage()

        update_question_page = Tk()
        update_question_page.title("welcome page")
        update_question_page.geometry("500x500")
        update_question_page.configure(bg="azure")
        question_header = Label(update_question_page, text="      UPDATE QUESTION         ", bg="sky blue",
                                fg="black", font=('Arial Black', 17, "bold", "italic"))
        question_header.place(x=100, y=0)

        update_label = Label(update_question_page, text="Question no", font=('Arial Black', 9, "bold", "italic"))
        update_label.place(x=50, y=60)

        update_question_entry = Entry(update_question_page)
        update_question_entry.place(x=140, y=60)

        question_submit_button = Button(update_question_page, text="UPDATE QUESTION", command=find_question, height=1,
                                        width=17)
        question_submit_button.place(x=200, y=100)

        update_question_page.mainloop()

    def treeview():                        # to cteating the table or all question and answers
        main_page.geometry("850x800")
        tree_frame = ttk.Frame(main_page)
        tree_frame.grid(row=1, column=0)
        s=ttk.Style()
        s.configure('Treeview', rowheight=60)

        tree = ttk.Treeview(tree_frame,height = 15,selectmode = "browse",style='Treeview')

        db = pymysql.connect("localhost", "root", "", "quiz_database")
        cursor = db.cursor()
        tree["columns"] = ("question", "option_a", "option_b", "option_c", "option_d", "answer",)
        #tree.column("question_no", width=45)
        tree.column("question", width=300)
        tree.column("option_a", width=150)
        tree.column("option_b", width=150)
        tree.column("option_c", width=150)
        tree.column("option_d", width=150)
        tree.column("answer", width=50)

        #tree.heading("question_no", text="SR no", )
        tree.heading("question", text="QUESTION", anchor='w')
        tree.heading("option_a", text="OPTION A", anchor='w')
        tree.heading("option_b", text="OPTION B", anchor='w')
        tree.heading("option_c", text="OPTION C", anchor='w')
        tree.heading("option_d", text="OPTION D", anchor='w')
        tree.heading("answer", text="ANSWER", anchor='w')
        sql = "SELECT * FROM quiz_question_answers"
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            question_no = row[0]

            question = row[1]
            option_a = row[2]
            option_b = row[3]
            option_c = row[4]
            option_d = row[5]
            answer = row[6]
            tree.insert("", question_no,text=question_no, values=(question, option_a, option_b, option_c, option_d, answer))
        tree.grid(row=1,column=0)

        def clear_tree():
            tree_frame.destroy()
            main_page.geometry("500x500")

        btn_register = Button(tree_frame, text="Exit", bg="azure", fg="blue4", command=clear_tree,
                              height=1, width=8)
        btn_register.grid(row=3,column=0)

    def question_details():

        def fetch_question():
            db = pymysql.connect("localhost", "root", "", "quiz_database")
            cursor = db.cursor()
            try:
                get_question_detail = int(question_number.get())
                sql = "select * from quiz_question_answers where question_no=%d" % get_question_detail
                cursor.execute(sql)
                r = (cursor.fetchall())
                if len(r)<1:
                    mb.showerror("", "question is not in database")
                else:
                    q_tuple = r[0]
                    question_text.insert(END, q_tuple[1])
                    option_a_text.insert(END, q_tuple[2])
                    option_b_text.insert(END, q_tuple[3])
                    option_c_text.insert(END, q_tuple[4])
                    option_d_text.insert(END, q_tuple[5])
                    qanswer_entry.insert(END, q_tuple[6])
            except ValueError:
                mb.showerror("", "enter numaric value")
        def clear_function():
            question_details()

        frame = ttk.Frame(main_page)
        frame.grid(row=1,column=0)
        frame.configure(width=400, height=400)
        q_label = Label(frame, text="question number")
        q_label.grid(row=0, column=0)
        question_number = Entry(frame)
        question_submit_button = Button(frame, text="find", command=fetch_question, height=1,
                                        width=17)
        question_number.grid(row=1,column=0)
        question_submit_button.grid(row=1,column=1)
        question_text = Text(frame)
        question_text.config(width=70,height=4)
        question_text.grid(row=3,columnspan=2)


        option_a_text = Text(frame)
        option_a_text.config(width=30,height=2)
        option_a_text.grid(row=4,column=0)
        option_b_text = Text(frame)
        option_b_text.config(width=30,height=2)
        option_b_text.grid(row=4,column=1)

        option_c_text = Text(frame)
        option_c_text.config(width=30,height=2)
        option_c_text.grid(row=5,column=0)

        option_d_text = Text(frame)
        option_d_text.config(width=30,height=2)
        option_d_text.grid(row=5,column=1)

        qanswer_text = Label(frame, text="answer")
        qanswer_text.grid(row=6,column=0)
        qanswer_entry = Entry(frame)
        qanswer_entry.grid(row=6,column=1)

        clear_button = Button(frame, text="clean", command=clear_function, height=1,
                                        width=17)
        clear_button.grid(row=8,column=1)
        def exit_function():
            frame.destroy()

        exit_button = Button(frame, text="Exit", command=exit_function, height=1,
                              width=17)
        exit_button.grid(row=8, column=0)

    def delete_question():

        def delete():
            db = pymysql.connect("localhost", "root", "", "quiz_database")
            cursor = db.cursor()
            try:
                get_question_detail = int(question_number_entry.get())
                sql = "delete from quiz_question_answers where question_no='%d'" % get_question_detail
                r=cursor.execute(sql)
                if r > 0:
                    mb.showinfo("", "Question deleted successfully.")
                else:
                    mb.showinfo("", "Question is not in database .")
                db.commit()
            except ValueError:
                mb.showerror("", "enter numaric value")


        header = Label(main_page, text="      Delete QUESTION         ", bg="sky blue",
                                fg="black", font=('Arial Black', 17, "bold", "italic"))
        header.place(x=100, y=0)

        question_number = Label(main_page, text="Question no", font=('Arial Black', 9, "bold", "italic"))
        question_number.place(x=50, y=60)

        question_number_entry = Entry(main_page)
        question_number_entry.place(x=140, y=60)

        delete_submit_button = Button(main_page, text="Delete", command=delete, height=1,
                                        width=17)
        delete_submit_button.place(x=200, y=100)



    manubar=Menu(main_page)

    filemenu=Menu(manubar,tearoff=0)
    filemenu.add_command(label="Insert questions",command=Insertquestion)
    filemenu.add_command(label="find question",command=question_details)
    filemenu.add_separator()
    filemenu.add_command(label="Select all question",command=treeview)
    manubar.add_cascade(label="File",menu=filemenu)

    editmenu=Menu(manubar,tearoff=0)
    editmenu.add_command(label="Update question",command=main_update_question)
    editmenu.add_command(label="Delete question",command=delete_question)
    manubar.add_cascade(label="Update",menu=editmenu)
    main_page.configure(menu=manubar,height=1,width=17)

    main_page.mainloop()

def quiz_login():
    bhavya = txt_email.get()
    passw = txt_password.get()
    db = pymysql.connect("localhost", "root", "", "quiz_database")
    cursor = db.cursor()
    sql = "select user_id,user_password from registerd_user where user_id='%s' and user_password='%s'"\
          % (bhavya,passw)
    r=cursor.execute(sql)
    user_id=cursor.fetchall()
    if r:
        mb.showinfo("login","LOGIN SUCCESSFULL")
        root.destroy()
        mainpage()




    else:
        mb.showerror("Error 404","Invalid email and password")

    db.close()

def forgot_password():
    forgot_screen=Tk()
    forgot_screen.title("Forgot password")
    forgot_screen.geometry("500x500")
    forgot_screen.config(bg="azure")
    imageframe=Frame(forgot_screen)


    def forgot_user_password():
        db = pymysql.connect("localhost", "root", "", "quiz_database")
        user_name1=txt_user_name.get()
        user_email=txt_email.get()

        cursor = db.cursor()
        sql = "select user_id,user_password from registerd_user where user_name='%s' and user_id='%s'"%(user_name1,user_email)
        cursor.execute(sql)
        id_pass=cursor.fetchall()
        if id_pass:
            id = id_pass[0]
            mb.showinfo("","Your User Id is = '%s' \n and password is = '%s'"%(id[0],id[1]))
        else:
            mb.showinfo("","plese enter valid user name and user email.")

        db.commit()
        db.close()
    Login_hader = Label(forgot_screen, text="Forgot Your Password? \n", bg="sky blue",
                        fg="black", font=('Arial Black', 20, "bold", "italic"))
    Login_hader.place(x=100, y=20)
    Login_hader = Label(forgot_screen, text="Please enter your name and email address  \nregisterd on your account", bg="sky blue",
                        fg="black", font=('Arial Black', 10, "bold", "italic"))
    Login_hader.place(x=100, y=60)

    user_name = Label(forgot_screen, text="Name:\t\t\t\t     \n\n\n\n\n\n", bg="khaki", font=('Arial', 13))
    user_name.place(x=125, y=110)

    txt_user_name = Entry(forgot_screen, font=('Arial', 13,))
    txt_user_name.place(x=205, y=120)

    email = Label(forgot_screen, text="Email:", bg="khaki", font=('Arial', 13,))
    email.place(x=125, y=160)

    txt_email = Entry(forgot_screen, font=('Arial', 13,))
    txt_email.place(x=205, y=160)

    btn_login = Button(forgot_screen, text="forgot password", relief=GROOVE, command=forgot_user_password, height=1, width=20)
    btn_login.place(x=170, y=210)

    imageframe.pack()
    forgot_screen.mainloop()

def register_user():                            #Another page of registration
    register=Tk()
    register.title("Quiz Registration")
    register.geometry("500x500")
    register.config(bg="azure")

    def register_data_in_database():            #funcrion for registration page
        import pymysql
        u_name=txt_user_name.get()
        email=txt_email.get()
        u_password=txt_password_u.get()
        u_password_confirm=txt_password_u_confirm.get()

        if len(u_password) > 3 and (u_password==u_password_confirm) and len(u_name)>3 and len(email) >3:      #to check whether both passwords are same
            db = pymysql.connect("localhost", "root", "", "quiz_database")
            cursor = db.cursor()
            sql="INSERT into registerd_user(user_name,user_id,user_password)values('%s','%s','%s')"%(u_name,email,u_password)
            r=cursor.execute(sql)
            if r:
                register.destroy()
                mb.showinfo("","Registerd Successfully")
                register.destroy()

            else:
                mb.showerror("","enter data properly")

            db.commit()
            db.close()
        else:
            mb.showerror("","Password not matched")

    Login_hader = Label(register, text="        Registration For Quiz    ", bg="sky blue",
                        fg="black", font=('Arial Black', 17, "bold", "italic"))
    Login_hader.place(x=100, y=20)

    user_name = Label(register, text="Name:", bg="azure", font=('Arial', 13,))
    user_name.place(x=100, y=80 )

    txt_user_name = Entry(register, font=('Arial', 13,))
    txt_user_name.place(x=190, y=80)

    email = Label(register, text="Email:", bg="azure", font=('Arial', 13,))
    email.place(x=100, y=120 )

    txt_email = Entry(register, font=('Arial', 13,))
    txt_email.place(x=190, y=120)

    password = Label(register, text="Password:", bg="azure", font=('Arial', 13,))
    password.place(x=100, y=160 )

    txt_password_u = Entry(register, font=('Arial', 13,),show="*")
    txt_password_u.place(x=190, y=160)

    password_confirm = Label(register,text="Confirm Password:", bg="azure", font=('Arial', 13,))
    password_confirm.place(x=100, y=200)

    txt_password_u_confirm = Entry(register, font=('Arial', 13,),show="*")
    txt_password_u_confirm.place(x=260, y=200)

    btn_new_register = Button(register, text="Sign Up",font=(10), command=register_data_in_database, height=1, width=13)
    btn_new_register.place(x=200, y=240)

    register.mainloop()

Login_hader = Label(root , text = "        Sign in for QUIZ management                     " , bg = "sky blue" , fg = "black", font = ('Arial Black', 17, "bold","italic"))
Login_hader.place(x=10,y=20)

image_1="Python-Logo.png"
img = ImageTk.PhotoImage(Image.open(image_1))
image_label=Label(root,image = img,bg="azure",fg="azure")
image_label.place(x=120,y=215)

email_label=Label(root, text="User id:",bg="azure", font=('Arial',13,))
email_label.place(x=100, y=80,)

txt_email=Entry(root,font=('Arial',13,))
txt_email.place(x=190,y=80)

password_label=Label(root,text="password:",bg="azure", font=('Arial',13))
password_label.place(x=100, y=120,)

txt_password=Entry(root,show="*",font=(13))
txt_password.place(x=190,y=120)

btn_login = Button(root, text="Login",relief=GROOVE ,command = quiz_login,height=1,width=20,)
btn_login.place(x=180, y=160)

btn_register = Button(root, text="Sign Up",relief=FLAT,bg="azure",fg="blue4",command = register_user,height=1,width=8)
btn_register.place(x=222, y=185)

btn_login = Button(root, text="Forgot Password",bg="azure",relief=FLAT,fg="blue4" ,font=('bold',8,'underline'),command =forgot_password,height=1,width=15,)
btn_login.place(x=380, y=120)

root.mainloop()

