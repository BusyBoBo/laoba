# coding:utf-8
import json
import logging

from PyQt4.QtCore import *
from PyQt4.QtGui import QPalette

from myutil.MyTool import beautiful_log


class MyUpdateHistoryResultDataAction(object):
    @staticmethod
    @beautiful_log
    @pyqtSlot(dict)
    def run(console_instance, data_dict):
        try:
            logging.info(u"【控制台】更新历史结果数据")
            console_instance.history_data = data_dict
            QMetaObject.invokeMethod(console_instance.parent, "updateHistoryResultData", Qt.QueuedConnection,
                         Q_ARG(dict, data_dict))
            logging.info(u"【更新历史结果数据】写到文件config/history.json")
            with open('config/history.json', 'wb') as f:
                f.write(json.dumps(console_instance.history_data['data']['result']))
        except Exception, ex:
            logging.error(ex, exc_info=1)
