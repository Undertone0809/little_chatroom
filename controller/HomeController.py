# -*- coding: utf-8 -*-
# @Time    : 2022/5/12 16:48
# @Author  : Zeeland
# @File    : HomeController.py
# @Software: PyCharm

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QBrush, QColor, QPalette, QPixmap, QRegExpValidator, QIntValidator
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QLineEdit, QAbstractItemView, QHeaderView, QTableWidget, \
    QTableWidgetItem, QMainWindow, QDesktopWidget, QAction

from concurrent.futures import ThreadPoolExecutor
import socket
import os

from views.home import Ui_MainWindow
from service.socket_server import ChatServer
from service.socket_client import ChatClient

class HomeController(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,socket_mode=None,thread_pool=ThreadPoolExecutor(max_workers=5)):
        super().__init__()
        try:
            # 参数初始化
            self.thread_pool = thread_pool
            self.socket_mode = socket_mode
            self.socket_service = None
            # 判断当前为服务端App还是客户端App
            if self.socket_mode=='server':
                self.thread_pool.submit(self.create_server)
            elif self.socket_mode=='client':
                self.thread_pool.submit(self.create_client)

        except Exception as e:
            print('[error] HomeController init error:',e)

        # 往空的QWidget里面放置UI内容
        self.setupUi(self)
        self.initAttr()
        self.initFun()

    # 属性处理
    def initAttr(self):
        # 创建
        self.setWindowTitle("ChatRoom by "+self.socket_mode)

        # 设置背景图片
        palette = QtGui.QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap(os.getcwd()+"\static\images\\bg1.jpg")))
        self.setPalette(palette)

    # 信号与槽绑定
    def initFun(self):
        # 发送按钮绑定对应回调函数
        self.btn_send.clicked.connect(self.send_msg)

    # 发送信息
    def send_msg(self):
        # 获取textEdit控件（输入框）中的文字
        word = self.textEdit.toPlainText()
        # 非空判断
        if word == '':
            QMessageBox.about(self,"提示", "发送内容不能为空！")
        else:
            # 发送信息给服务端（客户端）
            self.socket_service.send_msg(word)
            # textBrowser控件追加文字
            self.textBrowser.append(self.socket_mode+":\n" + word+'\n')
            # 输入框清零
            self.textEdit.setText('')

    # 创建客户端
    def create_client(self):
        self.socket_service = ChatClient()
        self.socket_service.start()

        while True:
            # 监听从服务端发来的消息
            res_msg = str(self.socket_service.socket.recv(1024),encoding='utf-8')
            # 发来的消息追加显示到textBrowser控件上显示出来
            self.textBrowser.append("server:\n"+res_msg+'\n')
            print('[info] rec from server', res_msg)

    # 创建服务器
    def create_server(self):
        self.socket_service = ChatServer()
        self.socket_service.start()

        # 监听连接
        while True:
            # 返回客户端的连接，conn为client socket
            client, addr = self.socket_service.socket.accept()
            self.socket_service.client_list.append(client)

            # 如果检测到新的客户端，则打开一个新的线程
            self.thread_pool.submit(self.hanle_client, client, addr)

    def hanle_client(self,client,addr):
        """处理客户端的请求"""
        with client:
            print('[info] conn by', addr)
            client.sendall(b'hello client!')
            while True:
                try:
                    # 监听客户端发来的消息
                    res_msg = str(client.recv(1024),encoding='utf-8')
                    if not res_msg:
                        break
                    print("[info] rec from client:"+res_msg)
                    # 将发来的消息追加到textBrowser控件中显示
                    self.textBrowser.append("client:\n"+res_msg+'\n')
                except Exception as e:
                    print(e)
                    return
