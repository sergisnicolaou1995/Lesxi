import cv2
import os
import np

def card_separator(img):
    #img = cv2.resize(img, (100, 100), interpolation=cv2.INTER_LINEAR)
    shape = img.shape
    orig_area = shape[0] * shape[1]
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, threshold = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(
            threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


    i = 0
    for contour in contours:
        if i == 0:
            i = 1
            continue
        x, y, w, h = cv2.boundingRect(contour)
        area_ratio = ((w * h)/ orig_area)
        
        if area_ratio >= 0.01:
            approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
            if len(approx) <= 10:
                # cropped_image = img[y:y + h, x:x + w]

                # Instead of bounding rect keep only the image part with transparent background
                mask = np.zeros_like(img_gray) # Create mask where white is what we want, black otherwise
                cv2.drawContours(mask, contours, i, 255, -1) # Draw filled contour in mask
                cardImage = np.zeros_like(img_gray) # Extract out the object and place into output image
                cardImage[mask == 255] = img_gray[mask == 255]

                # Crop the image based on the mask
                (y, x) = np.where(mask == 255)
                (topy, topx) = (np.min(y), np.min(x))
                (bottomy, bottomx) = (np.max(y), np.max(x))
                cardImage = cardImage[topy:bottomy+1, topx:bottomx+1]
    
                yield cardImage
        i += 1    

if __name__ == '__main__':
    SEPERATOR_IMAGE_FOLDER = "testSeparator"
    SEPERATOR_RESULTS_FOLDER = "seperatorResults"
    testImages = [
            "4aces1.jpg",
            "4aces2.jpg",
            "5-5-2.jpg",
            "k-10.png",
            "all.png"
    ]
    if not os.path.exists(SEPERATOR_RESULTS_FOLDER):
        os.makedirs(SEPERATOR_RESULTS_FOLDER)

    k = 0
    for testImage in testImages:
        k += 1
        name = testImage.split('.')[0]
        imageDirectory = f"{SEPERATOR_RESULTS_FOLDER}/{name}"
        if not os.path.exists(imageDirectory):
            os.makedirs(imageDirectory)
        i = 0
        img = cv2.imread(f"{SEPERATOR_IMAGE_FOLDER}/{testImage}")
        for c in list(card_separator(img)):
            i += 1
            cv2.imwrite(f"{imageDirectory}/{i}.png", c)



