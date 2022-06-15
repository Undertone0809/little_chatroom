# -*- coding: utf-8 -*-
# @Time    : 2022/6/8 00:58
# @Author  : Zeeland
# @File    : socket_server.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# @Time    : 2022/6/7 15:31
# @Author  : Zeeland
# @File    : service.py
# @Software: PyCharm
import socket

from service.meta_socket import BaseSocket

class ChatServer(BaseSocket):
    """运行程序前需要先启动该服务器"""

    def __init__(self,ip_add='localhost',port=33333):
        self.ip_add = ip_add    # 服务端ip地址
        self.port = port        # 服务端端口
        self.client_list = []   # 存放连接的客户端
        self.socket = None      # socket实例
        self.has_open = False   # 判断是否打开服务端监听

    def start(self):
        # 创建socket实例
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 服务端绑定ip和port
        self.socket.bind((self.ip_add,self.port))
        # 开启服务端
        self.socket.listen()
        self.has_open = True
        print('[info] socket server start')
        """controller端需要实现客户端监听部分的代码"""

    def send_msg(self,msg):
        """向所有客户端发送广播信息"""
        print('[info] ready to send msg')
        temp_msg = bytes(msg,encoding='utf-8')
        for client in self.client_list:
            client.sendall(temp_msg)
        print('[info] send msg success')

if __name__ == '__main__':
    """you can test here"""
    s = ChatServer()
    s.start()
