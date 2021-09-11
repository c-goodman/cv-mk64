# cv-mk64
This project uses a combination of computer vision to scrape dolphin emulated Mario Kart 64

Much inspiration, and code, taken from [Learn Code by Gaming's "OpenCV Object Detection in Games" playlist.](https://www.youtube.com/playlist?list=PL1m2M8LQlzfKtkKq2lK5xko4X-8EZzFPI) Besides the ins-and-outs of OpenCV, Ben's videos also helped me learn a lot about classes in python. Specifically the code for fast window capture. Check out [learncodebygaming's github](https://github.com/learncodebygaming) and [opencv_tutorials](https://github.com/learncodebygaming/opencv_tutorials) repo!

Inspiration was also taken from [Clarity Coder's "Computer Vision - OpenCV" playlist.](https://youtube.com/playlist?list=PLFAkc-SDlaKwdZqul_KTpNsw1U2ViKmbD) This was where I first encountered the OpenCV library and got the idea for this project, so many thanks!


## Virtual Environment

I tried to use conda as a package manager but most of the libraries worked better with 'pip' and a plain python virtual environment ([venv](https://docs.python.org/3/library/venv.html)).

I also ended up downloading [NVIDIA's CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit) for use with [easyocr](https://github.com/JaidedAI/EasyOCR) and it's [PyTorch](https://pytorch.org/) dependancies. 

### Contents (2021-09-11)

```
(env) C:\Users\Cooper\cv-mk64>pip list
Package           Version
----------------- ------------
cycler            0.10.0      
easyocr           1.4
imageio           2.9.0       
kiwisolver        1.3.2       
matplotlib        3.4.3
networkx          2.6.3
numpy             1.21.2
opencv-python     4.5.3.56
Pillow            8.3.2
pip               21.2.4
pyparsing         2.4.7
python-bidi       0.4.2
python-dateutil   2.8.2
PyWavelets        1.1.1
pywin32           301
PyYAML            5.4.1
scikit-image      0.18.3
scipy             1.7.1
setuptools        56.0.0
six               1.16.0
tifffile          2021.8.30
torch             1.9.0+cu111
torchaudio        0.9.0
torchvision       0.10.0+cu111
typing-extensions 3.10.0.2
```