from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from gui import *

import sys
import cv2

# Main Window
class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        # Connect buttons to respective methods
        self.ui.show_bt.clicked.connect(self.show_image)
        self.ui.clear_bt.clicked.connect(self.clear_image)

    def get_image_path(self):
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self, "Select Image File")
        return image_path

    def show_image(self):
        image_path = self.get_image_path()
        if not image_path:
            print("No image selected.")
            return

        image = cv2.imread(image_path)
        if image is None:
            print("Failed to load image.")
            return
        
        img = cv2.imread(image_path)
        label_width = self.ui.image.width()
        label_height = self.ui.image.height()

        # Resize the image to fit the QLabel dimensions
        img = cv2.resize(image, (label_width, label_height))

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Get the dimensions of the image
        h, w, ch = img_rgb.shape
        bytes_per_line = ch * w

        # Convert the image to QImage
        q_img = QImage(img_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)

        # Display the QImage in the QLabel
        self.ui.image.setPixmap(QPixmap.fromImage(q_img))
        self.ui.image.setAlignment(Qt.AlignCenter)

    def clear_image(self):
        # Clear the QLabel by setting an empty QPixmap
        self.ui.image.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = MainWindow()
    sys.exit(app.exec())