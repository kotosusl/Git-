import sys

from PyQt5.QtWidgets import QPushButton, QApplication, QMainWindow


class RoundGenerate(QMainWindow):
    pass


if __name__ == '__main__':
    app = QApplication([])
    rounds = RoundGenerate()
    rounds.show()
    sys.exit(app.exec())
