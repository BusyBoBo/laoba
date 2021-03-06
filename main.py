# #coding:utf-8
import sys
import logging

from PyQt4 import QtGui

from myutil.MainWindow import MainWindow
from myutil.MyLogUtil import MyLogUtil

if __name__ == '__main__':
    MyLogUtil.init_logging()

    try:
        app = QtGui.QApplication(sys.argv)
        MainWindow()
        sys.exit(app.exec_())
    except Exception, ex:
        logging.error(ex, exc_info=1)
