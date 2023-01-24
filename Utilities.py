import cv2
from matplotlib import pyplot as plt
import webcolors as wc
import numpy as np


def showHistogram(img):
    color = ('b', 'g', 'r')
    if len(img.shape) == 2:
        color = ('b')
    #plt.close()
    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.show()

def plotHistogramVector(histogram):
    plt.plot(histogram, color='b')
    plt.xlim([0, len(histogram)])
    plt.show()

def grabWebcam():
    cap = cv2.VideoCapture(0)
    while True:
        ret, im = cap.read()
        cv2.imshow('video test', im)
        key = cv2.waitKey(10)
        if key == 27:
            break
        # if key == ord(' '):
        # cv2.imwrite('vid_result.jpg',im)

def color_name(rgb):
    if np.isscalar(rgb):
        res = ["black"] * 51 + ["dark gray"] * 51 + ["gray"] * 52 + ["light gray"] * 51 + ["white"] * 51
        return res[rgb]
    
    colors_dist = {} # euklidischer Abstand zu Farbbezeichnungen im css3 rgb-Farbraum
    for key, name in wc.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = wc.hex_to_rgb(key)
        colors_dist[(r_c - rgb[0]) ** 2 + (g_c - rgb[1]) ** 2 + (b_c - rgb[2]) ** 2] = name
    return colors_dist[min(colors_dist.keys())]

