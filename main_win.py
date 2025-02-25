import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from rooms_win import Rooms

class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Главный экран')
        main_l = QVBoxLayout()
        wid = QWidget()
        wid.setLayout(main_l)
        self.setCentralWidget(wid)
        self.label = QLabel()
        pixmap = QPixmap('logo.jpg')
        self.label.setPixmap(pixmap)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_l.addWidget(self.label)
        self.resize(300, 200)
        self.setFixedSize(self.width(), self.height())
        self.rooms = QPushButton('Комнаты')
        self.developers = QPushButton('О создателях')
        self.close = QPushButton('Выход')
        main_l.addWidget(self.rooms)
        main_l.addWidget(self.developers)
        main_l.addWidget(self.close)
        self.developers.clicked.connect(self.show_developers)
        self.close.clicked.connect(QApplication.quit)
        self.rooms.clicked.connect(self.show_rooms)
        self.show()

    def show_developers(self):
        self.win_developers = QMessageBox()
        self.win_developers.setWindowTitle('О создателях')
        self.win_developers.setText('Разработчики: Мажаров Артём и Плотников Дмитрий\nГруппа: 3СПИ')
        self.win_developers.show()

    def show_rooms(self):
        self.rooms_win = Rooms()
        self.rooms_win.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = MainWin()
    sys.exit(app.exec())