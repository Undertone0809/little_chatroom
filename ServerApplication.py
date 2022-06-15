# -*- coding: utf-8 -*-
# @Time    : 2022/6/8 00:56
# @Author  : Zeeland
# @File    : ServerApplication.py
# @Software: PyCharm
from PyQt5 import QtWidgets
from controller.HomeController import HomeController

from concurrent.futures import ThreadPoolExecutor

# main Application
if __name__ == "__main__":
    import sys
    # 创建线程池
    pool=ThreadPoolExecutor(max_workers=5)

    # 创建UI，启动UI
    app = QtWidgets.QApplication(sys.argv)
    a = HomeController(socket_mode='server',thread_pool=pool)
    a.show()
    sys.exit(app.exec_())

