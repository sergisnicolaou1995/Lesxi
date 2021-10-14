import cv2
from matplotlib import pyplot as plt
import np


suitImage = {}
valueImage = {}

def readTemplateImage(path,label,templateObj):
    img_find = cv2.imread(path)
    img_find = cv2.resize(img_find, (45,45), interpolation= cv2.INTER_LINEAR)

    img_find_gray = cv2.cvtColor(img_find, cv2.COLOR_BGR2GRAY)
    find_w, find_h = img_find_gray.shape[::-1]
    up_points = (find_w, find_h)
    (thresh, img_find_black) = cv2.threshold(img_find_gray, 127, 255, cv2.THRESH_BINARY)
    # img_find_black = (255-img_find_black)
    templateObj[label] = {
        "img_find" : img_find,
        "img_find_gray" : cv2.cvtColor(img_find, cv2.COLOR_BGR2GRAY),
        "find_w" : find_w,
        "find_h" : find_h,
        "up_points" : (find_w, find_h),
        "img_find_black" : img_find_black
    }


testImages = [
    "testImages/KHeart.png",
    "testImages/QDiamond.png",
    "testImages/JSpade.png",
    "testImages/10Heart.png",
    "testImages/9Diamond.png",
    "testImages/8Club.png",
    "testImages/7Diamond.png",
    "testImages/6Diamond.png",
    "testImages/5Club.png",
    "testImages/4Spade.png",
    "testImages/3Diamond.png",
    "testImages/2Spades.png",
    "testImages/AHeart.png",
]
readTemplateImage("img/Clubs.png","Clubs",suitImage);
readTemplateImage("img/Diamonds.png","Diamonds",suitImage);
readTemplateImage("img/Spades.png","Spades",suitImage);
readTemplateImage("img/Heart.png","Hearts",suitImage);

readTemplateImage("img/Ace.png","Ace",valueImage);
readTemplateImage("img/2.png","2",valueImage);
readTemplateImage("img/3.png","3",valueImage);
readTemplateImage("img/4.png","4",valueImage);
readTemplateImage("img/5.png","5",valueImage);
readTemplateImage("img/6.png","6",valueImage);
readTemplateImage("img/7.png","7",valueImage);
readTemplateImage("img/8.png","8",valueImage);
readTemplateImage("img/9.png","9",valueImage);
readTemplateImage("img/10.png","10",valueImage);
readTemplateImage("img/J.png","J",valueImage);
readTemplateImage("img/Q.png","Q",valueImage);
readTemplateImage("img/K.png","K",valueImage);

counterIndex = 459

def getGuess(imgPath,templateObj):

    img = cv2.imread(imgPath)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # (thresh, img_black_or) = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)

    (thresh, img_black) = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
    ret , thrash = cv2.threshold(img_black, 127 , 255, cv2.CHAIN_APPROX_NONE)
    contours , hierarchy = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    maxPredictionBlacks = 0
    predictionImage = None
    counter = 0
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
        # if len(approx) > 2:
        if len(approx) > -1:
            x = approx.ravel()[0]
            y = approx.ravel()[1] - 5
            x,y,w,h = cv2.boundingRect(contour)
            # cv2.rectangle(img_black,(x,y),(x+w,y+h),(0,255,0),2)
            # print(f"{counter} Angles:{len(approx)}")
            # cv2.putText(img_black, str(counter), (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
            crop_img = img_black[y:y+h, x:x+w]
            for label in templateObj:
                testImage = templateObj[label]
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
            counter = counter + 1


    # img_rgb = cv2.resize(img_black, (400,400), interpolation= cv2.INTER_LINEAR)
    # cv2.imshow("cropped", img_black)
    # cv2.waitKey(0)

    # x,y,w,h = cv2.boundingRect(contours[counterIndex])
    # # cv2.rectangle(img_rgb,(x,y),(x+w,y+h),(0,255,0),2)

    # crop_img = img_black_or[y:y+h, x:x+w]
    # cv2.imshow("cropped", crop_img)
    # cv2.waitKey(0)

    return predictionLabel
    


for imgPath in testImages:
    suit = getGuess(imgPath,suitImage)
    value = getGuess(imgPath,valueImage)
    print(f"ImagePath:{imgPath} Value:{value} Suit:{suit}")

