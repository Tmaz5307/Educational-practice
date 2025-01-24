from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class Rooms(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Комнаты')
        main_l = QVBoxLayout()
        h_l1 = QHBoxLayout()
        h_l2 = QHBoxLayout()
        self.resize(650, 600)
        self.setFixedSize(self.width(), self.height())
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        h_l1.addWidget(self.label)
        self.delete_button = QPushButton('Удалить')
        self.add_button = QPushButton('Добавить')
        self.edit_button = QPushButton('Изменить')
        self.close_button = QPushButton('Закрыть')
        h_l2.addWidget(self.add_button)
        h_l2.addWidget(self.delete_button)
        h_l2.addWidget(self.edit_button)
        h_l2.addWidget(self.close_button)
        main_l.addLayout(h_l1)
        main_l.addStretch()
        main_l.addLayout(h_l2)
        self.setLayout(main_l)
        self.show()
        self.close_button.clicked.connect(self.go_back)

    def add_dish(self):
        pass

    def delete_dish(self):
        pass

    def edit_dish(self):
        pass

    def go_back(self):
        self.close()
