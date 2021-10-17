import cv2
import np
import math
import sys

def readTemplateImage(path, label, templateImages):
    img = cv2.imread(path)
    img = cv2.resize(img, (45, 45), interpolation=cv2.INTER_LINEAR)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    w, h = img_gray.shape[::-1]
    (thresh, img_black) = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
    templateImages[label] = {
        "scale": (w, h),
        "img": img_black
    }

def getGuess(img, templateImages):
    h, w, _ = img.shape
    # Keep onnly top left of the image to make prediciton more accurate
    img = img[0:math.ceil(h*0.3), 0:math.ceil(w*0.20)]
    # transform to black and white to count white and black pixels later
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # (thresh, img_black_or) = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)
    (thresh, img_black) = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
    ret, thrash = cv2.threshold(img_black, 127, 255, cv2.CHAIN_APPROX_NONE)

    # find shapes in image
    contours, hierarchy = cv2.findContours(
        thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    maxPredictionBlacks = 0
    minPredictionWhite = 100000000
    predictionImage = None
    IGNORE_SIZE_VALUE = 10

    for contour in contours:
        # get shape area
        x, y, w, h = cv2.boundingRect(contour)

        # ignore small shapes
        if w < IGNORE_SIZE_VALUE or h < IGNORE_SIZE_VALUE:
            continue

        # Get sub-image under investigation 
        sub_img_black = img_black[y:y+h, x:x+w]

        # test with all templpate images to find closest match
        for label in templateImages:
            templateImage = templateImages[label]

            # resize image to same dimmension as test image to be able to compare 
            sub_img_resized_black = cv2.resize(
                sub_img_black, templateImage["scale"], interpolation=cv2.INTER_LINEAR)

            # combine image to find common pixels
            combinedImage = sub_img_resized_black+templateImage["img"]

            # less white and more black pixels means that the images are similar
            number_of_white_pix = np.sum(combinedImage == 255)
            number_of_black_pix = np.sum(combinedImage == 0)

            # print(f"Label:{label} White: {number_of_white_pix} Black: {number_of_black_pix}" )
            # find the more black pixels
            if maxPredictionBlacks < number_of_black_pix:
                maxPredictionBlacks = number_of_black_pix
                predictionBlackImage = img[y:y+h, x:x+w]
                predictionBlackImageCombined = combinedImage
                predictionBlackLabel = label
            
            # find the less white pixels
            if minPredictionWhite > number_of_white_pix:
                minPredictionWhite = number_of_white_pix
                predictionWhiteImage = img_black[y:y+h, x:x+w]
                predictionWhiteImageCombined = combinedImage
                predictionWhiteLabel = label

    # cv2.imshow("cropped", predictionWhiteImage)
    # cv2.waitKey(0)

    return predictionBlackLabel, predictionWhiteLabel

# currently not working because it is 2 digits
# "10_Heart.png",

suitTemplateImages = {}
valueTemmplateImages = {}

BASE_TEMPLATE_IMAGE_FOLDER = "img"

suitImages = [
    "Club",
    "Diamond",
    "Spade",
    "Heart"
]

valueImages = [
    "Ace",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "J",
    "Q",
    "K"
]

for suitImage in suitImages:
    readTemplateImage(f"{BASE_TEMPLATE_IMAGE_FOLDER}/{suitImage}.png", suitImage, suitTemplateImages)

for valueImage in valueImages:
    readTemplateImage(f"{BASE_TEMPLATE_IMAGE_FOLDER}/{valueImage}.png", valueImage, valueTemmplateImages)

if __name__ == '__main__':
    BASE_TEST_IMAGE_FOLDER = "testImages"
    testImages = [
        "K_Heart.png",
        "Q_Diamond.png",
        "J_Spade.png",
        "9_Diamond.png",
        "8_Club.png",
        "7_Diamond.png",
        "6_Diamond.png",
        "5_Club.png",
        "4_Spade.png",
        "3_Diamond.png",
        "2_Spades.png",
        "Ace_Heart.png",
    ]

    for imgFile in testImages:
        img = cv2.imread(f"{BASE_TEST_IMAGE_FOLDER}/{imgFile}")
        suitBlack, suitWhite = getGuess(img, suitTemplateImages)
        valueBlack, valueWhite = getGuess(img, valueTemmplateImages)

        value = valueWhite
        suit = suitWhite

        # Min white produces more accurate results than max black
        # value = valueBlack
        # suit = suitBlack

        if value in imgFile and suit in imgFile:
            matched = "success"
        else:
            matched = "error"

        print(f"Predicted Value:{value} \nPredicted Suit:{suit}\nFor the image({imgFile}) the result is: {matched}\n")   