import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtCore import Qt, QTimer, QPoint


class TurtleDrawing(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.points = [(50, 200), (150, 50), (250, 200),
                       (50, 200)]  # 삼각형 점과 시작점으로 돌아오기
        self.current_index = 0

    def initUI(self):
        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('Turtle Drawing a Triangle')
        self.label = QLabel(self)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_drawing)
        self.timer.start(1000)  # 1초 간격으로 업데이트
        self.show()

    def update_drawing(self):
        if self.current_index < len(self.points) - 1:
            self.current_index += 1
            self.update()

    def paintEvent(self, event):
        qp = QPainter(self.label.pixmap())
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        start = self.points[self.current_index - 1]
        end = self.points[self.current_index]
        qp.drawLine(start[0], start[1], end[0], end[1])
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TurtleDrawing()
    sys.exit(app.exec_())
