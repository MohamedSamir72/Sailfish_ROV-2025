from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from gui import *


import sys
import cv2

class VideoThread(QThread):
    # Define a signal to send the frame to the main thread
    change_pixmap_signal = pyqtSignal(QImage)

    def __init__(self, video_path=None):
        super(VideoThread, self).__init__()
        self.video_path = video_path
        self._run_flag = True

    def run(self):
        cap = cv2.VideoCapture(self.video_path)

        while self._run_flag:
            ret, frame = cap.read()
            if ret:
                # Convert to RGB
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Flip the image hrizontally
                frame_rgb = cv2.flip(frame_rgb, 1)
                
                # Convert frame to QImage
                h, w, ch = frame_rgb.shape
                bytes_per_line = ch * w
                q_img = QImage(frame_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)

                # Emit the signal with the QImage
                self.change_pixmap_signal.emit(q_img)
            else:
                break

        cap.release()

    def stop(self):
        """Sets run flag to False and waits for the thread to finish."""
        self._run_flag = False
        self.wait()


class Window(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        # Connect buttons to respective methods
        self.ui.camera_bt.clicked.connect(self.start_camera)
        self.ui.video_bt.clicked.connect(self.start_video)
        self.ui.stop_bt.clicked.connect(self.stop_video)


        # Initialize the video thread variable
        self.thread = None

    def get_video_path(self):
        # Open a file dialog to select a video file
        file_dialog = QFileDialog()
        video_path, _ = file_dialog.getOpenFileName(self, "Select Video File")
        return video_path

    def start_camera(self):
        # Create a new video thread with laptop's camera
        self.thread = VideoThread(0)
        
        # Connect the signal from the thread to the update image method
        self.thread.change_pixmap_signal.connect(self.update_image)

        # Start the thread
        self.thread.start()

    def start_video(self):
        video_path = self.get_video_path()
        if not video_path:
            print("No video selected.")
            return

        # Create a new video thread
        self.thread = VideoThread(video_path)
        
        # Connect the signal from the thread to the update image method
        self.thread.change_pixmap_signal.connect(self.update_image)

        # Start the thread
        self.thread.start()

    def update_image(self, q_img):
        # Update the QLabel with the QImage
        label_width = self.ui.image.width()
        label_height = self.ui.image.height()

        # Resize QImage to fit the QLabel
        q_img = q_img.scaled(label_width, label_height)

        self.ui.image.setPixmap(QPixmap.fromImage(q_img))
        self.ui.image.setAlignment(Qt.AlignCenter)

    def stop_video(self):
        # Stop the video thread if it's running
        if self.thread is not None:
            self.thread.stop()
            self.thread = None
        
        # Clear the QLabel
        self.ui.image.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = Window()
    sys.exit(app.exec())



