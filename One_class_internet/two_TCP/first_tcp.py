import socket

def main():
    # 创建tcp套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 链接服务器
    server_ip = input("请输入目标服务器的IP地址：")
    server_port = int(input("请输入目标服务器的端口号："))
    server_adds = (server_ip,server_port)
    tcp_socket.connect(server_adds)
    # 收发数据
    # 1.发送数据
    send_date = input("请输入要发送的数据：")
    tcp_socket.send(send_date.encode("utf-8"))

    # 2.接收数据
    recv_date = tcp_socket.recv(1024)
    print("接收消息：",recv_date.decode("utf-8"))
    #关闭tcp套接字
    tcp_socket.close()


if __name__ == "__main__":
    main()