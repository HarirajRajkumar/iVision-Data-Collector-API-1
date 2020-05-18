from PySide2 import QtWidgets
from PySide2.QtWidgets import QWidget, QVBoxLayout
from PySide2.QtGui import QPixmap
from images import main
import cv2 
import pandas as pd
import datetime
import numpy as np 
from PIL import Image
import os

app_name = 'iVision Data Collector'
app_version = '1.1.0'

httpfile= open("httpSet.txt","a")
locfile = open("LocSet.txt","a")

class MyQtApp(main.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp,self).__init__()
        self.setupUi(self)
        self.setWindowTitle(app_name+' '+app_version)   # pop up main window with app name and version
        #self.pushButton.clicked.connect(self.checkCam)  # check cam if connected
        self.pushButton_2.clicked.connect(self.start_ss)    # start taking snap shots
        self.pushButton_3.clicked.connect(self.ss_stop)     # stop taking snap shotss
        self.pushButton_3.hide()
        
        locfile = open("LocSet.txt","r")        # ALWAYS READ AND CLOSE 
        self.locFileData = locfile.read()
        locfile.close()

        httpfile = open("httpSet.txt","r")        # ALWAYS READ AND CLOSE 
        self.httpFileData = httpfile.read()
        httpfile.close()

        if not self.httpFileData:                 # Appending http camera link
            self.pushButton.clicked.connect(self.checkCam)  
        else: 
            print(self.httpFileData)
            self.lineEdit.setText(self.httpFileData)

        if not self.locFileData : # if nothing present in lock file get data from user
            self.toolButton.clicked.connect(self.select_Save_folder)    #select saving folder
        elif self.locFileData :   # else if present append to that text line 
            print(self.locFileData)     #''.join.locfile.read())
            self.lineEdit_2.setText(self.locFileData)

    def checkCam(self): 
        #self.camNo = self.lineEdit.text()    # read from lineEdit    # CAN be changed to self Variable
        #print(self.camNo)                    # check camNo 

        if self.lineEdit.text() == 'http://' or not self.lineEdit.text():                   # if cam not given
            QtWidgets.QMessageBox.about(self, "Camera Config Error ", "Camera IP Not Given ")
            return  
        else:
            self.camNo = self.lineEdit.text()
            print(self.camNo)     #''.join.locfile.read())
            self.lineEdit.setText(self.camNo)
            cap = cv2.VideoCapture(self.camNo)   # Start VideoCapture at cv2
            httpFileData = open("httpSet.txt","w")        # Saving the folder path to the file
            httpFileData.write(self.camNo)
            httpFileData.close()


        while(cap.isOpened()):          # while camera is opened read and show to live feed
            ret, frame = cap.read()

            cv2.imshow('TESTING CAMERA - Press escape to CLOSE',frame)
            if cv2.waitKey(1) == 27 :   # if escape is pressed !! MUST BE CHANGED TO WHEN Window 'X' is pressed !!
                break

        cap.release()
        cv2.destroyAllWindows()         # close cv2 all windows

    def select_Save_folder(self):       # Asks user to select a destination
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self,"Test","test")
        if folder_path:
            self.lineEdit_2.setText(folder_path)
            locfile = open("LocSet.txt","w")        # Saving the folder path to the file
            locfile.write(folder_path)
            locfile.close()
    
    def start_ss(self):                 # Start screenshots if movement is detected #### Imported from C:\Motion Detection and store image
        #self.ss_camNo = self.camNo       # CAN be changed to self Variable from checkCam 'camNo'
        #print(self.ss_camNo)

        ss_folder_path = self.lineEdit_2.text()     # Selected path to store the images
        print(ss_folder_path)
        
        self.ss_camNo = self.lineEdit.text()       # CAN be changed to self Variable from checkCam 'camNo'
        print(self.ss_camNo)

        if not ss_folder_path and self.ss_camNo == 'http://' or not self.lineEdit.text():                      # If not entered shows error
            QtWidgets.QMessageBox.about(self, "Choose Folder ", "Choose folder to store snapshots or initialize camera!!")
        else:
            os.chdir(ss_folder_path)        # Changes working dir to provided user path to save images
            self.cap = cv2.VideoCapture(self.ss_camNo)   # CAN be changed to self Variable from checkCam 'camNo'

        ss_folder_path = self.lineEdit_2.text()     # Selected path to store the images
        print(ss_folder_path)

        ret, frame1 = self.cap.read() 
        ret, frame2 = self.cap.read() 

        df = pd.DataFrame(columns=['timestamp', 'img_path'])

        

        # When Camera is Opened
        while self.cap.isOpened():
            diff = cv2.absdiff(frame1, frame2)  # returns abs difference value between frame1 and frame2
            gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)   # Converts to Gray Scale image
            blur = cv2.GaussianBlur(gray, (5,5), 0) 
            _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
            dilated = cv2.dilate(thresh, None, iterations=3)
            contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
            for contour in contours:
                (x, y, w, h) = cv2.boundingRect(contour)
        
                array = cv2.cvtColor(np.array(frame1), cv2.COLOR_RGB2BGR)
                image = Image.fromarray(array)

                file_path = ss_folder_path 
                
                #Needs calibration
                if cv2.contourArea(contour) < 2000: #if contour area is more than 2000px then store the image
                    continue
                
                self.imageNo = str(len(df))
                self.lcdNumber.display(self.imageNo)

                image.save(self.imageNo +'.jpg', "JPEG")   
                df.loc[len(df)] = [datetime.datetime.now(), file_path]

            # show feed view
            #self.L = [self.camNo, ss_folder_path]
            
            cv2.imshow("Live Camera Taking Snapshots !!", frame1)
            frame1 = frame2
            ret, frame2 = self.cap.read()
            self.pushButton_3.show()
            self.pushButton_2.hide()

            if cv2.waitKey(1) == 27 :
                print("Stopping")
                break
                
    def ss_stop(self):
        self.pushButton_2.show()
        self.pushButton_3.hide()

        cv2.destroyAllWindows()
        self.cap.release() 
        print(self.ss_camNo)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()