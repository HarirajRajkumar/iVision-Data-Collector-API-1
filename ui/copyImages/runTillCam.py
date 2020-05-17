#Opens camera 

from PySide2 import QtWidgets
from images import main
import cv2 

app_name = 'iVision Data Collector'
app_version = '1.0.0'

class MyQtApp(main.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp,self).__init__()
        self.setupUi(self)
        self.setWindowTitle(app_name+' '+app_version)
        self.pushButton.clicked.connect(self.checkCam)

    def checkCam(self):
        camNo = self.lineEdit.text()
        print(camNo)    
        cap = cv2.VideoCapture(int(camNo))
        #Pop up if
        if not camNo:
            QtWidgets.QMessageBox.about(self, "Camera Config Error ", "Camera IP Not Given ")
            return  

        while(cap.isOpened()):
            ret, frame = cap.read()

            cv2.imshow('frame',frame)
            if cv2.waitKey(1) == 27:
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()