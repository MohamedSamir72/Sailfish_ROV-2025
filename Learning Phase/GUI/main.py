from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from front_end import *

import sys

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        # QTimer to call change_label_text after 8 seconds
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.change_label_text)
        # Ensure it only triggers once
        self.timer.setSingleShot(True)  
        
        self.timer.start(8000)  # 8000 milliseconds = 8 seconds

    def change_label_text(self):
        self.ui.label.setText("Text changed after 8 seconds")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = MainWindow()
    sys.exit(app.exec())
