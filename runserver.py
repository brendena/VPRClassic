#!/usr/local/bin/python2.7

import sys
import os
from main import app
from upload_s3 import set_metadata
from flask_frozen import Freezer

def directoryInFiles(name):
    f = open(cwd + "\\main\\Build\\" + name, 'r+')
    newPython = f.read()
    f.close()
    newPython = newPython.replace("/static/","/VPRClassical-static/")
    b = open(cwd + "\\main\\Build\\" + name, 'w+')
    b.write(newPython)
    b.close()


#!!!!!!!!
if len(sys.argv) > 1 and sys.argv[1] == 'freeze':
    freezer = Freezer(app)
    freezer.freeze()
    cwd = os.getcwd()
    old = cwd + '\\main\\Build\\static'
    new = cwd + "\\main\\Build\\VPRClassical-static"
    os.rename(old,new)
    directoryInFiles("vpr-classical")
    directoryInFiles("vpr-classical-calendar")
    set_metadata()

#!!!!!!!!
else:
    app.debug = True
    app.run()



    
