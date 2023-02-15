# Turtle_Neck_Syndrome_Discriminator  


### INTRODUCTION <a name="introduction"></a>

---

이미지 또는 영상 기반의 데이터를 통해 AI 모델 기반의 거북목 판별 알고리즘을 적용하여 거북목 여부를 판별하여 검출한다.  
Image or video based data is applied to AI model based turtle neck syndrome discriminator algorithm to detect whether it is a turtle neck or not.


This application uses the following tools:

> Python 3.11.2  
> OpenCV 4.7.0


### DONE <a name="done"></a>

---

* 거북목 진단 기준 
  - 전방머리자세각도(Craniovertebral Angle, CV 각도)를 측정하여 거북목 증후군을 판단 . CV 각도가 50° 미만일 경우에 일반 적으로 거북목 증후군이라고 판단
  - 그러나 일상 에서 CV 각도를 정확하게 측정하는 것이 어려우므로, 좀 더 단순화된 방법으로
귀구슬로부터 견봉점까 지의 수평거리(Acromion distance)를 거북목 자세 판별 기준으로 사용할 수 있다.
이 점들 간의 거리가 2.5cm 이하이면 정상, 2.5cm 이상 나오면 거 북목이 진행되고 있는 상태이며, 5cm 이상 나왔을 때는 심각한 거북목 상태로 판별 (from Responsive Healthcare System for Posture Correction Using WebcamBased Turtle Neck Syndrome Discrimination Algorithm)



### TODO <a name="todo"></a>

---



* 거북목 진단 기준에 따른 판별 알고리즘 개발
* 활용 모델 검토





### REFERENCE <a name="reference"></a>

---

* 웹캠 기반 거북목 판별 알고리즘을 활용한자세 교정 반응형 헬스케어 시스템 : http://koreascience.or.kr/article/JAKO202106763002134.pdf
* CNN기반의 학습모델을 활용한 거북목 증후군 자세 교정 시스템 : http://koreascience.or.kr/article/JAKO202022560454953.pdf




### TIPS <a name="tips"></a>

---

