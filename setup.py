import sys

from setuptools import setup

if sys.version_info.major != 3:
    print("This module is only compatible with Python 3, but you are running "
          "Python {}. The installation will likely fail.".format(sys.version_info.major))

setup(
    name='tensorvault',
    packages = ['tensorvault'],
    version='0.0.1',
    install_requires=[
        "path.py==10.3"
    ],
    author='Tom B Brown',
    author_email='nottombrown@gmail.com',
    url = 'https://github.com/nottombrown/tensorvault',
    # https://github.com/tensorflow/tensorflow/issues/7166#issuecomment-280881808
    extras_require={
        "tf": ["tensorflow ~= 1.2"],
        "tf_gpu": ["tensorflow-gpu >= 1.1"],
        "test": [
            'pytest ~= 3.2',
        ]
    }
)
