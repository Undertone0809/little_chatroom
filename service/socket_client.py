# -*- coding: utf-8 -*-
# @Time    : 2022/6/8 01:37
# @Author  : Zeeland
# @File    : socket_client.py
# @Software: PyCharm
import socket

from service.meta_socket import BaseSocket

class ChatClient(BaseSocket):
    """运行程序前需要先启动该服务器"""

    def __init__(self):
        self.socket = None       # socket实例
        self.has_open = False    # 判断是否打开

    def start(self):
        # 创建socket实例
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 连接服务端
        self.socket.connect(('localhost',33333))
        self.has_open = True
        print('[info] socket client start')

    def send_msg(self,msg):
        """向服务端发布信息"""
        print('[info] ready to send msg')
        temp_msg = bytes(msg,encoding='utf-8')
        self.socket.sendall(temp_msg)
        print('[info] send msg success')

if __name__ == '__main__':
    """you can test here"""
    c = ChatClient()
    c.start()
