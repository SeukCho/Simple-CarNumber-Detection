import cv2
import numpy as np
import pytesseract
import os
import time
from PIL import ImageFont, ImageDraw, Image
from plate_recognition import imwrite, recognize_plate

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe' 
# Tesseract가 설치된 경로에 맞게 경로 수정해야 작동함
# 한국어에 대한 확장을 선택해서 설치해야 함.

import numpy as np
import cv2

def correct_perspective(image, points):
    
    # 네 개의 좌표를 순서대로 연결합니다.
    pts1 = np.float32(points)   
    

    # 보정된 직사각형의 가로 세로 길이 계산
    width = max(np.linalg.norm(pts1[0] - pts1[1]), np.linalg.norm(pts1[2] - pts1[3]))
    height = max(np.linalg.norm(pts1[0] - pts1[3]), np.linalg.norm(pts1[1] - pts1[2]))

    # 보정된 직사각형의 좌표 정의
    pts2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])

    # 변환 행렬 계산
    M = cv2.getPerspectiveTransform(pts1, pts2)

    # 이미지 보정
    corrected_image = cv2.warpPerspective(image, M, (int(width), int(height)))

    return corrected_image

cap = cv2.VideoCapture('example.mp4')
points = []

def mouse_callback(event, x, y, flags, param):
    global points
    
    if event == cv2.EVENT_LBUTTONDOWN and not is_playing:
        if len(points) < 4:
            points.append((x, y))
        
if not cap.isOpened():
    print("Cannot open video file.")
    exit()
    
is_playing= True
did_recognized = False
while True:
    if is_playing:
        ret, frame = cap.read()
        if not ret:
            print("End of Video")
            break    
    
    cv2.imshow('Video', frame)
    
    
    
    key = cv2.waitKey(10)
    if key == ord(' '):
        frame_copy = frame.copy()
        if not is_playing:
            points = []
            did_recognized = False
        is_playing = not is_playing        
    elif key == ord('q'):
        break
    elif not is_playing and key == 27:
        frame = frame_copy
        points = []
        did_recognized = False
    
    
    if not is_playing and not did_recognized:
        cv2.setMouseCallback('Video', mouse_callback)
        for point in points:
            cv2.circle(frame, point, 5, (0, 255, 0), -1)
            
        if len(points) > 1:
            for i in range(1, len(points)):
                cv2.line(frame, points[i-1], points[i], (0, 255, 0), 2)
        if len(points)==4:
            cv2.line(frame, points[0], points[3], (0, 255, 0), 2)
            corrected_image = correct_perspective(frame_copy, points)

            cv2.imshow("Adjusted image", corrected_image)
    
    if not is_playing and (len(points) == 0 or len(points) == 4)and key == 13 and not did_recognized:
                if len(points) == 0:
                    info, chars = recognize_plate(frame)
                    if info and chars is not None:
                        cv2.rectangle(frame, pt1=(info['x'], info['y']), pt2=(info['x']+info['w'], info['y']+info['h']), color=(255,0,0), thickness=2)  
                        pil_image = Image.fromarray(frame)
                        draw = ImageDraw.Draw(pil_image)
                        font = ImageFont.truetype("fonts/malgunbd.ttf", size=24)
                        draw.text((info['x'], info['y']-50), chars, font=font, fill=(0,0,0))
                        frame = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)   
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  
                        did_recognized = True
                else:
                    info, chars = recognize_plate(corrected_image)
                    if info and chars is not None: 
                        pil_image = Image.fromarray(frame)
                        draw = ImageDraw.Draw(pil_image)
                        font = ImageFont.truetype("fonts/malgunbd.ttf", size=24)
                        draw.text((points[0][0], points[0][1]-50), chars, font=font, fill=(0,0,0))
                        frame = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)   
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        did_recognized = True

               
            
        
        
cap.release()
cv2.destroyAllWindows()