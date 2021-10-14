import cv2
from matplotlib import pyplot as plt
import np


suitImage = {}

def readSuitImage(path,label):
    img_find = cv2.imread(path)
    img_find = cv2.resize(img_find, (45,45), interpolation= cv2.INTER_LINEAR)

    img_find_gray = cv2.cvtColor(img_find, cv2.COLOR_BGR2GRAY)
    find_w, find_h = img_find_gray.shape[::-1]
    up_points = (find_w, find_h)
    (thresh, img_find_black) = cv2.threshold(img_find_gray, 127, 255, cv2.THRESH_BINARY)
    # img_find_black = (255-img_find_black)
    suitImage[label] = {
        "img_find" : img_find,
        "img_find_gray" : cv2.cvtColor(img_find, cv2.COLOR_BGR2GRAY),
        "find_w" : find_w,
        "find_h" : find_h,
        "up_points" : (find_w, find_h),
        "img_find_black" : img_find_black
    }


testImages = ["testImages/AHeartpng.png","testImages/8Club.png","testImages/7Diamond.png","testImages/2Spades.jpeg"]
readSuitImage("img/Clubs.png","Clubs");
readSuitImage("img/Diamonds.png","Diamonds");
readSuitImage("img/Spades.png","Spades");
readSuitImage("img/Heart.png","Hearts");


for imgPath in testImages:
    img = cv2.imread(imgPath)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    (thresh, img_black) = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
    ret , thrash = cv2.threshold(img_gray, 127 , 255, cv2.CHAIN_APPROX_NONE)
    contours , hierarchy = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    maxPredictionBlacks = 0
    predictionImage = None
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
        if len(approx) > 2:
            x = approx.ravel()[0]
            y = approx.ravel()[1] - 5
            x,y,w,h = cv2.boundingRect(contour)
            # cv2.rectangle(img_rgb,(x,y),(x+w,y+h),(0,255,0),2)
            crop_img = img_black[y:y+h, x:x+w]
            for label in suitImage:
                testImage = suitImage[label]
                resized_up = cv2.resize(crop_img, testImage["up_points"], interpolation= cv2.INTER_LINEAR)
                combinedImage = resized_up+testImage["img_find_black"]
                # combinedImage=cv2.addWeighted(resized_up, 0.5, testImage["img_find_black"], 0.5, 0)

                number_of_white_pix = np.sum(combinedImage == 255)
                number_of_black_pix = np.sum(combinedImage == 0)
                if maxPredictionBlacks < number_of_black_pix:
                    # print(f"Label:{label} White: {number_of_white_pix} Black: {number_of_black_pix} Len{len(approx)}" )
                    maxPredictionBlacks = number_of_black_pix
                    predictionImage = img[y:y+h, x:x+w]
                    predictionLabel = label
                    # cv2.imshow("cropped", resized_up)
                    # cv2.waitKey(0)
                    # cv2.imshow("cropped", testImage["img_find_black"])
                    # cv2.waitKey(0)
                    # cv2.imshow("cropped", combinedImage)
                    # cv2.waitKey(0)



    print(f"ImagePath:{imgPath} Label:{predictionLabel}" )

    # cv2.imshow("cropped", predictionImage)
    # # cv2.waitKey(0)
    # # plt.subplot(1, 1, 1)
    # # plt.imshow(img_rgb)
    # # cv2.waitKey(0)

    # plt.show()
    # cv2.waitKey(0)

