class Question():
    def __init__(self, question = 'корень из девяти?',
    right_ans = '3',
    wrong1 = '5', 
    wrong2 = '1',
    
    wrong3 = '9'):
        self.question = question
        self.right_answer = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
    def get_question(self):
        self.question = input('Введите вопрос')
        self.right_answer = input('Введите правильный ответ')
        self.wrong1 = input('Введите неправильный ответ №1')
        self.wrong2 = input('Введите неправильный ответ №2')
        self.wrong3 = input('Введите неправильный ответ №3')

if __name__ == '__main__':
    q = Question()
    print(f'{q.question}')
    q2 = Question('Висит груша , нельзя скушать',
    'лампочка',
    'шпатель',
    'утка',
    'да')
    print(f'{q2.question}')
    q3 = Question()
    q3.get_question()