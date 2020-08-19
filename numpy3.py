## 题目

#在彩色图像中，一般有3个通道，分别是R、G、B三个通道，每个通道上都有一个相同大小的矩阵，矩阵上的元素取值范围为0～255。 
#灰度图像则只有一个通道，即只有一个矩阵，元素取值范围为0～255. 现在请你写一个方法，将一张彩色图片转为灰度图片。 
#其中，彩色转灰度的方式可以采用平均法，即将R、G、B 3个通道的每个像素点加和取平均。
from numpy.core.multiarray import ndarray
import numpy as np
from PIL import Image


def image_gray(image_ar: ndarray) -> ndarray:
    # todo: 使用平均法对图像进行灰度化处理
    r, g, b = image_ar[:, :, 0], image_ar[:, :, 1], image_ar[:, :, 2]
    gray = (r + g + b)/3
    return gray


def read_image(image_path: str) -> ndarray:
    image = Image.open(image_path)
    return np.array(image)


def show_image_array(image_ar: ndarray):
    image = Image.fromarray(image_ar)
    image.show()


if __name__ == "__main__":
    image_array = read_image('image.jpg')
    array = image_gray(image_array)
    show_image_array(array)
 