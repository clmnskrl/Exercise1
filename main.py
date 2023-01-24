import cv2
import ImageManipulation as IM
import Utilities




# This is some sample code. Feel free to delete the functions "getCroppedImage" and "onMouse"
def getCroppedImage(img, x,y, width, height, zoom):
    cropped = img[y-int(height/2):y+int(height/2), x-int(width/2):x+int(width/2)]
    Utilities.showHistogram(cropped)
    cropped = cv2.resize(cropped, None, fx=zoom, fy=zoom, interpolation=cv2.INTER_NEAREST)
    return cropped

def onMouse(event, x, y, flags, img):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('x = %d, y = %d'%(x, y))
        print("Color of the pixel (%d, y = %d): "%(x,y) + str(img[y, x]))
        cropped = getCroppedImage(img, x,y, 100, 100, 4)

        cv2.imshow('zoomed', cropped)
        cv2.resizeWindow('zoomed', 300, 300)
        #cv2.waitKey()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    g = cv2.imread('./SampleData/classics/cat.png', 0)
    c = cv2.imread('./SampleData/classics/cat.png', 1)

    IM.printImageDetails(c)
    IM.printImageDetails(g)

    cv2.imshow('Cat_color', c)
    cv2.imshow('Cat_gray', g)
    cv2.waitKey(0)



    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    #cv2.imshow('Image', img)
    #cv2.setMouseCallback('Image', onMouse, img)
    #cv2.waitKey()

    #Utilities.showHistogram(img)

    #flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
    #print( flags )
    #cv2.imshow('Image', fruits)
    #IM.myFirstImageManipulation(img = fruits)
    #cv2.imshow('Image_mod', fruits)
