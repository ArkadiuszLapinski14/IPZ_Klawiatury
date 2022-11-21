import cv2
import mediapipe as mp
import time
import Modules.HandTrackingModule as htm
from Keyboard import Keyboard
from HandMovingKeyboard import HandMovingKeyboard

def main():
    pTime = 0

    cap = cv2.VideoCapture(0)
    detector = htm.handDetector(maxHands=1)
    classic_keyboard = Keyboard()
    handMovingKeyboard = HandMovingKeyboard(classic_keyboard)

    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        img = detector.findHands(img)
        lmList = detector.findPosition(img)

        handMovingKeyboard.update(lmList)

        classic_keyboard.draw(img)
        img = classic_keyboard.update()

        ###FPS###
        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime

        ###DRAW RESULT###
        try:
            img = handMovingKeyboard.draw_result(img)
        except:
            print("nie dziala")
        #################
        
        cv2.putText(img, str(int(fps)),(0,15), cv2.FONT_HERSHEY_PLAIN, 1 ,(255,0,255), 2)
        cv2.imshow("Image", img)
        cv2.waitKey(1)
        #########

if __name__ == '__main__':
    main()

