from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton

app =QApplication([])


window = QWidget()
window.setWindowTitle('привец')
window.move(900, 70)
window.resize(400, 400)
window.show()

#кнопки
button1 = QPushButton('PHP')
button2 = QPushButton('JavaScript')
button3 = QPushButton('Python')
button4 = QPushButton('Pascal')
button5 = QPushButton('SQL')
button6 = QPushButton('C++')

#направляющие линии
v_line = QVBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()

#помещаем кнпоки на линии
h_line1.addWidget(button1, alignment= Qt.AlignCenter)
h_line1.addWidget(button2, alignment= Qt.AlignCenter)
h_line2.addWidget(button3, alignment= Qt.AlignCenter)
h_line2.addWidget(button4, alignment= Qt.AlignCenter)
h_line3.addWidget(button5, alignment= Qt.AlignCenter)
h_line3.addWidget(button6, alignment= Qt.AlignCenter)

#помещаем горизантальные линии на вертикальную
v_line.addLayout(h_line1)
v_line.addLayout(h_line2)
v_line.addLayout(h_line3)

#помещаем линии на окно
window.setLayout(v_line)


app.exec_()