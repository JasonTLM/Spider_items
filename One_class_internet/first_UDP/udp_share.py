import socket

def send_to(udp_socket):
    # 发送数据
    dest_ip = input("请输入目标ip地址：")
    dest_port = int(input("请输入目标端口："))
    send_date = input("请输入要发送的数据：")
    udp_socket.sendto(send_date.encode("utf-8"),(dest_ip,dest_port))


def recv_from(udp_socket):
    recv_date = udp_socket.recvfrom(1024)
    print("%s:%s" % (str(recv_date[1]),recv_date[0].decode("utf-8")))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    while True:
        # 调用函数，发送数据
        send_to(udp_socket)
        # 调用函数，接收数据
        recv_from(udp_socket)

    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()