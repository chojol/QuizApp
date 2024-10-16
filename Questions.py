from PyQt6.QtWidgets import QDialog, QRadioButton, QSizePolicy
from ApiHandler import ApiHandler
from Question import Question
from questionLayout import Ui_Question


class Questions(QDialog):
    def __init__(self, category:str, limit: int):
        super().__init__()
        self.ui = Ui_Question()
        self.ui.setupUi(self)

        self.questions = ApiHandler.getQuestions(category,limit)

        self.number_of_question = 0
        self.buttons: [QRadioButton]= []

        self.get_question(self.questions[self.number_of_question])
        self.ui.nextButton.clicked.connect(self.next_question)
        self.show()

    def get_question(self, question: Question):
        self.ui.questionLabel.setText(question.question_text)
        for button in self.buttons:
            self.ui.verticalLayout.removeWidget(button)
        self.buttons = []

        for answer in question.answers:
            button = QRadioButton(text=answer)
            button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
            self.buttons.append(button)

        for button in self.buttons:
            self.ui.verticalLayout.addWidget(button)
            
    def next_question(self):
        self.number_of_question += 1
        if self.number_of_question < len(self.questions):
            self.get_question(self.questions[self.number_of_question])