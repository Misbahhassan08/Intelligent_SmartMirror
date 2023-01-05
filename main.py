from PyQt5 import QtCore, QtGui, QtWidgets
from emoji_ui import Ui_MainWindow
from PyQt5.QtGui import QPixmap
import cv2
import sys
from threading import Thread
from time import sleep

class Main_screen(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Main_screen, self).__init__()
        self.setupUi(self)
        pass   # end of ini function
    pass   # end of main screen class
class main:
    def __init__(self):
        self.main_screen = Main_screen()
        self.init_properties()
        self.main_screen.showFullScreen()
        QtCore.QTimer.singleShot(1500,self.smile_icon)
        QtCore.QTimer.singleShot(4500,self.sad_icon)
        QtCore.QTimer.singleShot(7500,self.expression_icon)
        self.run_video()
        pass   # end of init function

    def run_video(self):
        self.stream_thread.change_pixmap.connect(self.main_screen.label_2.setPixmap)
        self.stream_thread.start()
        pass   # end of run_video function

    def init_properties(self):
        self.stream_thread = Stream_thread()
        pass   # end of init_properties function

    def smile_icon(self):
        self.main_screen.label.setPixmap(QtGui.QPixmap("smile.png"))
        pass   # end of smile__icon

    def sad_icon(self):
        self.main_screen.label.setPixmap(QtGui.QPixmap("sad.png"))
        pass   # end of sad__icon

    def expression_icon(self):
        self.main_screen.label.setPixmap(QtGui.QPixmap("expression.png"))
        pass   # end of expression__icon
    pass   # end of main class

class Stream_thread(QtCore.QThread):
    change_pixmap = QtCore.pyqtSignal(QtGui.QPixmap)
    
    def run(self):
        cap = cv2.VideoCapture(0)  
        self.thread_is_active = True
        while self.thread_is_active:
            ret, frame = cap.read()
            if ret:
                width = 1800
                height = 950
                dsize = (width, height)
                output = cv2.resize(frame, dsize, interpolation = cv2.INTER_AREA)
                image = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
                flipped_image = cv2.flip(image, 1)
                qt_image = QtGui.QImage(flipped_image.data, flipped_image.shape[1], flipped_image.shape[0], QtGui.QImage.Format_RGB888)
                pixmap = QtGui.QPixmap.fromImage(qt_image)
                self.change_pixmap.emit(pixmap)
        pass   # end of run function
    def stop_thread(self):
        self.thread_is_active = False
        self.quit()
        pass    # end of stop_thread
def _main():
    app = QtWidgets.QApplication(sys.argv)
    w = main()
    sys.exit(app.exec_())
    pass   # end of _main function
if __name__ == "__main__":
    _main()
    pass   # end of  __main__