#импорты
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel, QLineEdit
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
        self.bttn = QPushButton('поройти пробу Руфье')
        self.labl = QLabel("Проба Руфье представляет собой нагрузочный комплекс, предназначенный\nдля оценки работоспособности сердца при физической нагрузке")
        self.line = QLineEdit("имя")
        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.line,alignment=Qt.AlignCenter)
        self.h_layout.addWidget(self.bttn,alignment=Qt.AlignCenter)
        self.h_layout.addWidget(self.labl,alignment=Qt.AlignRight)
        self.setLayout(self.h_layout)
    def connects(self):
        self.bttn.clicked.connect(self.testik)
    def testik(self):
        #self.h_layout.setParent(None)
        self.h_layout = QHBoxLayout()
        self.labl = QLabel("a")
        self.h_layout.addWidget(self.labl,alignment=Qt.AlignRight)
        self.setLayout(h_layout)
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