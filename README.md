# Simple-CarNumber-Detection
이미지 또는 비디오 파일을 input으로 넣으면 장면당 하나의 차량 번호판을 인식하고 차량 번호판과 인식한 번호(예시 : OOO가 OOOO) 현재 시간과 함께 저장하는 간단한 프로그램입니다.   
   


https://github.com/UB-Mannheim/tesseract/wiki   

OCR용 라이브러리로 Tesseract를 사용했습니다.   

https://github.com/Mactto/License_Plate_Recognition   

또한 번호판 인식 알고리즘은 해당 github project의 소스코드를 사용했으며, 필요한 부분만을 남겨 plate_recognition.py 파일로 사용했습니다.   

이 프로젝트는 tesseract를 설치한 후, python main.py 명령어로 실행하여 사용이 가능합니다.