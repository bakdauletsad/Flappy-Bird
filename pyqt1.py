from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

app =QApplication([])


window = QWidget()
window.setWindowTitle('привец')
window.move(900, 70)
window.resize(400, 200)
window.show()

button = QPushButton('Кнопка с секретом')
h_line = QVBoxLayout()
h_line.addWidget(button, alignment=Qt.AlignCenter)
window.setLayout(h_line)

def show_text():
    title = QLabel('Я родился!')
    h_line.addWidget(title, alignment=Qt.AlignCenter)
    window.setLayout(h_line)

button.clicked.connect(show_text)

app.exec_()