# yolo-v3-with-bdd

# Intro
Yolo Object detection algo has gained a lot of attention in the last couple years that even big players in autonomous vehicles apply YOLOv3 in their object detection algorithm.
This repo is my side project that to develop a YOLOv3 object detection algo with BDD100K data set that is recently released by UC Berkeley in 2018.

# To-Do
(1) Convert BDD100K data label to YOLOv3 standard -- [DONE]

(2) Train YOLOv3 network with yolov3 ready data -- [IN PROGRESS]

# Training Command
./darknet detector train cfg/bdd100k.data cfg/yolov3-tiny-bdd100k.cfg weight/darknet53.conv.74



# Reference
BDD100K : A Large-scale Diverse Driving Video Database
https://bair.berkeley.edu/blog/2018/05/30/bdd/

YOLO: Real-Time Object Detection
https://pjreddie.com/darknet/yolo/
