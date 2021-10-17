import cv2

testImages = [
        "testSeparator/4aces1.jpg",
        "testSeparator/4aces2.jpg",
        "testSeparator/5-5-2.jpg",
        "testSeparator/k-10.png",
        "testSeparator/all.png"
]


def card_separator(img_path):
    img = cv2.imread(img_path)
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
                cropped_image = img[y:y + h, x:x + w]
                #cv2.drawContours(img, [contour], 0, (0, 0, 255), 1)
                yield cropped_image
    
    cv2.imshow('selected_contours', img)
    


i = 0
for c in list(card_separator(testImages[1])):
    i += 1
    cv2.imwrite(str(i) + '.png', c)





