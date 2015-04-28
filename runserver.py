#!/usr/local/bin/python2.7

import sys
import os
from main import app
from upload_s3 import set_metadata
from flask_frozen import Freezer

#converting to relative os path
# http://stackoverflow.com/questions/4297450/convert-backward-slash-to-forward-slash-in-python

def directoryInFiles(name):
    manDir = os.path.normpath("\\main\\Build\\")

    f = open(cwd + manDir + name, 'r+')
    newPython = f.read()
    f.close()
    newPython = newPython.replace("/static/","/VPRClassical-static/")
    b = open(cwd + manDir + name, 'w+')
    b.write(newPython)
    b.close()


#!!!!!!!!
if len(sys.argv) > 1 and sys.argv[1] == 'freeze':
    freezer = Freezer(app)
    freezer.freeze()
    cwd = os.getcwd()
    old = cwd + os.path.normpath('\\main\\Build\\static')
    new = cwd + os.path.normpath("\\main\\Build\\VPRClassical-static")
    os.rename(old,new)
    directoryInFiles("vpr-classical")
    directoryInFiles("vpr-classical-calendar")
    set_metadata()

#!!!!!!!!
else:
    app.debug = True
    app.run()



    
