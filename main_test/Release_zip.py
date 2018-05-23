# -*- coding: utf-8 -*-
"""
this is the release zip to temporary directory for  Yanteng's game analysis program,
Author : fibonacci
connect : ericpan1124@yahoo.com
Edit date :20180523
Accomplish : No
Final : No
"""
import zipfile as zf
import os
import shutil

fPath = os.path.abspath('..').replace('\\', '/')
tmpPath = fPath + "/tmp"
gameDegree = fPath + "/data/lvl"   #or easy and so on ， should be variable at last