# Simple-CarNumber-Detection
비디오 파일을 input으로 넣으면 하나의 차량 번호판을 인식하고 차량 번호판과 인식한 번호(예시 : OOO가 OOOO) 현재 시간과 함께 저장하는 간단한 프로그램입니다.   
   


https://github.com/UB-Mannheim/tesseract/wiki   

OCR용 라이브러리로 Tesseract를 사용했습니다.   

https://github.com/Mactto/License_Plate_Recognition   

또한 번호판 인식 알고리즘은 해당 github project의 소스코드를 사용했으며, 필요한 부분만을 남겨 plate_recognition.py 파일로 사용했습니다. 또한 main.py 에 필요한 함수 imwrite의 정의와 exception 처리 또한 포함되어 있습니다.    

이 프로젝트는 tesseract를 설치한 후, python main.py 명령어로 실행하여 사용이 가능합니다. 실행에는 plate_recognition.py 파일도 필요합니다.   
example.mp4 파일을 재생하고, 스페이스바 입력으로 일시정지 할 수 있습니다. 일시정지 상태에서는 두 가지 방법으로 차량 번호판 인식을 시도할 수 있습니다.   

1. 그냥 Enter키 입력하기
2. 마우스 왼쪽 클릭 4번으로 차량 번호판 지정 후, Enter키 입력하기


차량 번호판을 인식하는 과정은 동일하지만 영역을 직접 지정해 준 후, 해당 영역을 getPerspectiveTransForm 함수와 warpPerspective 함수로 평탄화해서 인식을 시도할 수 있습니다.   
<img src="https://github.com/SeukCho/Simple-CarNumber-Detection/blob/main/example1.png" width="50%" height="50%">

일반적인 Enter 키 입력으로 차량 번호판을 인식한 모습입니다. 번호판의 대략적인 위치와, 인식한 번호판의 글자가 표시됩니다.   

<img src="https://github.com/SeukCho/Simple-CarNumber-Detection/blob/main/example2.png" width="50%" height="50%"><img src="https://github.com/SeukCho/Simple-CarNumber-Detection/blob/main/example3.png" width="50%" height="50%">   
번호판을 지정한 후 Enter키를 입력하여 인식한 모습입니다.   

Tesseract 자체가 한글 인식률이 높지 않아 실제 인식률 자체는 좋지 않습니다. 인식하면 인식한문자열_y-m-d-HMS.jpg 의 형식으로 pics 폴더에 저장됩니다. 저장된 샘플은 깃허브 pics 폴더에서도 확인할 수 있습니다. 인식하지 못한 경우 Cannot find license plate. 라고 콘솔에 표시됩니다. 또한 엔터키를 눌러서 인식을 시도한 후 ESC를 눌러 다시 인식을 시도해 볼 수 있고, 마우스 왼쪽 클릭으로 영역을 지정할 때에는 4가지 점을 모두 입력하기 전까지는 엔터키를 눌러도 반응하지 않습니다.
   
example.mp4 파일은 직접 촬영한 영상입니다. 해당 방식을 활용한 real-time 인식은 실시간으로 처리할 수 없을 정도로 느린 속도를 보여서 일시정지하는 방식으로 변경했습니다.
