#!/usr/bin/python

import os
import string
import time
import shutil

###################################################
__SRCDIR__ = "/mnt/camera"
__DESTDIR__ = "/home/videos/raw"
###################################################
def cbwalk(arg, dirname, names):
    sdatetime = time.strftime("%y%m%d%H%M")
    for name in names:
    	if string.lower(name[-3:]) in ("nts"):
    		srcfile = "%s/%s" % (dirname, name)
    		destfile = "%s/%s_%s" % (__DESTDIR__, sdatetime, name)
                	print destfile
    		shutil.copyfile( srcfile, destfile)
###################################################
if __name__ == "__main__":
    os.path.walk(__SRCDIR__, cbwalk, None)
