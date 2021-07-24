# Bicycle Detection

This project shows how to selectively detect a bicycle, even when many other objects exist. 
The file [Bicycle_Detection] (https://github.com/BakaZoro/ComputerVision/blob/master/Object_Detection/Bicycle_Detection/Bicycle_Detection.ipynb) implements selectively Bicycle detection
using ImageA! library.
The Yolo.v3 object recognition model is loaded as the object detection model. Pretrained weights from training on COCO dataset have been used. A custom model is then built to detect only 
bicycles instead of detecting other objects as well.

[test_images]] (https://github.com/BakaZoro/ComputerVision/tree/master/Object_Detection/Bicycle_Detection/test_images) include 5 images of cycles that I clicked with my phone camera.
[detected_images] (https://github.com/BakaZoro/ComputerVision/tree/master/Object_Detection/Bicycle_Detection/detected_images) includes the images after the bicycles were detected in them.
