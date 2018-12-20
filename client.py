import socket


host = '0.0.0.0'
data_payload = 2048
backlog = 5
ack = 'test223'
ack = bytes(ack, encoding='utf-8')


def echo_server(port):
    sock = socket.socket(socket.AF_INET, socket. SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (host, port)
    print("Starting up echo server on %s port %s" % server_address)
    sock.bind(server_address)
    sock.listen(backlog)

    while True:
        print('Waiting to receiving message from client')
        client, address = sock.accept()
        data = client.recv(data_payload)
        if data:
            print('Data: %s' % data)
            client.send(ack)
            print('Sent: %s back to %s' % (ack, address))
        client.close()


if __name__ == '__main__':
    echo_server(1234)







