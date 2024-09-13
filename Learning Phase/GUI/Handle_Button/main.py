from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from front_end import *
import sys

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.count = 0

        # Excute methods when user click on buttons
        self.ui.up_bt.clicked.connect(self.up_count)
        self.ui.down_bt.clicked.connect(self.down_count)
        self.ui.reset_bt.clicked.connect(self.reset_count)
        

        self.ui.up_bt.setCursor(Qt.PointingHandCursor)
        self.ui.down_bt.setCursor(Qt.PointingHandCursor)
        self.ui.reset_bt.setCursor(Qt.PointingHandCursor)
        

    def up_count(self):
        self.count+=1
        self.ui.counter.setText(f"{self.count}")
        self.ui.counter.setAlignment(Qt.AlignCenter)
        

    def down_count(self):
        self.count-=1
        self.ui.counter.setText(f"{self.count}")
        self.ui.counter.setAlignment(Qt.AlignCenter)
        

    def reset_count(self):
        self.count = 0
        self.ui.counter.setText(f"{self.count}")
        self.ui.counter.setAlignment(Qt.AlignCenter)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = MainWindow()
    sys.exit(app.exec())
