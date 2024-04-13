#создай приложение для запоминания информации
ql = [
    ['Чему рапно число Пи?' , '3.14', '4.5','6' , '3/4'],
    ['Чему равен √9?','3' , '4', '7','1' ],
    ['Чему равен 3/1?','3','2','1','5']
]
from question import Question
from PyQt5 import Qt 
from PyQt5.QtWidgets import (
QApplication, 
QWidget, 
QPushButton, 
QLabel, 
QVBoxLayout, 
QMessageBox, 
QHBoxLayout, 
QRadioButton, 
QHBoxLayout, 
QGroupBox, 
QButtonGroup)
from PyQt5.QtGui import QFont 
from random import shuffle, randint

counter = 0
attempts = 0
true_attempts = 0

def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    right_ans.setText(f'Правильный ответ:{q.right_answer}')
    show_qestion()

def check_answer():
    true_ans = bool()
    if answers[0].isChecked():
        result = 'ПРАВИЛЬНО!😎'
    else:
        result = 'НЕВЕРНО!※'
        true_ans = False
    show_correct(result, true_ans)

def show_correct(r, true_ans):
    global attempts, true_attempts
    if true_ans:
        true_attempts += 1
    txt_stats = f'Статистика:\nКоличество попыток:{attempts}\nПравильных ответов: {true_attempts}\nРейтинг: {int(true_attempts/attempts*100)}%'
    stats.setText(txt_stats)
    res.setText(r) 
    show_answer()


def start_test():
    #global counter
    if btn_OK.text() == 'Ответить':
        btn_OK.setText('Далее')
        check_answer()
    elif btn_OK.text() == 'Далее':
        btn_OK.setText('Ответить')
        randNum = randint(0,len(q_list)-1)
        ask(q_list[randNum])
        #counter += 1
        #if counter > len(q_list) - 1:
            #counter = 0

def show_answer():
    RadioGroupBox.hide()
    AnsBox.show()

def show_qestion():
    global attempts 
    attempts += 1
    Buttons.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    Buttons.setExclusive(True)
    RadioGroupBox.show()
    AnsBox.hide()


font = QFont()
font.setFamily('Roboto')
font.setPointSize(16)

app = QApplication([])

window = QWidget()
window.resize(400,350)
window.setWindowTitle('Memory Card')

res = QLabel('Верно/Неверно')
res.setFont(font)
stats = QLabel()
right_ans = QLabel('голубой')

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Какого цвета настоящий шайлушай?')

RadioGroupBox = QGroupBox('Вaривнты ответов:')
Buttons = QButtonGroup()

rbtn1 = QRadioButton('красный')
rbtn2 = QRadioButton('голубой')
rbtn3 = QRadioButton('зеленый')
rbtn4 = QRadioButton('фиолетовый')

answers = [rbtn1, rbtn2, rbtn3, rbtn4]

Buttons.addButton(rbtn1)
Buttons.addButton(rbtn2)
Buttons.addButton(rbtn3)
Buttons.addButton(rbtn4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)



RadioGroupBox.setLayout(layout_ans1)
AnsBox = QGroupBox('Результат')

res_line = QVBoxLayout()
res_line.addWidget(res)  # , alignment=Qt.AlignLeft)
res_line.addWidget(right_ans)  # , alignment=Qt.AlignCenter)
AnsBox.setLayout(res_line)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line2_5 = QHBoxLayout()
layout_line3 = QHBoxLayout()
#_____________________________________________________________________________

layout_line1.addWidget(lb_Question) #, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsBox)

layout_line2_5.addWidget(stats)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line2_5)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

btn_OK.clicked.connect(start_test)
AnsBox.hide()
window.setLayout(layout_card)
q1 = Question('1+1','2','3','6','65')
q2 = Question('2+1-1+108+1+1-109','3','2','6','35')
q3 = Question('2+2-1+1-1+3-2-1','4','3','6','7')
q4 = Question('вероятность выпадения орла на монетке равна:','50/50','40/20','99/1','100')
q5 = Question('какая видеокарта не относится к линейке 16?','1600','1640','1650','1690 titanium')
q6 = Question('Чему равен √9?','3','2','1','9')
q7 = Question('Петербург основан в ','1703','1678','3478','980')
q_list = list()
q_list.append(q1)
q_list.append(q2)
q_list.append(q3)
q_list.append(q4)
q_list.append(q5)
q_list.append(q6)
q_list.append(q7)
ask(q1)
window.show()
app.exec_()   


# в программе 
# имеется множество
# различных функций

# имеются прработанные
# варианты ответов

# статистика в
# ркальном времени