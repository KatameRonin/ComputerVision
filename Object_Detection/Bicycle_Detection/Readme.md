# Bicycle Detection

This project shows how to selectively detect a bicycle, even when many other objects exist. 
The file [Bicycle_Detection] (./Object_Detection/Bicycle_Detection/Bicycle_Detection.ipynb) implements selectively Bicycle detection
using ImageAI library.
The Yolo.v3 object recognition model is loaded as the object detection model. Pretrained weights from training on COCO dataset have been used. A custom model is then built to detect only 
bicycles instead of detecting other objects as well.

[test_images]] (./Object_Detection/Bicycle_Detection/test_images) include 5 images of cycles that I clicked with my phone camera.
[detected_images] (./Object_Detection/Bicycle_Detection/detected_images) includes the images after the bicycles were detected in them.
