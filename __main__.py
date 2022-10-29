#!/usr/bin/env python3
import os
try:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

except Exception as e:
    print(e)
from PyQt5 import QtWidgets, Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from viewManagers.mainWindowManager import MainWindow
import sys

def main():
    app = QApplication(sys.argv)
    # app.setAttribute(Qt.AA_UseHighDpiPixmaps)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()