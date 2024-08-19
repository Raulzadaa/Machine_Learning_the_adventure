import cv2 
import mediapipe as mp
import pyautogui as bot
import time as tm

video = cv2.VideoCapture(0)

hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=1)

mpDraw = mp.solutions.drawing_utils

while True:

    ret , frame = video.read()
    imgRGB = cv2.cvtColor( frame, cv2.COLOR_BGR2RGB)

    results = Hand.process(imgRGB)
    handsPoints = results.multi_hand_landmarks

    h , w, _ = frame.shape

    pontos = []

    if handsPoints:
        for points in handsPoints:
            # print(points)
            mpDraw.draw_landmarks(frame, points, hand.HAND_CONNECTIONS)
            
            for id,cord in enumerate(points.landmark):
                cx , cy = int(cord.x*w) , int(cord.y*h)
                cv2.putText(frame, str(id), (cx -5 , cy + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (161, 146 , 0), 2) #blue green red
                pontos.append((cx,cy))

        dpol ,dind , dmid , dring , dlittle = 4, 8 , 12 , 16 , 20

        if points:

            if (pontos[dind][1] < pontos[dind - 2 ][1]) and (pontos[dmid][1] < pontos[dmid - 2 ][1]):
                bot.keyDown("w")
                tm.sleep(0.3)
                bot.keyUp("w")

            elif pontos[dind][1] < pontos[dind - 2 ][1]:
                bot.keyDown("a")
                tm.sleep(0.3)
                bot.keyUp("a")

            elif pontos[dlittle][1] < pontos[dlittle - 2 ][1]:
                bot.keyDown("d")
                tm.sleep(0.3)
                bot.keyUp("d")

            elif pontos[dpol][0] > pontos[dpol - 1][0]:
                bot.keyDown("s")
                tm.sleep(0.3)
                bot.keyUp("s")

            elif pontos[dmid][1] < pontos[dmid - 2][1]:
                bot.keyDown("SPACE")
                tm.sleep(0.3)
                bot.keyUp("SPACE")
            
    cv2.imshow("Imagem", frame)

    wk = cv2.waitKey(1)
    if wk == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
exit()