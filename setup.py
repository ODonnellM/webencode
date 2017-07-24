from distutils.core import setup
setup(
    name = 'webencode',
    packages = ['webencode'],
    version = '1.0',
    install_requires = ['ffprobe', 'subprocess', 'signal', 'tempfile', 'argparse']
    description = 'An ffmpeg wrapper for encoding various videos into web compatible formats',
    author = "Mike O'Donnell",
    author_email = "mike@devferret.com",
    url = "https://github.com/ODonnellM/webencode",
    download_url = "https://github.com/odonnellm/webencode/archive/1.0.tar.gz",
    keywords = ['video', 'transcode', 'encode', 'ffmpeg', 'cross browser'],
    classifiers = [],
)
