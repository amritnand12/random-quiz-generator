import gspread
from oauth2client.service_account import ServiceAccountCredentials
import tkinter
from timer import Countdown
from tkinter import *
import random
scope = ['https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.\
    from_json_keyfile_name('testsheets.json', scope)
client = gspread.authorize(credentials)
sheet = client.open('quiz data').sheet1
data = sheet.get_all_records()
questions = []
options = []
answer = []
n = 0
for i in range(len(data)):
    row = sheet.row_values(i+1)
    queso, op1, op2, op3, op4, ans = row
    questions.append(queso)
    options.append([op1, op2, op3, op4])
    if ans == op1:
        answer.append(0)
    elif ans == op2:
        answer.append(1)
    elif ans == op3:
        answer.append(2)
    else:
        answer.append(3)
    n += 1
# COMMENTED CODE IS FOR SQLITE DATABASE
# IN ORDER TO CREATE DATABASE , THE INSERT VALUE SQLITE COMMAND WAS RUN WITHIN THE LOOP OF SOURCE CODE TO FILL THE DATABASE WITH ALL THE DATA

# import sqlite3
# table = sqlite3.connect('quizdata.db')
# table.execute(" CREATE TABLE IF NOT EXISTS QUESTIONS(ques VARCHAR(8000),"
#               "op1 VARCHAR(8000),op2 VARCHAR(8000),op3 VARCHAR(8000),op4 VARCHAR(8000),"
#               "ans VARCHAR(8000));")
# table.commit()
# l = table.execute("SELECT * FROM QUESTIONS")
# for row in l:
#     queso, op1, op2, op3, op4, ans = row
#     questions.append(queso)
#     options.append([op1, op2, op3, op4])
#     if ans == op1:
#         answer.append(0)
#     elif ans == op2:
#         answer.append(1)
#     elif ans == op3:
#         answer.append(2)
#     else:
#         answer.append(3)
#     n += 1
# table.close()

root = tkinter.Tk()
root.title('QuizTime')
root.geometry('720x540')
root.resizable(0, 0)

user_answer = ["*"]*n

indexes = []


def gen():
    global indexes
    while len(indexes) < 10:
        x = random.randint(0, n-1)
        if x not in indexes:
            indexes.append(x)
    # print(indexes)


def showresult(score):
    ques.destroy()
    s1.destroy()
    s2.destroy()
    s3.destroy()
    s4.destroy()

    labelimage = Label(root, )
    labelimage.pack(pady=(10, 50))

    labelresult = Label(root, font=('showcard gothic', 20), )
    labelresult.pack()

    if score >= 9:
        img = PhotoImage(file='excellent.png')
        labelimage.image = img
        labelimage.configure(image=img)

        labelresult.configure(text='YOU DID GREAT JOB !! \n YOU SCORED "{}"'.format(score), bg='green')

    elif 4 < score < 9:
        imgg = PhotoImage(file='good.png')
        labelimage.image = imgg
        labelimage.configure(image=imgg)

        labelresult.configure(text='GOOD ONE BUT YOU CAN DO BETTER NEXT TIME.\n YOU SCORED "{}"'.format(score),
                              bg='yellow')

    else:
        img = PhotoImage(file='bad.png')
        labelimage.image = img
        labelimage.configure(image=img)

        labelresult.configure(text='YOU FAILED, YOU HAVE TO DO BETTER..\n YOU SCORED JUST "{}"'.format(score), bg='red')

    exit = tkinter.Frame(root)
    exit.pack(pady=(20, 0))
    exit_button = tkinter.Button(exit, text='** EXIT **', font=('casteller',), bg='red', command=root.destroy)
    exit_button.pack()


def calc():
    global indexes, user_answer, answer
    j = 0
    score = 0
    for i in indexes:
        if user_answer[j] == answer[i]:
            score += 1
        j += 1
    # print(score)
    showresult(score)


quest = 1


def selected():
    global submit, user_answer, ques, s1, s2, s3, s4, quest
    x = submit.get()
    # print(x)
    user_answer[quest - 1] = x
    submit.set(-1)
    if quest < 10 and count._timer_on:
        ques.config(text=questions[indexes[quest]])
        s1['text'] = options[indexes[quest]][0]
        s2['text'] = options[indexes[quest]][1]
        s3['text'] = options[indexes[quest]][2]
        s4['text'] = options[indexes[quest]][3]
        quest += 1

    else:
        # print(indexes)
        # print(user_answer)
        # print(answer)
        calc()
    if quest == 10:
        calc()


def start_quiz():
    global ques, s1, s2, s3, s4
    ques = Label(root, text=questions[indexes[0]],
                 font=('tw cen mt', 20), width=500, wraplength=400)
    ques.pack(pady=(50, 20))

    global submit
    submit = IntVar()
    submit.set(-1)

    s1 = Radiobutton(root, text=options[indexes[0]][0], font=('times new roman', 12), value=0, variable=submit,
                     command=selected)
    s1.pack(pady=5)

    s2 = Radiobutton(root, text=options[indexes[0]][1], font=('times new roman', 12), value=1, variable=submit,
                     command=selected)
    s2.pack(pady=5)

    s3 = Radiobutton(root, text=options[indexes[0]][2], font=('times new roman', 12), value=2, variable=submit,
                     command=selected)
    s3.pack(pady=5)

    s4 = Radiobutton(root, text=options[indexes[0]][3], font=('times new roman', 12), value=3, variable=submit,
                     command=selected)
    s4.pack(pady=5)


def start_press():

    labeltext.destroy()
    key.destroy()
    instruction.destroy()
    rule1.destroy()
    # rule2.destroy()
    rule3.destroy()
    rule4.destroy()
    start_inst.destroy()
    gen()
    start_quiz()
    count.start_button()


labeltext = Label(root, text="QUIZ-VERSION 1.0", font=('broadway', 24, 'bold'))
labeltext.pack()

key = tkinter.Frame(root)
key.pack()
# countdown=Countdown(root,key)
# countdown.pack()
start = tkinter.Button(key, text='** START **', bg='blue', font='castellar', command=start_press)
start.pack()


instruction = Label(root, text='READ THE FOLLOWING INSTRUCTIONS CAREFULLY BEFORE YOU START:',
                    font=('lucida handwriting', 12))
instruction.pack()

rule1 = Label(root, text="1- This quiz contains 10 questions having FOUR options each.", font=('ocr a', 12))
rule1.pack(pady=(5, 0))

# rule2 = Label(root, text="2- You have 30 seconds for each questions.", font=('ocr a', 12))
# rule2.pack(pady=(5, 0))

rule3 = Label(root,
              text="2- Once ticked, your answer will be automatically submitted,\n you can't change your options once "
                   "you pressed the option.",
              font=('ocr a', 12))
rule3.pack(pady=(5, 0))

rule4 = Label(root, text="3- Think before you answer.", font=('ocr a', 12))
rule4.pack(pady=(5, 0))

start_inst = Label(root, text="-- now press START above instructions --", fg='red', font=('sitka', 15))
start_inst.pack(pady=(20, 0))
count = Countdown(root)
count.pack()
root.mainloop()
