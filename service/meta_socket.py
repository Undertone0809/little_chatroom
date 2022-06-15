# -*- coding: utf-8 -*-
# @Time    : 2022/6/11 13:45
# @Author  : Zeeland
# @File    : meta_socket.py
# @Software: PyCharm
import abc

class BaseSocket(metaclass=abc.ABCMeta):
    """SocketServer和SocketClient的抽象类"""

    @abc.abstractmethod
    def start(self):
        """开始监听"""
        pass

    @abc.abstractmethod
    def send_msg(self,msg):
        """发送广播信息"""
        pass
