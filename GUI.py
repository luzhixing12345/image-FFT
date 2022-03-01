
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from SVG import bitmap_to_contour_svg, writeFile
from fft import draw

from opencvUtils import *


class InteractiveWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        #configuration
        self.setWindowTitle('Visiable FFT image')
        self.resize(500,500)
        
        self.layout_main = QHBoxLayout()
        
        self.layoutLeft = QFormLayout()
        self.layoutRight = QFormLayout()
        
        self.leftForm()
        self.rightForm()
        
        self.layout_main.addLayout(self.layoutLeft)
        self.layout_main.addLayout(self.layoutRight)
        self.setLayout(self.layout_main)

        
    def leftForm(self):
        
        self.edgeProcessingMethodChoose = QComboBox()
        self.edgeProcessingMethodChoose.addItems(["Canny","Sobel","Laplacian","Scharr"])
        self.edgeProcessingMethod = {
            "Canny":Canny,
            "Sobel":Sobel,
            "Scharr":Scharr,
            "Laplacian":Laplacian,
        }
        self.layoutLeft.addRow("图片边缘处理方式",self.edgeProcessingMethodChoose)
        # load picture
        self.button_1 = QPushButton("导入图片")
        self.button_1.clicked.connect(self.loadPicture)
        
        # processing image
        self.button_2 = QPushButton("处理图片")
        self.button_2.clicked.connect(self.processImage)
        
        # make svg picture
        self.button_3 = QPushButton("生成结果")
        self.button_3.clicked.connect(self.fftImageProcess)
        
        self.layoutLeft.addWidget(self.button_1)
        self.layoutLeft.addWidget(self.button_2)
        self.layoutLeft.addWidget(self.button_3)
    
    def rightForm(self):
        
        self.picture = QLabel()
        self.layoutRight.addWidget(self.picture)

        
    def loadPicture(self):
        '''
        load picture from the computer content
        G:\\learnerLu\\image-FFT
        '''
        self.fname, _ = QFileDialog.getOpenFileName(self, '选择图片', 'G:\\learnerLu\\image-FFT\\examples', 'Image files(*.jpg *.gif *.png *.jpeg)')
        # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        self.picture.setPixmap(QPixmap(self.fname))

    def processImage(self):
        '''
        use th selected method to process the image to get the edge
        '''
        processMethod = self.edgeProcessingMethod[self.edgeProcessingMethodChoose.currentText()]
        
        newPictureName = processMethod(self.fname)
        #print(newPictureName)
        self.picture.setPixmap(QPixmap(newPictureName))

    def fftImageProcess(self):
        newPictureName = f"./images/{self.fname.split('/')[-1].split('.')[0]}.svg"
        fileName = f"./images/{self.fname.split('/')[-1].split('.')[0]}.txt"
        
        bitmap_to_contour_svg(self.fname,newPictureName)
        self.picture.setPixmap(QPixmap(newPictureName))
        writeFile(newPictureName,fileName)
        #fftProcess(fileName)
        draw(fileName)
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tool = InteractiveWindow()
    tool.show()
    sys.exit(app.exec_())