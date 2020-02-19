from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import os
import urllib.request
import json
import re
import platform

import sys

system = platform.system()

namepath = "app.config"
f = open(namepath)
config = f.read()
replaceconfig = config.replace("title: ", "")

currentfile = os.path.abspath(__file__)

#replace dictionary
dic = {'webengine.py':'index.html', '\\':'/'}

#multireplace function
def multiple_replace(string, rep_dict):
    pattern = re.compile("|".join([re.escape(k) for k in sorted(rep_dict,key=len,reverse=True)]), flags=re.DOTALL)
    return pattern.sub(lambda x: rep_dict[x.group(0)], string)

replacedindexfile = multiple_replace(currentfile, dic)
if system == 'Windows':
    indexfile = "file:///" + replacedindexfile
else:
    indexfile = "file://" + replacedindexfile
print(indexfile)

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, *kwargs)

        self.setWindowTitle(replaceconfig)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(indexfile))

        self.setCentralWidget(self.browser)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()