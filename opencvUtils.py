import cv2
from cv2 import findContours


def Sobel(name):
    image = cv2.imread(name, cv2.IMREAD_GRAYSCALE)  # H W C
    sobxel_h = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    # Sobelx [[-1,0,1]
    #        [-2,0,2]
    #        [-1,0,1]]
    sobxel_h = cv2.convertScaleAbs(sobxel_h)

    sobxel_v = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    sobxel_v = cv2.convertScaleAbs(sobxel_v)

    Sobel_all = cv2.addWeighted(sobxel_h, 0.5, sobxel_v, 0.5, 0)
    return savePicture(name, Sobel.__name__, Sobel_all)


def Scharr(name):
    # Scharr [[-3,0,3]
    #        [-10,0,10]
    #        [-3,0,3]]
    image = cv2.imread(name, cv2.IMREAD_GRAYSCALE)  # H W C
    scharrx = cv2.Scharr(image, cv2.CV_64F, 1, 0)
    scharry = cv2.Scharr(image, cv2.CV_64F, 0, 1)
    scharrx = cv2.convertScaleAbs(scharrx)
    scharry = cv2.convertScaleAbs(scharry)
    Scharr_all = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)
    return savePicture(name, Scharr.__name__, Scharr_all)


def Laplacian(name):
    # Laplacian [[0,1,0]
    #          [1,-4,1]
    #          [0,1,0]]
    image = cv2.imread(name, cv2.IMREAD_GRAYSCALE)  # H W C
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    laplacian = cv2.convertScaleAbs(laplacian)
    return savePicture(name, Laplacian.__name__, laplacian)


def Canny(name):
    """
    高斯滤波器
    Sobel算子
    非极大值抑制(edge)[min,max]
    <min不考虑,>max认为是边界,min~max判断是否是边界
    双阈值
    """
    image = cv2.imread(name, cv2.IMREAD_GRAYSCALE)  # H W C
    conny = cv2.Canny(image, 100, 200)
    return savePicture(name, Canny.__name__, conny)


def FindContours(image):
    # cv2.RETR_EXTERNAL 检索最外侧轮廓
    # cv2.RETR_TREE 检索所有轮廓
    ret, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    draw_image = image.copy()
    newImage = cv2.drawContours(draw_image, contours, -1, (0, 0, 255), 2)
    return newImage


class GaussPyramid:
    # 高斯内核卷积 下采样
    # 零填充 上采样
    def __init__(self, name) -> None:
        self.name = name
        self.image = cv2.imread(name, cv2.IMREAD_GRAYSCALE)  # H W C

    def up(self):
        newImage = cv2.pyrUp(self.image)
        return savePicture(self.name, "GaussPyramidUp", newImage)

    def down(self):
        newImage = cv2.pyrDown(self.image)
        return savePicture(self.name, "GaussPyramidDown", newImage)


def savePicture(name, functionName, image):
    """
    get picture name from absoluate path and save the new image under folder (./images)
    """
    newPictureName = f"./images/{name.split('/')[-1].split('.')[0]}_{functionName}.png"
    cv2.imwrite(newPictureName, image)
    return newPictureName
