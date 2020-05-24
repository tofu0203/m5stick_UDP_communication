# from socket import socket, AF_INET, SOCK_DGRAM

# M_SIZE = 1024

# HOST = '192.168.10.17'
# PORT = 22222

# # ソケットを用意
# s = socket(AF_INET, SOCK_DGRAM)
# # バインドしておく
# s.bind((HOST, PORT))

# while True:
#     try:
#         # 受信
#         print("test")
#         msg, address = s.recvfrom(M_SIZE)
#         print(f"message: {msg}\nfrom: {address}")
#     except KeyboardInterrupt:
#         print('\n . . .\n')
#         s.close()

from socket import *

# UDP受信クラス


class udprecv():
    def __init__(self):

        SrcIP = "192.168.10.7"                             # 受信元IP
        SrcPort = 11111                                 # 受信元ポート番号
        self.SrcAddr = (SrcIP, SrcPort)                 # アドレスをtupleに格納

        self.BUFSIZE = 1024                             # バッファサイズ指定
        self.udpServSock = socket(AF_INET, SOCK_DGRAM)  # ソケット作成
        self.udpServSock.bind(self.SrcAddr)             # 受信元アドレスでバインド

    def recv(self):
        while True:                                     # 常に受信待ち

            data, addr = self.udpServSock.recvfrom(self.BUFSIZE)
            # 受信
            print(data.decode(), addr)                  # 受信データと送信アドレス表示


udp = udprecv()     # クラス呼び出し
udp.recv()          # 関数実行
