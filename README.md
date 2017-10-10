# Camcha.OpenCV
### 2017.10.10
이미지 차이를 이용한 탐지
-------------

1. 밝은 이미지와 어두운 이미지의 rgb값의 차이를 이용해서 탐지하는 방법
![Alt text](https://raw.githubusercontent.com/SoftMilkTea/Camcha.OpenCV/master/images/bright_spot.jpg) ![Alt text](https://raw.githubusercontent.com/SoftMilkTea/Camcha.OpenCV/master/images/dark_spot.jpg)
두 이미지의 차이 이미지
![Alt text](https://raw.githubusercontent.com/SoftMilkTea/Camcha.OpenCV/master/images/subtarction_image.jpg)
보이는 바와 같이 육안으로도 점의 위치를 파악하기 어렵다.

결과는 실패..

밝은 이미지 만을 이용한 탐지
-------------

* 원본 이미지
![Alt text](/path/to/img.jpg)

* 필터를 적용한 이미지(필터를 적용하지 않으면 노이즈 발생)
![Alt text](https://raw.githubusercontent.com/SoftMilkTea/Camcha.OpenCV/master/images/spot_origin_image.jpg)
* 스레시홀드 값을 적용시킨 이미지
![Alt text](https://raw.githubusercontent.com/SoftMilkTea/Camcha.OpenCV/master/images/spot_threshhold_img.jpg)
* 마지막으로 캐니알고리즘을 적용시킨 이미지
![Alt text](https://raw.githubusercontent.com/SoftMilkTea/Camcha.OpenCV/master/images/spot_canney_img.jpg)


