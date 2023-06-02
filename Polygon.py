import cv2
import easyocr
image = cv2.imread('chinese.jpg')

# perform character recognition
reader = easyocr.Reader(['en', 'ch_tra'])
results = reader.readtext(image)
# iterate on all results
for res in results:
    top_left = tuple(res[0][0]) # top left coordinates as tuple
    bottom_right = tuple(res[0][2]) # bottom right coordinates as tuple
    # draw rectangle on image
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
    # write recognized text on image (top_left) minus 10 pixel on y
    cv2.putText(image, res[1], (top_left[0], top_left[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("rectangle", image)
    cv2.waitKey()