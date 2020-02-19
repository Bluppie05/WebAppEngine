import os
import platform

system = platform.system()

if system == 'Windows':
    os.system("pip install pyqt5")
    os.system("pip install pyqtwebengine")
    print("The needed dependencies are installed, on every system this webapp is deployed you need to run setup.py")
elif system == 'Macos':
    os.system("pip install pyqt5")
    os.system("pip install pyqtwebengine")
    print("The needed dependencies are installed, on every system this webapp is deployed you need to run setup.py")
elif system == 'Linux':
    os.system("sudo apt install python3-pyqt5")
    os.system("sudo apt install python3-pyqt5.qtwebengine -y")
    print("The needed dependencies are installed, on every system this webapp is deployed you need to run setup.py")