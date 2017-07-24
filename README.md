# Webencode.py

Webencode is a simple python wrapper around ffmpeg.

This wrapper provides anyone the ability to take any ffmpeg [compatible video format](https://en.wikipedia.org/wiki/FFmpeg#Supported_formats) and convert it into any or all web compatible formats: mp4, webm and ogg.

### Installation

Currently, webencode is only available through github. Feel free to download or clone the repository and use it your own discretion. The project is currently waiting to be uploaded to PyPi.


### Dependencies

Webencode is built off python 2.7 and is dependant on ffmpeg being installed. 
It is also dependant on the packages ffprobe, tempfile, argparse and tempfile in case you don't have them with the default python install.

### Usage

Webencode is very easy to use and only provides a fe command line arguments

| argument | description | example |
|:--------:|:-----------:|:-------:|
|   -h     |Display help                     | webencode -h                      |
|   -i     |Input filename                   | webencode -i video.mp4            |
|   -o     |Set base name for new files      | webencode -i video.mp4 -o newVideo|
|   -d     |Directory to place encoded videos| webencode -i video.mp4 -d ~/Videos|
|   -f     |specific formats to encode to    | webencode -i video.mp4 -f webm ogg|
|   -y     |Force overwrite when encountered | webencode -i video.mpy -y         |

### Future
This is considered the first stable release of webencode. There are some features not yet implemented as well as a few bugs that I have missed here and there. Anything you do find going wrong, please make me aware of or feel free to submit a pull request!
