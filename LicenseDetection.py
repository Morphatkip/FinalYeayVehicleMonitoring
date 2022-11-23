# ProjectGurukul Number plate recognition
# import necessary packages

import cv2
import easyocr


def licenceId(img):
    platedetails ='null'
    # initialize cascade classifier 
    numberPlate_cascade = "numberplate_haarcade.xml"
    detector = cv2.CascadeClassifier(numberPlate_cascade)

    # initialize the easyocr Reader object 
    reader = easyocr.Reader(['en'],  gpu=False, verbose=True)

    # read image
    img = cv2.imread('car.jpeg')

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #-- Detect Number plates
    plates = detector.detectMultiScale(
            img_gray,scaleFactor=1.05, minNeighbors=7,
            minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    #print(plates)


    # iterate through each detected number plates
    for (x,y,w,h) in plates:

        # draw bounding box
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Crop the numberplate
        plateROI = img_gray[y:y+h,x:x+w]

        #cv2.imshow("Numberplate", plateROI)

        # detect text
        
        text = reader.readtext(plateROI)

        if len(text) == 0:
            continue
        #print( text)
        platedetails =text[0][1]
       

        # draw text in the frame
        cv2.putText(img, text[0][1], (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2) 

    # Show the final output
    #cv2.imshow('Output', img)

    # wait until  any key is pressed
    cv2.waitKey(0)
    return(platedetails)

