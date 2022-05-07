#импорты
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt
#константы
WIGHT = 1024
HEIGHT = 512
okno_x = 200
okno_y = 200
#класс окна
class okoshko(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent,flags=flags)
        self.initUI()
        self.show()
        self.connects()
    def initUI(self):
        self.bttn = QPushButton('пройти пробу Руфье')
        self.labl = QLabel("Проба Руфье представляет собой нагрузочный комплекс, предназначенный\nдля оценки работоспособности сердца при физической нагрузке")
        self.line = QLineEdit("ФИО")
        self.line0 = QLineEdit("возраст")
        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()
        self.h_layout0 = QHBoxLayout()
        self.h_layout0.addWidget(self.line,alignment=Qt.AlignCenter)
        self.h_layout0.addWidget(self.line0,alignment=Qt.AlignCenter)
        self.h_layout.addWidget(self.bttn,alignment=Qt.AlignCenter)
        self.h_layout.addWidget(self.labl,alignment=Qt.AlignLeft)
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addLayout(self.h_layout0)
        self.setLayout(self.v_layout)
    def connects(self):
        self.bttn.clicked.connect(self.testik)
    def testik(self):
        self.h_layout0.removeWidget(self.labl)
        self.labl.deleteLater()
        self.labl = None
        self.h_layout0.removeWidget(self.line0)
        self.line0.deleteLater()
        self.line0 = None
        self.line1 = QLabel("Полежите 5 минут, замерьте пульс и запишите его")
        self.line.setText("пульс")
        self.h_layout0.addWidget(self.line1,alignment=Qt.AlignRight)
        self.h_layout.addWidget(self.labl,alignment=Qt.AlignRight)
#для потестить
def qqq():
    print('heheheheh')
#мейн дофига
def main():
    app = QApplication([])
    okno = okoshko()
    okno.resize(WIGHT,HEIGHT)
    okno.move(okno_x,okno_y)
    okno.setWindowTitle("hehe")
    app.exec_()

#исполняемая часть)
main()
