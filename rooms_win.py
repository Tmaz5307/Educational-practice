import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QMessageBox
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Room, Resident, Base  # Импортируем модели из ранее созданного файла

# Настраиваем базу данных
engine = create_engine('sqlite:///hostel0.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

class Rooms(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Система управления общежитием")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()

        # Создать таблицу для отображения данных
        self.table = QTableWidget()
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.layout.addWidget(self.table)

        # Поля для ввода данных
        self.name_input = QLineEdit()
        self.age_input = QLineEdit()
        self.room_input = QLineEdit()

        self.layout.addWidget(QLabel("Имя:"))
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(QLabel("Возраст:"))
        self.layout.addWidget(self.age_input)
        self.layout.addWidget(QLabel("Номер комнаты:"))
        self.layout.addWidget(self.room_input)

        # Кнопки управления
        self.add_button = QPushButton("Добавить жителя")
        self.add_button.clicked.connect(self.add_resident)
        self.layout.addWidget(self.add_button)

        self.update_button = QPushButton("Изменить жителя")
        self.update_button.clicked.connect(self.update_resident)
        self.layout.addWidget(self.update_button)

        self.delete_button = QPushButton("Удалить жителя")
        self.delete_button.clicked.connect(self.delete_resident)
        self.layout.addWidget(self.delete_button)

        self.refresh_button = QPushButton("Обновить данные")
        self.refresh_button.clicked.connect(self.load_data)
        self.layout.addWidget(self.refresh_button)

        self.close_button = QPushButton("Закрыть")
        self.close_button.clicked.connect(self.go_back)
        self.layout.addWidget(self.close_button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        # Загрузить данные при инициализации
        self.load_data()

    def load_data(self):
        # Загрузить данные из базы
        residents = session.query(Resident).all()
        self.table.setRowCount(len(residents))
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Имя", "Возраст", "Номер комнаты"])

        for row_idx, resident in enumerate(residents):
            self.table.setItem(row_idx, 0, QTableWidgetItem(resident.имя))
            self.table.setItem(row_idx, 1, QTableWidgetItem(str(resident.возраст)))
            self.table.setItem(row_idx, 2, QTableWidgetItem(resident.room.номер_комнаты if resident.room else "Нет комнаты"))

    def add_resident(self):
        имя = self.name_input.text()
        возраст = int(self.age_input.text())
        номер_комнаты = self.room_input.text()

        room = session.query(Room).filter_by(номер_комнаты=номер_комнаты).first()
        if not room:
            room = Room(номер_комнаты=номер_комнаты, вместимость=1)
            session.add(room)
            session.commit()

        new_resident = Resident(имя=имя, возраст=возраст, комната_id=room.id)
        session.add(new_resident)
        session.commit()

        self.load_data()

    def update_resident(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Внимание", "Пожалуйста, выберите жителя для изменения")
            return

        resident_id = session.query(Resident).all()[selected_row].id
        имя = self.name_input.text()
        возраст = int(self.age_input.text())
        номер_комнаты = self.room_input.text()

        resident = session.query(Resident).filter_by(id=resident_id).first()
        resident.имя = имя
        resident.возраст = возраст

        room = session.query(Room).filter_by(номер_комнаты=номер_комнаты).first()
        if not room:
            room = Room(номер_комнаты=номер_комнаты, вместимость=1)
            session.add(room)
            session.commit()

        resident.комната_id = room.id
        session.commit()

        self.load_data()

    def delete_resident(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Внимание", "Пожалуйста, выберите жителя для удаления")
            return

        resident_id = session.query(Resident).all()[selected_row].id
        resident = session.query(Resident).filter_by(id=resident_id).first()
        session.delete(resident)
        session.commit()

        self.load_data()

    def go_back(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DormitoryApp()
    window.show()
    sys.exit(app.exec())