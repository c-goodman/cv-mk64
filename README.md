# cv-mk64
This project uses a combination of Computer Vision ([OpenCV-Python](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)) and Optical Character Recognition [EasyOCR](https://github.com/JaidedAI/EasyOCR) to automatically scrape information from Mario Kart 64 playing on a [Dolphin Emulator](https://dolphin-emu.org/).

**GOAL:** Populate either a locally hosted Pandas DataFrame or MongoDB server with scraped information to track player performance statistics. 

Much inspiration, and code, taken from [Learn Code by Gaming's "OpenCV Object Detection in Games" playlist.](https://www.youtube.com/playlist?list=PL1m2M8LQlzfKtkKq2lK5xko4X-8EZzFPI) Besides the ins-and-outs of OpenCV, Ben's videos also helped me learn a lot about classes in python. Specifically the code for fast window capture. Check out [learncodebygaming's github](https://github.com/learncodebygaming) and [opencv_tutorials](https://github.com/learncodebygaming/opencv_tutorials) repo!

Inspiration was also taken from [Clarity Coder's "Computer Vision - OpenCV" playlist.](https://youtube.com/playlist?list=PLFAkc-SDlaKwdZqul_KTpNsw1U2ViKmbD) This was where I first encountered the OpenCV library and got the idea for this project, so many thanks!


## Virtual Environment and Packages

I tried to use conda as a package manager but most of the libraries worked better with 'pip' and a plain python virtual environment ([venv](https://docs.python.org/3/library/venv.html)).

I also ended up downloading [NVIDIA's CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit) for use with [EasyOCR](https://github.com/JaidedAI/EasyOCR) and it's [PyTorch](https://pytorch.org/) dependancies. 

### [Added a requirements.txt instead.](https://stackoverflow.com/questions/51863155/do-we-need-to-upload-virtual-env-on-github-too) 