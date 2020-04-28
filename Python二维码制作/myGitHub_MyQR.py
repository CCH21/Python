#!/usr/bin/env python3

from MyQR import myqr
import os

myqr.run(
    words='https://github.com/CCH21',
    version=1,
    level='H',
    picture='GitHub_logo.jpg',
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name='myGitHub_MyQR.png',
    save_dir=os.getcwd()
)
